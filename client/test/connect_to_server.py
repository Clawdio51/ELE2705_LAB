import socket
import json


HOST = "132.207.64.218"  # The server's hostname or IP address
PORT = 54654  # The port used by the server

config = {}
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    response = str({"status": "OK", "data": "data"})
    s.sendto(json.dumps(response).encode(), (HOST, PORT))

    # Print server echo reply
    reply, addr = s.recvfrom(1024)
    print(reply.decode())