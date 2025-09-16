import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7994547564:AAG3NBz20H2N30J5E-oH3K0rgDnbnTkpM4A")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "17640565"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ff67816c19a48aff1f86204ff61ce786")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7959404410"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://windows11joiya_db_user:Dd4968l3TDA1TJHx@cluster0.g15vx1l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
