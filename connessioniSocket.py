import socket as so
''' se vuoto utilizza tutte le interfacce, 
    altrimenti quella di appartenenza dell'ip 
    esempio se ho 192.168.50.100 su eth0
    mi bastera' mettere 192.168.50.100 per usare eth0
    mente se voglio usare solo lo dovrei mettere 127.0.0.1
'''
SRV_ADDR = "" 
SRV_PORT = 4444
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Sto attendendo una connessione...")
connection, address = s.accept()
print("Ho stabilito una connessione con: ", address)
while True:
    connection.sendall(b"$ ")
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b"Ho ricevuto il messaggio! \n")
    print(data.decode('utf-8'))
connection.close()
