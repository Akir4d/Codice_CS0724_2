a=30
b=70
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}") # divisione intera
print(f"{a} % {b} = {a%b}")   # resto o modulo
print(f"{a} ** 3 = {a**3}") # potenza
f=float(input("inserisci un float: ").replace(",", "."))
print(str(round(f, 1)).replace(".", ","))
