# ------------- WAVE 1 --------------------

from lib2to3.pgen2.pgen import generate_grammar
from shutil import move
from turtle import title


def create_movie(title, genre, rating):
    # testing git
    movie_dict ={}

    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    else:
        return None

    return movie_dict

def add_to_watched(user_data, movie):
    watched_movie_dict = {
        "title": movie["title"],
        "genre": movie["genre"],
        "rating": movie["rating"]
    }

    user_data["watched"].append(watched_movie_dict)

    return user_data

def add_to_watchlist(user_data, movie):
    to_watch_movie_dict = {
        "title": movie["title"],
        "genre": movie["genre"],
        "rating": movie["rating"]
    }

    user_data["watchlist"].append(to_watch_movie_dict)

    return user_data

def watch_movie(user_data, title):
    # create a dictionary where key = title, value = index
    watchlist_titles_dict = {}

    # gather all of the watchlist titles
    for i in range(len(user_data["watchlist"])):
        watchlist_titles_dict[user_data["watchlist"][i]["title"]] = i

    if title in watchlist_titles_dict.keys():
        user_data["watchlist"].pop(watchlist_titles_dict[title])
        user_data["watched"].append(watchlist_titles_dict[title])

    return user_data






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

