from mongoengine import *
from connect import connect

connect()

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()


class Contact(Document):
    fullname = StringField()
    email = EmailField()
    phone = StringField()
    preferred = StringField(choices=["email", "sms"])
    sent = BooleanField(default=False)
