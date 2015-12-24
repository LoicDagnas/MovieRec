import argparse
import pickle_methods as pm
from scrape_films import fetch_all_movie_ratings

input_list = '../data/movie_list'
output_file_name = '../data/movie_ratings_tryout'

if __name__ == '__main__':
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', help="verbose mode", default=False)
    arguments = parser.parse_args()
    verbose = arguments.v
    list_films = pm.load(input_list)
    list_films_as_dict = {}
    nbr_bugs = 0
    for i in list_films:
        list_films_as_dict[i] = True
    movie_ratings = {}
    nbr_movies = len(list_films)
    consecutive_bug = False
    nbr_bugs = 0
    fetch_all_movie_ratings(list_films_as_dict, movie_ratings,
                            verbose, nbr_movies, consecutive_bug, nbr_bugs)
    pm.save(movie_ratings, output_file_name)
    print("successfully stored ratings of {} movies"
          " in {} with {} bugs ".format(
              nbr_movies, output_file_name, nbr_bugs))
