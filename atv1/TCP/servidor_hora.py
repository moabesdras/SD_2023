
import socket
import threading
import datetime
import time

def conexao_cliente(client, address):
    h = str(datetime.datetime.now().hour) + 'h:' + str(datetime.datetime.now().minute) + 'm:' + str(datetime.datetime.now().second) + 's'

    data = client.recv(2048)

    mensagem = data.decode()
    client.sendall(h.encode())

sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
time.sleep(2)
#Reservando porta
sock.bind(server_address)
#Escutando na porta reservada
sock.listen(1)

#Iniciando protocolo
while (True):
    client, address = sock.accept()
    conexao = threading.Thread(target=conexao_cliente, args=(client, address,))
    conexao.start()
