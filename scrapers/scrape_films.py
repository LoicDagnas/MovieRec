import datetime as dt
from time import strptime
import requests
import json
import pickle_methods as pm
import makesoup
import time


def list_films(url, output_file, nb_page_max, verbose):
    """
    Scrape the whole list of films on senscritique.com
    Return a list of film_id
    """
    films_list = []
    films_page = makesoup.make_soup(url + str(1))
    pager = films_page.find('ul', 'eipa-pages').find_all('a')
    last_page = int(pager[-1].contents[0].replace('.', ''))
    last_page = min(last_page, nb_page_max)
    nbr_movies = last_page * 15
    if verbose:
        print("scraping over {} pages of 15 movies each that is "
              "a total of about {} movies"
              " (modulus the last page)".format(last_page, nbr_movies))
    for page in range(1, last_page + 1):
        if verbose:
            print('Scraping films in page "{}"'.format(page))
        films_page = makesoup.make_soup(url + str(page))
        try:
            films = films_page.find_all('div', 'd-link')
            for f in films:
                films_list.append(str(f.get('data-sc-link')))
        except AttributeError:
            print("On page" + str(page) + ": films urls not found!")
    pm.save(films_list, output_file)
    print("successfully stored {} movies in {}".format(
        len(films_list), output_file))


def fetch_all_atributes(list_films_as_dict, movie_attributes,
                        verbose, nbr_movies, consecutive_bug, nbr_bugs):
    try:
        loop_over_movies_for_attributes(
            list_films_as_dict, movie_attributes,
            verbose, nbr_movies)
        consecutive_bug = False
    except Exception as e:
        print(e)
        time.sleep(10)
        if not consecutive_bug:
            nbr_bugs += 1
        consecutive_bug = True
        fetch_all_atributes(list_films_as_dict, movie_attributes,
                            verbose, nbr_movies, consecutive_bug, nbr_bugs)


def loop_over_movies_for_attributes(movie_dict_to_loop_over,
                                    movie_attributes_dict, verbose,
                                    nbr_movies):
    for idx, f in enumerate(movie_dict_to_loop_over):
        if movie_dict_to_loop_over[f]:
            if verbose:
                print('Scraping attributes for movie {},'
                      ' number {} out of {}'.format(f,
                                                    idx + 1, nbr_movies))
            movie_attributes_dict[f] = film_attributes(f, idx, verbose)
            movie_dict_to_loop_over[f] = False


def film_attributes(film_id, idx, verbose):
    """
    Scrape film attributes from a film page.
    Return a dictionary with the title, original title, director, release
    date, average rating and number of ratings.
    """
    if film_id in ('/new_film',):
        return {'title': 'Le Titre', 'director': 'M. Lumière',
                'release_date': dt.date(1891, 7, 5)}
    film_page = makesoup.make_soup("http://www.senscritique.com" + film_id)
    # title
    try:
        title = film_page.find('h1', 'pvi-product-title').get('title')
    except AttributeError:
        if verbose:
            print(film_id + ": title not found!")
        title = ''
    # original title
    try:
        original_title = str(film_page.find(
            'h1', {'itemprop': 'alternativeHeadline',
                   'class': 'pvi-product-originaltitle'}).string)
    except AttributeError:
        original_title = ''
    # actors
    actors = []
    try:
        actors_c = film_page.find_all('span', 'd-offset ecot-contact-label')
        for actor in actors_c:
            try:
                actors.append(str(actor.contents[0]))
            except IndexError:
                if verbose:
                    print('actor not in the right space')
    except AttributeError:
        if verbose:
            print(film_id + ": actors not found!")
        actors = ''
    # directors
    director_spans = film_page.find_all('span', {'itemprop': 'director'})
    if director_spans:
        director_list = [director.a.get('href')
                         for director in director_spans]
        directors = ', '.join([director.a.span.string
                               for director in director_spans])
    else:
        if verbose:
            print(film_id + ": director not found!")
        director_list = []
        directors = ''
    # duration
    try:
        formatted_duration = [
            d for d in film_page.find_all('li', 'pvi-productDetails-item')
            if d.find('meta', {'itemprop': 'duration'})][0].text.strip()
        try:
            duration = strptime(formatted_duration, '%H h %M min')
        except ValueError:
            try:
                duration = strptime(formatted_duration, '%M min')
            except ValueError:
                duration = strptime(formatted_duration, '%H h')
        duration = 60 * duration.tm_hour + duration.tm_min
    except (AttributeError, IndexError):
        duration = None
    # release date
    try:
        li_release_date = film_page.find(
            'li', 'pvi-productDetails-item nowrap')
        release_date = dt.date(*[
            int(i) for i in li_release_date.time.get('datetime').split('-')])
    except AttributeError:
        try:
            string_release_year = film_page.find(
                'small', 'pvi-product-year').string.strip('()')
            release_date = dt.date(int(string_release_year), 1, 1)
        except AttributeError:
            if verbose:
                print(film_id + ": release year not found!")
            release_date = None
    # rating
    try:
        rating_string = film_page.find(
            'div', 'pvi-product-scrating').find(
            'span', {'itemprop': 'ratingValue'}).string
        rating = float(rating_string)
    except AttributeError:
        rating = None
    # genre
    genre_list = []
    genre_c = film_page.find_all(itemprop="genre")
    for g in genre_c:
        genre_list.append(str(g.contents[0]))
    if not genre_list:
        genre_list = []
    try:
        film_main_type = film_page.find(
            'li', 'pvi-productDetails-item').h2.text
        genre_list.append(film_main_type)
    except AttributeError:
        pass
    # number of ratings
    try:
        number_of_ratings_string = film_page.find(
            'span', {'itemprop': 'ratingCount'}).string
        number_of_ratings = int(number_of_ratings_string)
    except AttributeError:
        number_of_ratings = 0
    return {'title': title, 'original_title': original_title,
            'director': directors, 'director_list': director_list,
            'duration': duration,
            'actors': actors,
            'genre': genre_list,
            'release_date': release_date,
            'sc_average_rating': rating,
            'sc_number_of_ratings': number_of_ratings,
            }


def film_extended_storyline(film_id):
    short_id = film_id.strip('/').split('/')[-1]
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    text = requests.get(
        'http://www.senscritique.com/sc/products/storyline/' +
        short_id + '.json', headers=headers).text
    storyline = json.loads(text)['json']['data'].replace('\r\n', ' ')
    return storyline


def movie_test(input_file):
    movies = pm.load(input_file)
    print(movies)


def rating_test(input_file):
    rating = pm.load(input_file)
    i = 0
    for movie in rating:
        if rating[movie] != {}:
            i += 1
            print(movie)
    print(i)


def movie_list_from_ratings(input_rating_file, output_file):
    rating = pm.load(input_rating_file)
    list_to_output = []
    for movie in rating:
        if rating[movie] != {}:
            list_to_output.append(movie)
    print(list_to_output)
    pm.save(list_to_output, output_file)


def fetch_all_movie_ratings(list_films_as_dict, movie_ratings,
                            verbose, nbr_movies, consecutive_bug, nbr_bugs):
    try:
        loop_over_movies_for_ratings(
            list_films_as_dict, movie_ratings,
            verbose, nbr_movies)
        consecutive_bug = False
    except Exception as e:
        print('no internet connexion found or just kicked the'
              ' fuck out from the admin, gonna try again in 10 seconds')
        time.sleep(10)
        print(e)
        if not consecutive_bug:
            nbr_bugs += 1
        consecutive_bug = True
        fetch_all_atributes(list_films_as_dict, movie_ratings,
                            verbose, nbr_movies, consecutive_bug, nbr_bugs)


def loop_over_movies_for_ratings(movie_dict_to_loop_over,
                                 movie_ratings_dict, verbose,
                                 nbr_movies):
    for idx, f in enumerate(movie_dict_to_loop_over):
        if movie_dict_to_loop_over[f]:
            if verbose:
                print('Scraping ratings for movie {},'
                      ' number {} out of {}'.format(f,
                                                    idx + 1, nbr_movies))
            movie_ratings_dict[f] = movie_ratings(f)
            movie_dict_to_loop_over[f] = False


def all_movies_ratings(input_file, output_file):
    """
    Scrape the ratings of users for all movies
    return a dictionnary of ratings per films
    """
    list_films = pm.load(input_file)
    list_films_ratings = {}
    for f in list_films:
        ratings_dico = movie_ratings(f)
        list_films_ratings[f] = ratings_dico
        print(list_films_ratings)
    pm.save(list_films_ratings, output_file)


def movie_ratings(movie_url):
    """
    scrape the ratings of users on the movie_url
    returns a dictionnary user name to rating
    """
    movie_id = movie_url.split('/')[-1]
    #  Get the number of crewiew pages
    ratings = {}
    base_url = 'http://www.senscritique.com/sc/' + \
        movie_id + "/critiques/all/page-1.ajax"
    film_ratings = makesoup.make_soup(base_url)
    try:
        pager = film_ratings.find('ul', 'eipa-pages').find_all('a')
        last_page = pager[-1].contents[0].replace('.', '')
        # For all pages get the associated rates
        for page in range(1, int(last_page) + 1):
            generic_url = 'http://www.senscritique.com/sc/' + movie_id + \
                "/critiques/all/page-" + str(page) + ".ajax"
            film_ratings = makesoup.make_soup(generic_url)
            articles = film_ratings.find_all('article', 'ere-review')
            for art in articles:
                rating = str(art.find(
                    'span', 'elrua-useraction-inner').contents[0].strip())
                user = str(art.find('span', 'd-offset').contents[0].strip())
                ratings[user] = rating
        print(ratings)
    except AttributeError:
        print("There is no review for the movie {}".format(movie_id))
    return ratings
