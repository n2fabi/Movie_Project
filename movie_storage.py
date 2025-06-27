import json

def get_movies():
    with open("data.json","r") as fileobj:
        data = json.loads(fileobj.read())
    return data


def save_movies(movies):
    json_str = json.dumps(movies)
    with open("data.json", "w") as fileobj:
        fileobj.write(json_str)


def add_movie(title, year, rating):
    with open("data.json", "r") as fileobj:
        data = json.loads(fileobj.read())

    data[title] = {"Title": title, "Rating": rating, "Year": year}

    with open("data.json", "w") as fileobj:
        json.dump(data, fileobj, indent=2)


def delete_movie(title):
    with open("data.json", "r") as fileobj:
        data = json.loads(fileobj.read())

    del data[title]

    with open("data.json", "w") as fileobj:
        json.dump(data, fileobj, indent=2)


def update_movie(title, rating):
    with open("data.json", "r+") as fileobj:
        data = json.loads(fileobj.read())
    data[title]["Rating"] = rating

    with open("data.json", "w") as fileobj:
        json.dump(data, fileobj, indent=2)