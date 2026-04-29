from mongoengine import connect

connect(
    db="quotes_db",
    host="mongodb+srv://<user>:<password>@cluster.mongodb.net/quotes_db"
)
