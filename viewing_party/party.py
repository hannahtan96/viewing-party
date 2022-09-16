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
def get_watched_avg_rating(user_data):
    sum_of_ratings = 0
    if user_data["watched"]:
        for i in range(len(user_data["watched"])):
            sum_of_ratings += user_data["watched"][i]["rating"]
    else: return 0

    average_of_ratings = sum_of_ratings / len(user_data["watched"])
    return average_of_ratings


def get_most_watched_genre(user_data):
    genre_dict = {}
    if user_data["watched"]:
        for i in range(len(user_data["watched"])):
            if user_data["watched"][i]["genre"] in genre_dict.keys():
                genre_dict[user_data["watched"][i]["genre"]] += 1
            else: genre_dict[user_data["watched"][i]["genre"]] = 1
    else: return None

    most_watched_genre = max(genre_dict.values())
    for key, value in genre_dict.items():
        if value == most_watched_genre:
            return key

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):

    # creating a list of friend's watched movie titles
    friends_watched_movie_titles = []
    for i in range(len(user_data["friends"])):
        if "watched" in user_data["friends"][i].keys():
            for j in range(len(user_data["friends"][i]["watched"])):
                friends_watched_movie_titles.append(user_data["friends"][i]["watched"][j]["title"])

    # creating a list of my watched movie titles
    my_watched_movie_titles = []
    for k in range(len(user_data["watched"])):
        my_watched_movie_titles.append(user_data["watched"][k]["title"])
    
    if my_watched_movie_titles and friends_watched_movie_titles:
        # create two sets of dictionaries of my and my friend's watched movies
        my_list_of_movies = set(my_watched_movie_titles)
        my_friends_list_of_movies = set(friends_watched_movie_titles)
    else:
        return []

    my_unique_titles = my_list_of_movies - my_friends_list_of_movies

    my_unique_movies_list = []
    for title in my_unique_titles:
        
        for l in range(len(user_data["watched"])):
            if user_data["watched"][l]["title"] == title:
                genre = user_data["watched"][l]["genre"]
                rating = user_data["watched"][l]["rating"]
        my_unique_movies_list.append({"title": title, "genre": genre, "rating": rating})
    
    return my_unique_movies_list


def get_friends_unique_watched(user_data):

    # creating a list of friend's watched movie titles
    friends_watched_movie_titles = []
    for i in range(len(user_data["friends"])):
        if "watched" in user_data["friends"][i].keys():
            for j in range(len(user_data["friends"][i]["watched"])):
                friends_watched_movie_titles.append(user_data["friends"][i]["watched"][j]["title"])

    # creating a list of my watched movie titles
    my_watched_movie_titles = []
    for k in range(len(user_data["watched"])):
        my_watched_movie_titles.append(user_data["watched"][k]["title"])
    
    if my_watched_movie_titles and friends_watched_movie_titles:
        # create two sets of dictionaries of my and my friend's watched movies
        my_list_of_movies = set(my_watched_movie_titles)
        my_friends_list_of_movies = set(friends_watched_movie_titles)
    else:
        return []

    my_friends_unique_titles = my_friends_list_of_movies - my_list_of_movies

    my_friends_unique_movies_list = []
    for title in my_friends_unique_titles:
        for m in range(len(user_data["friends"])):
            if "watched" in user_data["friends"][m].keys():
                for n in range(len(user_data["friends"][m]["watched"])):
                    if user_data["friends"][m]["watched"][n]["title"] == title:
                        genre = user_data["friends"][m]["watched"][n]["genre"]
                        rating = user_data["friends"][m]["watched"][n]["rating"]
        my_friends_unique_movies_list.append({"title": title, "genre": genre, "rating": rating})
    
    return my_friends_unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

