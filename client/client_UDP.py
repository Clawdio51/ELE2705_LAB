# This client is a demo only. The real client is on the device

import socket
import json
import argparse

from commands.command_factory import get_command
from utils.choose_command import choose_command
from utils.create_response import create_response
from utils.echo_reply import echo_reply
from utils.init_board import initialize_board
from utils.status_codes import STATUS_CODE

import Adafruit_BBIO.GPIO as GPIO

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", help="Client device. Will indicate which config file to use", default="bb")
args = parser.parse_args()

with open(f"experiments/{args.device}_config.json") as config_file:
	config = json.load(config_file)

HOST = config["host"]  # The server's hostname or IP address
PORT = config["port"]  # The port used by the server

initialize_board(config)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        command_str = choose_command(config)
             
        command = get_command(command_str)
        response = command(config)
        s.sendto(create_response(response).encode(), (HOST, PORT))

        if response["status"] == STATUS_CODE.CLOSE:
            break

        # Print server echo reply
        reply, addr = s.recvfrom(1024)
        echo_reply(reply, config)

print("Connection terminated.")
