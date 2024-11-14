import socket as so

SRV_ADDR = ""
SRV_PORT = 4444
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Sto attendendo una connessione...")
connection, address = s.accept()
print("Ho stabilito una connessione con: ", address)
while True:
    prompt = "$ "
    connection.sendall(prompt.encode("utf-8"))
    data = connection.recv(1024)
    if not data: break
    comando = data.decode("utf-8")
    result = ""
    if (comando == 'ls'):
        result = "Mi spiace, non ancora disponibile"
    elif (comando.startswith('rm')):
        result = "Ci hai provato!"
    else:
        result = "Non trovato"
    connection.sendall(result.encode("utf-8"))
connection.close()
