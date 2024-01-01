import socket

HOST = "192.168.7.1"
PORT = 54654

DEST_HOST = "192.168.0.1"
DEST_PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        s.sendto(data, (DEST_HOST, DEST_PORT))