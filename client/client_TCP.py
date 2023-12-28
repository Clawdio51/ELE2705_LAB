# This client is a demo only. The real client is on the device

import socket
import json
import argparse

from commands.command_factory import get_command
from utils.create_response import create_response
from utils.status_codes import STATUS_CODE

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", help="Client device. Will indicate which config file to use", default="bb")
args = parser.parse_args()

with open(f"experiments/{args.device}_config.json") as config_file:
	config = json.load(config_file)

HOST = config["host"]  # The server's hostname or IP address
PORT = config["port"]  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b"Connected")

    while True:
        command_str = s.recv(1024)

        print(f"Received {command_str!r}")

        command = get_command(command_str.decode())
        response = command()
        s.sendall(create_response(response).encode())

        if response["status"] == STATUS_CODE.CLOSE:
            break

        # Print server echo reply
        echo_reply = print(s.recv(1024).decode())

print("Connection terminated.")
