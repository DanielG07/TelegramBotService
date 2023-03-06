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
  return client['appTelegram'] #we already know the name of the database


dbname = get_database()
collectiondata = dbname['Mensajes'] #We already know the name of the table to extract the data
detalles = collectiondata.find()
#Dataframe to analize the info and clean it and update 
Dataframe = pd.DataFrame(list(detalles))
#Clean all dummy info without a message
Dataframe['mensaje'] = Dataframe['mensaje'].replace([None,''],0)
Dataframe = Dataframe[Dataframe['mensaje'] != 0]

print(Dataframe)

# API use
for i in range(len(Dataframe.index)):
  if(Dataframe.iloc[i,7] == False):
    mensaje = f'El profesor {str(Dataframe.iloc[i,2])} de la materia {str(Dataframe.iloc[i,4])} dice:\n{Dataframe.iloc[i,1]}'  
    URL = f'https://api.telegram.org/bot6076404908:AAFBHUDbp55T4qwH8chUOB3ZbyenBMRsBD4/sendMessage?chat_id=@BotUpiita&text={mensaje}'
    x = requests.post(URL)
    #TO-DO
    #Que el equipo 2 cree una api para solo hacer update al registro de False a True c;
    URLUpdateStatus = f'https://AppTelegram.repl.co/check'             
    params={'id': Dataframe.iloc[i,0]}             
    y = requests.post(URLUpdateStatus, params) 
  else:
    pass
  