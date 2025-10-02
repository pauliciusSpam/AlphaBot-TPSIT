import socket

SERVER_ADDRESS = ("192.168.1.117", 5000) # Indirizzo IP del server al quale mando un messaggio e sua porta

# Crea un socket IPv4 UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # STREAM = TCP
s.connect(SERVER_ADDRESS)

n = 5
for _ in range(n):
    istruzione = input("Inserisci una direzione in cui muovere il robot (left, right, forward, backward): ")
    s.send(istruzione.encode())
    """tempo = input("Inserisci per quanto tempo eseguire l'istruzione: ")
    s.send(tempo.encode())"""
s.close()