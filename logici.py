if(1 < 3): print("Vero")
if(1 > 3):
    print("non stampa") # questo perche' falso
else:
    print("Vero")
if(1 <= 1): print("Vero")
if(1 >= 1): print("Vero")
if(2 != "Uno"): print("Vero")
if(1 == 1): print("Vero")
if(type(1) is int): print("e' un intero")
if(type("Ciao") is not int): print("non e' un intero")
lista = [1,2,3,"pippo"]
if ("pippo" in lista): print("Pippo e' in lista")
if ("Paolo" not in lista): print("Paolo non e' in lista")
if(not 1 > 1): print("nego la maggioranza")
if((1 > 1) or (2 == 2)): print("la seconda e' vera")
if((1 == 1) and ("pippo" == "pippo")): print("sono entrambe vere")
if(1 == "1"): print("Falso")

