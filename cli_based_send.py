# the is limit of port is in between 0 to 65536. 
 #192.168.71.236

import socket 
                ##dgram is a medium is used to send the msg.         
                ##socket library helps to communicate without connection.
              
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
ip_address =  '172.20.10.4'
port = 6565
target = (ip_address,port)
message = input("enter the message: ")
encript_message = message.encode('ascii')
s.sendto(encript_message,target)       #sendto is a built-in function.
# except Exception as e:
#     print("msg not sent")       #if there is any error then it execute.

