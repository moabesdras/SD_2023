
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 21212), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    mensagens = []

    def armazenar(mensagem):
        mensagens.append(mensagem)
        return True

    def getMensagens():
        return mensagens

    def getIP():
        return socket.gethostbyname(socket.gethostname())

    def getDataHora():
        return datetime.now().strftime('%Y-%m-%d %H:%M')

    server.register_function(armazenar, 'armazenar')
    server.register_function(getMensagens, 'getMensagens')
    server.register_function(getIP, 'getIP')
    server.register_function(getDataHora, 'getDataHora')

    print("Servidor XML-RPC rodando. Pressione Ctrl+C para encerrar.")
    server.serve_forever()
