
package RMI;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface RemoteInterface extends Remote {
    void storeMessage(String message) throws RemoteException;

    List<String> getMessages() throws RemoteException;

    String getServerIP() throws RemoteException;

    String getServerDateTime() throws RemoteException;
}
