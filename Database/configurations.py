from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import  certifi
 
uri  =  "mongodb+srv://bhagyalakshmip:7a9A2LchDXAitqGN@cluster0.kk5um5b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #mongoDB URI here
client  =  MongoClient(uri, tlsCAFile=certifi.where())
 
db  =  client.todo_db
collection  =  db["todo_data"]