import socket
from error_methods import corrupt_data

SERVER_HOST = "localhost"
SERVER_PORT = 5000
CLIENT2_PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen(1)

print("🟢 Server is running...")

while True:
    conn, addr = server.accept()
    packet = conn.recv(1024).decode()
    print("Received:", packet)

    # SAFE PACKET PARSING (2D PARITY FIX)
    parts = packet.split("|")
    data = parts[0]
    method = parts[1]
    control = "|".join(parts[2:])

    corrupted_data , error_type= corrupt_data(data) 
    
    if error_type is None:
        error_type = "NONE"


    new_packet = f"{corrupted_data}|{method}|{control}|{error_type}"

    forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward.connect((SERVER_HOST, CLIENT2_PORT))
    forward.send(new_packet.encode())
    forward.close()

    conn.close()


