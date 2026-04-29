mport redis
from models import Quote
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def find_by_name(name):
    key = f"name:{name}"

    if r.exists(key):
        return json.loads(r.get(key))

    result = [q.quote for q in Quote.objects(author__fullname__icontains=name)]

    r.set(key, json.dumps(result))
    return result


def find_by_tag(tag):
    key = f"tag:{tag}"

    if r.exists(key):
        return json.loads(r.get(key))

    result = [q.quote for q in Quote.objects(tags__icontains=tag)]

    r.set(key, json.dumps(result))
    return result


def find_by_tags(tags):
    tags = tags.split(",")
    return [q.quote for q in Quote.objects(tags__in=tags)]


def main():
    while True:
        cmd = input(">>> ")

        if cmd == "exit":
            break

        if cmd.startswith("name:"):
            print(find_by_name(cmd.split(":")[1]))

        elif cmd.startswith("tag:"):
            print(find_by_tag(cmd.split(":")[1]))

        elif cmd.startswith("tags:"):
            print(find_by_tags(cmd.split(":")[1]))


if name == "__main__":
    main()
