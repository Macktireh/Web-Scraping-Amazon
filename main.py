import os
import smtplib
import ssl

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


from amazon_bot import AmazonBot

# Chargement des variables d'environnement se trouvant dans le fichier .env
load_dotenv()

# Connexion à la base de donnée MongoDB
# try:
#     client = MongoClient("mongodb://localhost:27017/")
#     client.server_info()
# except Exception as e:
#     raise e

uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Connexion au serveur pour l'envoi d'email
try:
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(os.getenv("SENDER_EMAIL"), os.getenv("EMAIL_PASSWORD"))
except Exception as e:
    raise e

# Initialisation de la classe AmazonBot
bot = AmazonBot(mongodb_client=client, server_smtp=None)
# Lancement du Scraping
bot.scrap_urls()

# Liste des produits Amazon

# product_urls = [
#    "https://www.amazon.fr/Apple-AirPods-bo%C3%AEtier-charge-Dernier/dp/B07PZR3PVB/ref=sr_1_5?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=airpod&qid=1610634324&sr=8-5",
#    "https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=OC9DXXI5NXTR&dchild=1&keywords=playstation+5&qid=1610634362&sprefix=playstatio%2Caps%2C204&sr=8-1",
#    "https://www.amazon.fr/Nintendo-Switch-avec-paire-Rouge/dp/B07WKNQ8JT/ref=zg_bs_videogames_home_1?_encoding=UTF8&psc=1&refRID=NXGE6WDBSEDAVF5CS2AA",
#    "https://www.amazon.fr/T12S-Transformation-semaines-minutes-d%C3%A9finitivement/dp/2035999642/ref=zg_bsnr_books_home_1?_encoding=UTF8&psc=1&refRID=71P5R2S30WR2EPDRPAP7",
#    "https://www.amazon.fr/chronique-Bridgerton-Tomes-Julia-Quinn/dp/2290254738/ref=zg_bsnr_books_home_3?_encoding=UTF8&psc=1&refRID=71P5R2S30WR2EPDRPAP7",
#    "https://www.amazon.fr/Incorra-Pieuvre-Reversible-Peluche-Cr%C3%A9atifs/dp/B08NW2RRXJ/ref=zg_bsnr_toys_home_3?_encoding=UTF8&psc=1&refRID=71P5R2S30WR2EPDRPAP7"
# ]
