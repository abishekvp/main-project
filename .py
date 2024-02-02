from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://pro_user:rkwyrUiPnjjBsssg@cluster0.edxis.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.project_gpa
db_user = db.user

db_user.insert_one({"name":'Gayu',"time_series": datetime.datetime.utcnow()})

