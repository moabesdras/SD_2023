
import socket
import datetime

def conexao_cliente(client_address, data):
    h = str(datetime.datetime.now().hour) + 'h:' + str(datetime.datetime.now().minute) + 'm:' + str(
        datetime.datetime.now().second) + 's'
    
    server_socket.sendto(h.encode(), client_address)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 20001)
server_socket.bind(server_address)

print("Iniciando servidor na porta %s %s" % server_address)
data, client_address = server_socket.recvfrom(2048)
conexao_cliente(client_address, data)
