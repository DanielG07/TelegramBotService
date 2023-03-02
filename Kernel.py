import pandas as pd
#libreria de python que conecta con MongoDB
from pymongo import MongoClient
import requests
# Libreria para manejo de variables de entorno
from dotenv import load_dotenv
import os

def get_database():
  # Credenciales
  load_dotenv()
  MONGOUSER =  os.environ["MONGOUSER"]
  MONGOPASS = os.environ["MONGOPASS"]
  # URI del equipo 2
  MONGODB_URI = f'mongodb+srv://{MONGOUSER}:{MONGOPASS}@cluster-sd.uhhmbgs.mongodb.net/?retryWrites=true&w=majority'

  # Connect to your MongoDB cluster:
  client = MongoClient(MONGODB_URI)
  return client['appTelegram']

# List all the databases in the cluster:
dbname = get_database()
collectiondata = dbname['Mensajes']
detalles = collectiondata.find()

Dataframe = pd.DataFrame(list(detalles))
# print(Dataframe)

# API
# api-endpoint

for i in range(len(Dataframe.index)):
  
  if(Dataframe.iloc[i,7] == False):
    mensaje = Dataframe.iloc[i,1]  
    URL = f'https://api.telegram.org/bot6076404908:AAFBHUDbp55T4qwH8chUOB3ZbyenBMRsBD4/sendMessage?chat_id=@BotUpiita&text={mensaje}'
    #params={'chat_id':'@BotUpiita','text':mensaje}
    x = requests.post(URL)
    #TO.DO
    #Que el equipo 2 cree una api para solo hacer update al registro de False a True c;
  else:
    pass
  