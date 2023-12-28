import socket
import json
import argparse

from utils.parse_response import parse_response

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", help="Client device. Will indicate which config file to use", default="bb")
args = parser.parse_args()

with open(f"experiments/{args.device}_config.json") as config_file:
	config = json.load(config_file)

HOST = config["host"]	# Server address!!
PORT = config["port"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print(f"Connected by {addr}")
		# while True:
		# 	data = conn.recv(1024)
		# 	if not data:
		# 		break
		# 	# conn.sendall(data)
		while True:
			command_str = input("Command: ").strip().lower()
			conn.sendall(command_str.encode())

			response = parse_response(conn.recv(1024).decode())
			print(response)

			# Echo response to client
			conn.sendall(f"Server Received: {response}".encode())

			if command_str == "close":
				break
