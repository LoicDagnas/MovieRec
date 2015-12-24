#pragma once
#include <vector>
using namespace std;

class Rate {
    public:
        // Rater user name
        string username;
        // Rate 
        int rate;
        // Empty constructor 
        Rate();
        // Constructor 
        Rate(string user, int i_rate);
        // Destructor 
        ~Rate();
};


class Movie {
    public:
        // New id in {0, 1, 2, ...}
        int id;
        // Title
        string title;
        // Old id 
        int old_id;
        // Number of director
        int nb_directors;
        // List of directors
        vector<string> directors;
        // Formated duration
        string duration;
        // Formated release date
        string release_date;
        // Number of genre
        int nb_genre;
        // List of genre
        vector<string> genres;
        // Number of actors
        int nb_actors; 
        // List of actors
        vector<string> actors;
        // Average rating
        float average_rate;
        // Number of rating
        int nb_ratings;
        // List of rates
        vector<Rate> rates;
        // Constructor 
        Movie(int id, int old_id, string title, string duration, string release_date, 
              int nb_genre, vector<string> genres, int nb_directors, vector<string> directors, 
              int nb_actors, vector<string> actors, float average_rate, int nb_rate, vector<Rate> rates);
        // Destructor 
        ~Movie();
        // Printer
        friend ostream& operator<<(ostream& os, const Movie& dt);
};


class MovieList {
    public:
        // List of Movie object
        vector<Movie> list;
        // Constructor 
        MovieList();
        // Destructor 
        ~MovieList();
        // Add a movie in the list
        void add_movie(Movie m);
        // Get the number of movies
        int number();
};
