import argparse
import pickle_methods as pm
from scrape_films import fetch_all_atributes

input_list = '../data/movie_list_6898'
output_file_name = '../data/movie_attributes_6898'

if __name__ == '__main__':
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', help="verbose mode", default=False)
    arguments = parser.parse_args()
    verbose = arguments.v
    # urls and path
    list_films = pm.load(input_list)
    list_films_as_dict = {}
    nbr_bugs = 0
    for i in list_films:
        list_films_as_dict[i] = True
    movie_attributes = {}
    nbr_movies = len(list_films)
    consecutive_bug = False
    nbr_bugs = 0
    fetch_all_atributes(list_films_as_dict, movie_attributes,
                        verbose, nbr_movies, consecutive_bug, nbr_bugs)
    pm.save(movie_attributes, output_file_name)
    print("successfully stored attributes of {} movies"
          " in {} with {} bugs ".format(
              nbr_movies, output_file_name, nbr_bugs))
