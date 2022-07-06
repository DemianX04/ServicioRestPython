import json
import requests


def sendData():
    api_url = "http://localhost:8090/Clientes/apiv1/clientes/add"
    todo = {"firstname":"","surname":"", "lenguaje":"", "nombre":"", "lenguaje":"", "aerepuerto":""}
    cliente = open("Clientes.txt","r")
    lista_clientes = cliente.readlines()
    cliente.close()
    for clientes in lista_clientes:
        campos = clientes.rstrip("\n").split(",")
        todo = {"firstname":campos[0],"surname":campos[1], "lenguaje":campos[2], "nombre":campos[3], "aerepuerto":campos[4]}
        resp = requests.post(api_url,json=todo)
        print(resp)
sendData()
