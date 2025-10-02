import socket
import AlphaBot
import time
from p5 import *

def key_pressed():
    if key == "w":
        larry.forward()
    elif key == "a":
        larry.left()
    elif key == "s":
        larry.backward()
    elif key == "d":
        larry.right()
    else:
        print("Istruzione non valida.")

def key_released():
    if key == "w" or key == "a" or key == "s" or key =="d":
        larry.stop()

ADDRESS = ("0.0.0.0", 5000) # 0.0.0.0: Indirizzo IP speciale, anche detto "This host"
BUFFER = 4096 # Dimensione del buffer in Byte
NUMERO_CONNESSIONI = 100

# Crea un socket IPv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # STREAM = TCP

larry = AlphaBot.AlphaBot()
larry.stop()
# Questo è un server quindi si fa la .bind(indirizzo, porta)
s.bind(ADDRESS)

print("In attesa di connessioni: ")
n = 5
s.listen(NUMERO_CONNESSIONI) # Aspetta connessioni
connection, device_address = s.accept()
for _ in range(n):
    data = connection.recv(BUFFER)
    istruzione = data.decode()
    print("Comando ricevuto: " + istruzione)

    """data2 = connection.recv(BUFFER)
    tempo = int(data.decode())
    print("Tempo ricevuto" + tempo)"""

s.close()
connection.close()