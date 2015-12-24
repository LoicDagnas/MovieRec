import pickle_methods as pm
import csv


def from_pickle_to_csv():
    """
    Simple function taking a movie_list, a movie_ratings and
    a movie_attributes pickled object (see their structure)
    and returns a csv file with the following columns :
    ID (indexed from 0 to nbr_of_movies)
    ID_SC (sens critique id)
    title (sens critique with underscores)
    duration
    release_date
    number_of_genre
    genres
    number_of_directors
    director (sens critique format /contact/name/id)
    number_of_actors
    actors (real name with underscores)
    average_rating
    number_of_ratings
    user
    rating
    """
    movie_id_dict = {}
    with open('../data/movie_list', 'w') as movie_list_as_csv:
        movie_list = pm.load('../data/movie_list_6898')
        writer = csv.writer(movie_list_as_csv, delimiter=" ")
        i = 0
        # getting IDs
        for movie in movie_list:
            movie_id_dict[movie] = [i, movie.split("/")[3],
                                    movie.split("/")[2]]
            i += 1
        # getting ratings
        dict_ratings = {}
        rating_list = pm.load('../data/movie_ratings_6898')
        for movie in rating_list:
            if movie in movie_id_dict:
                dict_ratings[movie] = [len(rating_list[movie])] if rating_list[movie] else [0]
                compt = 0
                for user in rating_list[movie]:
                    
                    if str(rating_list[movie][user]).isdigit():
                        compt += 1
                        dict_ratings[movie].append(str(user).replace(" ", "_"))
                        dict_ratings[movie].append(rating_list[movie][user])
                dict_ratings[movie][0] = compt
        # getting attributes
        movie_attributes = pm.load('../data/movie_attributes_6898')
        for movie in movie_attributes:
            duration = movie_attributes[movie][
                'duration'] if movie_attributes[movie]['duration'] else 0
            movie_id_dict[movie].append(duration)
            release_date = str(
                movie_attributes[movie]['release_date']).replace(
                " ", "") if movie_attributes[movie]['release_date'] else 0
            movie_id_dict[movie].append(release_date)
            num_of_genre = len(movie_attributes[movie]['genre']) if movie_attributes[movie]['genre'] else 0
            movie_id_dict[movie].append(num_of_genre)
            for genre in movie_attributes[movie]['genre']:
                movie_id_dict[movie].append(genre.replace(" ", "_"))
            num_of_directors = len(movie_attributes[movie]['director_list']) if movie_attributes[movie]['director_list'] else 0
            movie_id_dict[movie].append(num_of_directors)
            for director in movie_attributes[movie]['director_list']:
                movie_id_dict[movie].append(director.replace(" ", "_").split('/')[2])
            num_of_actors = len(movie_attributes[movie]['actors']) if movie_attributes[movie]['actors'] else 0
            movie_id_dict[movie].append(num_of_actors)
            for actor in movie_attributes[movie]['actors']:
                movie_id_dict[movie].append(actor.replace(" ", "_"))
            average_rating = movie_attributes[movie]['sc_average_rating'] if movie_attributes[movie]['sc_average_rating']  else 0
            movie_id_dict[movie].append(average_rating)
            movie_id_dict[movie].extend(dict_ratings[movie])
            writer.writerow(movie_id_dict[movie])


if __name__ == '__main__':
    from_pickle_to_csv()
