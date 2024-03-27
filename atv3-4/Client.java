
package RMI;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.List;

public class Client {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost");

            RemoteInterface stub = (RemoteInterface) registry.lookup("RemoteInterface");

            // Armazenar uma mensagem
            stub.storeMessage("Hello World!");

            // Recuperar lista de mensagens
            List<String> messages = stub.getMessages();
            System.out.println("Mensagens no servidor:");
            for (String message : messages) {
                System.out.println(message);
            }

            // Obter IP do servidor
            String serverIP = stub.getServerIP();
            System.out.println("IP do servidor: " + serverIP);

            // Obter data e hora do servidor
            String serverDateTime = stub.getServerDateTime();
            System.out.println("Data e hora do servidor: " + serverDateTime);
        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.toString());
            e.printStackTrace();
        }
    }
}
