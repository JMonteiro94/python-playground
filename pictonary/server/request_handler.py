import socket
import threading
from player import Player
from game import Game
import json


class Server(object):
    PLAYERS_PER_GAME = 8

    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        while True:
            try:
                try:
                    data = conn.recv(1024)
                    data = json.loads(data.decode())
                    print("[LOG] Received data: ", data)
                except:
                    break

                keys = data.keys()
                send_msg = {int(key): [] for key in keys}

                for key in keys:
                    if key == -1:  # get game
                        if player.game:
                            send_msg[-1] = player.game.players
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0:  # guess
                            correct = player.game.player_guess(player, data[0][0])
                            send_msg[0] = correct
                        elif key == 1:  # skip
                            skip = player.game.skip()
                            send_msg[1] = skip
                        elif key == 2:  # get chat
                            content = player.game.round.chat.get_chat()
                            send_msg[2] = content
                        elif key == 3:  # get board
                            brd = player.game.board.get_board()
                            send_msg[3] = brd
                        elif key == 4:  # get score
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores
                        elif key == 5:  # get round
                            rnd = player.game.round_count
                            send_msg[6] = rnd
                        elif key == 6:  # get word
                            word = player.game.round.word
                            send_msg[6] = word
                        elif key == 7:  # skips
                            skips = player.game.round.skips
                            send_msg[0] = skips
                        elif key == 8:  # update board
                            x, y, color = data[8][:3]
                            self.game.update_board(x, y, color)
                            send_msg[0] = skips
                        elif key == 9:  # get round time
                            t = self.game.round.time
                            send_msg[9] = t

                    if key == 10:  # disconnect
                        raise Exception("Not a valid request")

                conn.sendall(json.dumps(send_msg).encode())

            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected:", e, e.args)
                conn.close()
                break
        print(f"[DISCONNECT] {player.get_name()} disconnected")
        conn.close()

    def handle_queue(self, player):
        self.connection_queue.append(player)
        if len(self.connection_queue) > self.PLAYERS_PER_GAME:
            game = Game(self.game_id, self.connection_queue[:])

            for p in self.connection_queue:
                p.set_game(game)

            self.game_id += 1
            self.connection_queue = []

    def authentication(self, conn, addr):
        try:
            data = conn.recv(16)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")
            conn.sendall("1".encode())

            player = Player(addr, name)
            self.handle_queue(player)
            thread = threading.Thread(target=self.player_thread, args=(conn, player))
            thread.start()
        except Exception as e:
            print("[EXCEPTION] ", e)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

    def connection_thread(self):
        server = "localhost"
        port = 5500

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen()
        print("waiting for a connection, server started...")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New connection !")

            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    thread = threading.Thread(target=s.connection_thread)
    thread.start()
