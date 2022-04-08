import socket

c=socket.socket()

c.connect(("168.62.48.183",80))

name=input("Enter The Name")

c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())