import argparse
from scrape_films import list_films


def scrape_movie_ids(output_file, url, nb_page_max, verbose):
    list_films(list_movie_url, output_file, nb_page_max, verbose)


if __name__ == '__main__':
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', help="verbose mode", default=False)
    parser.add_argument('-n', help="movie-pages to scrape", default=1000000)
    arguments = parser.parse_args()
    verbose = arguments.v
    nbr = int(arguments.n)
    # urls and path
    list_movie_url = 'http://www.senscritique.com/films/oeuvres/page-'
    output_file_for_list = '../data/movie_list'
    scrape_movie_ids(output_file_for_list, list_movie_url, nbr, verbose)
