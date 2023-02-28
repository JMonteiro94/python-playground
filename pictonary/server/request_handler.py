import socket
import threading
import time
from .player import Player
from .game import Game
from queue import Queue
import json

class Server(object):
    PLAYERS_PER_GAME = 8
    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        while True:
            try:
                data = json.load(conn.recv(1024))
                keys = [key for key in data.keys()]
                send_msg = {key:[] for key in keys}

                for key in keys:
                    if key == -1: # get game
                        if player.game:
                            send_msg[-1] = player.game.players
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0: # guess
                            correct = player.game.player_guess(player, data[0][0])
                            send_msg[0] = [correct]

                        elif key == 1: # skip

                        elif key == 2: # get chat

                        elif key == 3: # get board

                        elif key == 4: # get score

                        elif key == 5: # get round

                        elif key == 6: # get word

                        elif key == 7: # skips

                        elif key == 8: # update board

                        elif key == 9: # get round time

                        else:
                            raise Exception("Not a valid request")

                conn.sendall(json.dumps(send_msg))

            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected:", e)
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
            threading.Thread(target=self.player_thread, args=(conn, addr, player))
        except Exception as e:
            print("[EXCEPTION] ", e)
            conn.close()

    def connection_thread(self):
        server = ""
        port = 5555

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
    threading.Thread(target=s.connection_thread)