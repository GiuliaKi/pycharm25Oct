import socket

def scan_ports(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Crea un oggetto socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Imposta un timeout per la connessione
            sock.settimeout(1)
            # Prova a connettersi alla porta
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("Scansione interrotta.")
            break
        except socket.gaierror:
            print("L'host non può essere risolto.")
            break
        except socket.error:
            print("Errore di connessione al server.")
            break

    return open_ports

if __name__ == '__main__':
    target_host = input("Inserisci l'indirizzo IP o il nome host da scansionare: ")
    start_port = int(input("Inserisci la porta di inizio: "))
    end_port = int(input("Inserisci la porta di fine: "))

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("Porte aperte:", open_ports)
    else:
        print("Nessuna porta aperta trovata.")
