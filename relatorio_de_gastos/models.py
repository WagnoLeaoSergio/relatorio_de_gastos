import os
from mongoengine import *
from dotenv import load_dotenv

load_dotenv()

connect(
    "gastos_data",
    host=os.getenv("MONGO_DB_URI")
    )

class Gasto(Document):
    date = DateField(required=True)
    price = FloatField(required=True)
    category = StringField(
        required=True,
        choices=os.getenv("choices").split(",") #["almoco", "comida", "mercado", "remedio", "combustivel", "outros"]
    )

