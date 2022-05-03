# SERVER
import socket
import pickle

from _thread import start_new_thread
from player import Player

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	print(str(e))
	
s.listen(2)  # (number) - number of max connections to server
print("Waiting for a connection, Server Started")

players = [Player(0, 0, 50, 50, (0, 0, 255)), Player(100, 100, 50, 50, (0, 255, 0))]  # init positions for players


def threaded_client(conn, player):
	conn.send(pickle.dumps(players[player]))
	reply = ""
	while True:
		try:
			data = pickle.loads(conn.recv(2048))  # (amount of info we want to receive)
			players[player] = data

			if not data:
				print("Disconnected")
				break
			else:
				if player == 1:
					reply = players[0]
				else:
					reply = players[1]
				print("Received: ", data)
				print("Sending: ", reply)

			conn.sendall(pickle.dumps(reply))
		except:
			break
	print("Lost connection")
	conn.close()


def main():
	current_player = 0
	while True:
		conn, addr = s.accept()
		print("Connected to:", addr)

		start_new_thread(threaded_client, (conn, current_player))
		current_player += 1


if __name__ == "__main__":
	main()
