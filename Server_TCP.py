import socket
import AlphaBot
import time

def gestisci(c):
    destro, sinistro = larry.getSensor()

    if destro != 0 and sinistro != 0:
        if c == "w":
                larry.forward()

        elif c == "a":
            larry.left()

        elif c == "s":
            larry.backward()

        elif c == "d":
            larry.right()

        elif c == "stop":
            larry.stop()
            
        elif c == "finish":
            s.close()
            connection.close()

        elif c.startswith("DB"):
            comando = c.replace("DB", "")
            if comando == "forward":
                larry.forward()
            elif comando == "left":
                larry.left()
            elif comando == "backward":
                larry.backward()
            elif comando == "right":
                larry.right()
                
    else:
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
s.listen(NUMERO_CONNESSIONI) # Aspetta connessioni
connection, device_address = s.accept()

while True:
    data = connection.recv(BUFFER)
    istruzione = data.decode()
    print(f"Key: {istruzione}")

    gestisci(istruzione)
