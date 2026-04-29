import json
from models import Quote, Author

with open("quotes.json", encoding="utf-8") as f:
    quotes = json.load(f)

for q in quotes:
    author = Author.objects(fullname=q["author"]).first()

    Quote(
        tags=q["tags"],
        author=author,
        quote=q["quote"]
    ).save()
