
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
time.sleep(2)
#Conectando ao servidor
sock.connect(server_address)

message = "hora atual"

print ("Solicitando %s..." % message)
time.sleep(2)
#Enviando mensagem ao servidor
sock.sendall(message.encode('utf-8'))
#Recebendo mensagem do servidor
data = sock.recv(2048)
print(data.decode())
sock.close()
