
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 20001)

message = "hora atual"
print ("Solicitando %s..." % message)
time.sleep(2)
client_socket.sendto(message.encode(), server_address)

data, server = client_socket.recvfrom(2048)
print(f"Hora atual: {data.decode()}")
client_socket.close()
