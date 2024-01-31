
import xmlrpc.client
import socket

serv = xmlrpc.client.ServerProxy('http://localhost:21212')

serv.armazenar("Hello")
serv.armazenar("World!")
print(serv.getMensagens())
print(serv.getIP())
print(serv.getDataHora())
