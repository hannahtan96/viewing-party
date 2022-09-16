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
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

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

# create a helper function to return two lists: my_list_of_movies and my_friends_list_movies
def get_my_and_friends_watched_movie_titles(user_data):

    # create a list of my watched movie titles
    my_watched_movie_titles = []
    for k in range(len(user_data["watched"])):
        my_watched_movie_titles.append(user_data["watched"][k]["title"])

    # create a list of friend's watched movie titles
    friends_watched_movie_titles = []
    for i in range(len(user_data["friends"])):
        if "watched" in user_data["friends"][i].keys():
            for j in range(len(user_data["friends"][i]["watched"])):
                friends_watched_movie_titles.append(user_data["friends"][i]["watched"][j]["title"])

    # returns two sets in a list
    return [set(my_watched_movie_titles), set(friends_watched_movie_titles)]


def get_unique_watched(user_data):

    return_list = get_my_and_friends_watched_movie_titles(user_data)
    my_list_of_movies = return_list[0]
    friends_list_of_movies = return_list[1]

    if my_list_of_movies and friends_list_of_movies:
        my_unique_titles = my_list_of_movies - friends_list_of_movies
    else: return []

    my_unique_movies_list = []
    for title in my_unique_titles:
        
        for l in range(len(user_data["watched"])):
            if user_data["watched"][l]["title"] == title:
                genre = user_data["watched"][l]["genre"]
                rating = user_data["watched"][l]["rating"]
        my_unique_movies_list.append({"title": title, "genre": genre, "rating": rating})
    
    return my_unique_movies_list


def get_friends_unique_watched(user_data):

    return_list = get_my_and_friends_watched_movie_titles(user_data)
    my_list_of_movies = return_list[0]
    friends_list_of_movies = return_list[1]

    if my_list_of_movies and friends_list_of_movies:
        my_friends_unique_titles = friends_list_of_movies - my_list_of_movies
    else: return []

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
# def get_available_recs(user_data):


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
