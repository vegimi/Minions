import socket
import sys

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Client")
print("\n------------------------------------------------------------------------------\n")


print("Miresevini ne Vegim's client:\n")
print("\t Kerkesa duhet te jete brenda domenes se serverit per te ditur domenen e serverit sheno: help/h\n")

serverName = "127.0.0.1"
serverPort = 9000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

message = raw_input("Kerkesa:")
clientSocket.send(message.encode('ASCII'))
modifiedMessage = clientSocket.recv(4096)
print("From Server:"+ modifiedMessage.decode('ASCII'))
clientSocket.close()
