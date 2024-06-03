import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = '192.168.190.236'
port = 2233
target = (ip_address, port)

# User input to either send a message or a file
choice = input('Do you want to send a (1) message or (2) file? Enter 1 or 2: ')

if choice == '1':
    msg = input('Enter the message: ')
    encrypted_msg = msg.encode('ascii')
    s.sendto(encrypted_msg, target)
    print('Message sent')

elif choice == '2':
    # Specify the filename to send, e.g., hello.txt
    file_path = 'hello.txt'
    try:
        with open(file_path, 'rb') as f:
            file_name = file_path.split('/')[-1]
            s.sendto(f'FILE:{file_name}'.encode('ascii'), target)

            # Read and send file content in chunks
            while chunk := f.read(4096):
                s.sendto(chunk, target)
            s.sendto(b'EOF', target)
        print(f"File '{file_name}' sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

else:
    print("Invalid choice.")
