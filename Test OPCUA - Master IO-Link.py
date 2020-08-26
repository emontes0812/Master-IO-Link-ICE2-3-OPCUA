# El siguiente programa crea un cliente OPC UA para visualizar la valirable 
# "PDI Data Unsigned32" del puerto 5 de un Maestro IO-Link ICE2-8IOL-K45S-RJ45
#No olvidar instalar paquete ---  pip install opcua

from opcua import Client
import time

#Crea un cliente OPC y se realiza la conexion al Maestro IO-Link ICE2
url = "opc.tcp://192.168.1.34:4840"
 
client = Client(url)

client.connect()

#Imprime texto cuando esta conectado el Cliente al servidor OPC
print("Client Connected")

#Imprime una variable cada 1s
while True:
    Temp = client.get_node("ns=1;s=IOLM/Port 5/Attached Device/PDI Data Unsigned32")
    Measure = Temp.get_value()
    print(Measure)

    time.sleep(1)
