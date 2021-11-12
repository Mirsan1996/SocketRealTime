import mysql.connector
import paho.mqtt.client as mqttClient
mydb = mysql.connector.connect(
  host='172.20.108.32',
  user='Miranda',
  password='SqlAdmin',
  database='iot2040'
)
def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print('Connected to broker_11')
    global Connected
    Connected = True
  else:
    print('Connection failed')
def on_message(client, userdata, message):
    mydb.cursor().execute('INSERT INTO database_texto (texto) VALUE (%(message.payload)s)', {'message.payload':message.payload})
    mydb.commit()
Connected = False
broker_address = '172.20.108.32'
port = 1883  
user = 'chavito_'+str(11)  
password = '643092' 
client = mqttClient.Client('Python_'+str(11)) 
client.username_pw_set(user, password=password)  
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(broker_address, port, 60)  
client.subscribe('sensor') 
client.loop_forever()  
