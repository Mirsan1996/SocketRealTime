import mysql.connector
import paho.mqtt.client as mqttClient
from integers.credenciales import usermysql, usermqtt

mydb = mysql.connector.connect(
  host=usermysql[0],
  user=usermysql[1],
  password=usermysql[2],
  database=usermysql[3]
)

def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print('Connected to broker_4')
    global Connected
    Connected = True
  else:
    print('Connection failed')


def on_message(client, userdata, message):
    mydb.cursor().execute(
    "CREATE TABLE IF NOT EXISTS database_numero4(id INT PRIMARY KEY AUTO_INCREMENT, numero INT, fecha datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);")
    mydb.cursor().execute('INSERT INTO database_numero4 (numero) VALUE (%(message.payload)s)', {'message.payload':message.payload})
    mydb.commit()


Connected = False
broker_address = usermqtt
port = 1883  
user = 'chavito_'+str(4)  
password = '643092' 
client = mqttClient.Client('Python_'+str(4)) 
client.username_pw_set(user, password=password)  
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(broker_address, port, 60)  
client.subscribe('boton0')
client.loop_forever()  
