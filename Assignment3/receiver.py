import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = '192.168.190.69'
port = 2222
target = (ip_address, port)
s.bind(target)

while True:
    # Receive message from the sender
    msg, addr = s.recvfrom(4096)
    if msg:
        data = msg.decode('ascii')

        # Check if the message indicates a file transfer
        if data.startswith("FILE:"):
            filename = data.split(":")[1]
            with open(filename, 'wb') as f:
                while True:
                    file_data = s.recvfrom(4096)
                    if file_data == b'EOF':
                        break
                    f.write(file_data)
            print(f"File '{filename}' received successfully.")
        else:
            print(f"Message from {addr}: {data}")
