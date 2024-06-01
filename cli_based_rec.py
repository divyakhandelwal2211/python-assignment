import socket   ##socket library helps to communicate without connection.
              
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
ip_address =  '192.168.190.236'
port = 2233
target = (ip_address,port)
s.bind(target)
while True:
    message = s.recvfrom(120)
    print(message)
    data = message[0]
    data = '\n'
    print(data.encode('ascii'))
# except Exception as e:
#     print('message is received')     