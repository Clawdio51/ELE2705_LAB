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

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	s.bind((HOST, PORT))
	while True:
		response, addr = s.recvfrom(1024)
		response = parse_response(response.decode())
		print(f"{addr}: {response}")

		# Echo response to client
		s.sendto(f"Server Received: {addr}:{response}".encode(), addr)

