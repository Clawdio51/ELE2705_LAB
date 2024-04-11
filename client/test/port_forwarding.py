import socket
import threading

# TODO: Might need to remove multithreading and directly wait for reply from server and forward to client after the initial forward

# Forward to server
S_LISTEN_ADDRESS    = "192.168.7.1"
S_LISTEN_PORT       = 54654
S_CONNECT_ADDRESS   = "192.168.7.1"
S_CONNECT_PORT      = 12345

# Forward to client
# C_LISTEN_ADDRESS    = "192.168.0.1"
# C_LISTEN_PORT       = 12345
# C_CONNECT_ADDRESS   = "192.168.7.2"
# C_CONNECT_PORT      = 54654

def forward(listenaddress, listenport, connectaddress, connectport):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as private_socket:
        private_socket.bind((listenaddress, listenport))
        while True:

            data, client_addr = private_socket.recvfrom(1024)
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as public_socket:
                public_socket.sendto(data, (connectaddress, connectport))
                response, server_addr = public_socket.recvfrom(1024)
            private_socket.sendto(response, client_addr)

if __name__ == "__main__":

    forward(S_LISTEN_ADDRESS, S_LISTEN_PORT, S_CONNECT_ADDRESS, S_CONNECT_PORT)

    # t1 = threading.Thread(target=forward, args=(S_LISTEN_ADDRESS, S_LISTEN_PORT, S_CONNECT_ADDRESS, S_CONNECT_PORT))
    # t2 = threading.Thread(target=forward, args=(C_LISTEN_ADDRESS, C_LISTEN_PORT, C_CONNECT_ADDRESS, C_CONNECT_PORT))

    # t1.start()
    # t2.start()
    
    # t1.join()
    # t2.join()