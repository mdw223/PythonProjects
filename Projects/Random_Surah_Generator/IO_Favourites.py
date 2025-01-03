import json

from Surah import Surah

favourite_surahs = [] # list of favourite surahs

save_path = "Projects/Random_Surah_Generator/favourites.txt"

def load_favourites():
    global favourite_surahs
    try:
        with open(save_path, "r") as f:
            data = json.load(f)
            favourite_surahs = [Surah.from_dict(value) for value in data]
    except:
        favourite_surahs = []  # No file, start with an empty list

def save_favourites():
    with open(save_path, "w") as f:
        json.dump( [surah.to_dict() for surah in favourite_surahs], f)
        

def get_favourite_surahs():
    return favourite_surahs