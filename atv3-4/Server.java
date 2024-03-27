
package RMI;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Server implements RemoteInterface {
    private List<String> messages;
    private String serverIP;

    public Server() {
        messages = new ArrayList<>();
        serverIP = "localhost";
    }

    @Override
    public synchronized void storeMessage(String message) throws RemoteException {
        messages.add(message);
        System.out.println("Mensagem armazenada: " + message);
    }

    @Override
    public synchronized List<String> getMessages() throws RemoteException {
        return messages;
    }

    @Override
    public String getServerIP() throws RemoteException {
        return serverIP;
    }

    @Override
    public String getServerDateTime() throws RemoteException {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm");
        return dateFormat.format(new Date());
    }

    public static void main(String[] args) {
        try {
            Server obj = new Server();
            RemoteInterface stub = (RemoteInterface) UnicastRemoteObject.exportObject(obj, 0);

            Registry registry = LocateRegistry.getRegistry();
            registry.rebind("RemoteInterface", stub);

            System.out.println("Servidor pronto...");
        } catch (Exception e) {
            System.err.println("Erro no servidor: " + e.toString());
            e.printStackTrace();
        }
    }
}
