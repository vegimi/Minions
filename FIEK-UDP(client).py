import socket

server = "127.0.0.1"
port = 9000

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("UDP Server")
print("\n------------------------------------------------------------------------------\n")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Miresevini ne Vegim's client:\n")
print("\t Kerkesa duhet te jete brenda domenes se serverit per te ditur domenen e serverit sheno: help/h\n")
message = raw_input ("Kerkesa:")

clientSocket.sendto(message.encode("ASCII"),(server,port))

modifiedMessage, serverAddress = clientSocket.recvfrom(4096)

print(modifiedMessage)
