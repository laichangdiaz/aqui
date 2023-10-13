archivo = open("aqui/nota.txt")
for i in archivo:
    campo= i.split(",")
    print(campo[0])