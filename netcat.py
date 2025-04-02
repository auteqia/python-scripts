import socket
import sys

def connect_to_netcat(server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            print(f"Connecté à {server_ip}:{server_port}")
            while True:
                message = input("Entrez un message (ou 'exit' pour quitter) : ")
                if message.lower() == 'exit':
                    break
                s.sendall(message.encode('utf-8'))
                data = s.recv(1024)
                print(f"Reçu : {data.decode('utf-8')}")
    except Exception as e:
        print(f"Erreur : {e}")
        
        
def listen_to_netcat(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', port))
            s.listen(1)
            print(f"En attente de connexion sur le port {port}...")

            conn, addr = s.accept()
            with conn:
                print(f"Connexion établie avec {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Reçu : {data.decode('utf-8')}")
                    conn.sendall(data)

    except Exception as e:
        print(f"Erreur : {e}")


if len(sys.argv) < 2:
    print("Usage: python script.py -listen <port> | -connect <server_ip> <server_port>")
    sys.exit(1)

if sys.argv[1] == "-listen":
    port = int(sys.argv[2])
    listen_to_netcat(port)
    
elif sys.argv[1] == "-connect":
    server_ip = sys.argv[2]
    server_port = int(sys.argv[3])
    connect_to_netcat(server_ip, server_port)
else: 
    print("Usage: python script.py -listen <port> | -connect <server_ip> <server_port>")
    sys.exit(1)