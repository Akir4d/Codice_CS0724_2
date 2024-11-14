def saluta(nome):
    saluto = f"Ciao, {nome}!"
    return saluto

def somma(a,b):
    return a + b

def saluta_antonio():
    return "Saluta Antonio"

def mia_funzione():
    numero = 7
    print(numero)

globale = 20
def stampa_1():
    global globale
    globale = 30
    print(globale)
    
def stampa_2():
    print(globale)

def sottrazione(x,y):
    return x - y
