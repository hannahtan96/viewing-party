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
        for movie in user_data["watched"]:
            sum_of_ratings += movie["rating"]
    else: return 0

    average_of_ratings = sum_of_ratings / len(user_data["watched"])
    return average_of_ratings


def get_most_watched_genre(user_data):
    genre_dict = {}
    if user_data["watched"]:
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] += 1
            else: genre_dict[movie["genre"]] = 1
    else: return None

    most_watched_genre = max(genre_dict.values())
    for key, value in genre_dict.items():
        if value == most_watched_genre:
            return key

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# create a helper function to return two lists: my_list_of_movies and my_friends_list_movies
def get_my_and_friends_movies(user_data):

    # create a list of my watched movies
    my_watched_movies = []
    for movie in user_data["watched"]:
        my_watched_movies.append(movie)

    # create a list of friend's watched movies
    friends_watched_movies = []
    for elem in user_data["friends"]:
        if "watched" in elem:
            for movie in elem["watched"]:
                # remove potential duplicates among movies watched by friends
                if movie not in friends_watched_movies:
                    friends_watched_movies.append(movie)

    # returns two elements: my_watched_movies and friends_watched_movies
    return my_watched_movies, friends_watched_movies

# create a helper function to return a list of all movies in the first list that is not in the second list
def find_unique_movies(first_list, second_list):
    
    return_list = []
    if first_list:
        for movie in first_list:
            if movie not in second_list:
                return_list.append(movie)

    return return_list


def get_unique_watched(user_data):

    my_list_of_movies, friends_list_of_movies = get_my_and_friends_movies(user_data)
    my_unique_movies = find_unique_movies(my_list_of_movies, friends_list_of_movies)
    
    return my_unique_movies

def get_friends_unique_watched(user_data):

    my_list_of_movies, friends_list_of_movies = get_my_and_friends_movies(user_data)
    friends_unique_movies = find_unique_movies(friends_list_of_movies, my_list_of_movies)

    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    # retrieve list of movies that the user has not seen, but at least one friend has seen
    friends_unique_list = get_friends_unique_watched(user_data)

    available_recs = []
    for movie in friends_unique_list:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)

    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    # retrieve list of movies that the user has not seen, but at least one friend has seen
    friends_unique_list = get_friends_unique_watched(user_data)
    # retrieve genre with highest frequency
    most_popular_genre = get_most_watched_genre(user_data)

    available_recs_by_genre = []
    for movie in friends_unique_list:
        if movie["genre"] == most_popular_genre:
            available_recs_by_genre.append(movie)

    return available_recs_by_genre

def get_rec_from_favorites(user_data):

    # retrieve list of movies that the user has seen, but no friend have seen
    my_unique_list = get_unique_watched(user_data)

    available_recs_from_favs = []
    for movie in my_unique_list:
        if movie in user_data["favorites"]:
            available_recs_from_favs.append(movie)

    return available_recs_from_favs

