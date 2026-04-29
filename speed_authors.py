import json
from models import Author

with open("authors.json", encoding="utf-8") as f:
    authors = json.load(f)

for a in authors:
    Author(
        fullname=a["fullname"],
        born_date=a["born_date"],
        born_location=a["born_location"],
        description=a["description"]
    ).save()
