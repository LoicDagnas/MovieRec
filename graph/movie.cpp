#include "movie.h"
#include <string>
#include <algorithm>


Rate::Rate(string user, int i_rate) {
    username = user;
    rate = i_rate;
}

Rate::Rate(){
}

Rate::~Rate(){
}

Movie::Movie(int i_id, int i_old_id, string i_title, string i_duration, string i_release_date, 
              int i_nb_genre, vector<string> i_genres, int i_nb_directors, vector<string> i_directors, 
              int i_nb_actors, vector<string> i_actors, float i_average_rate, int i_nb_rate, vector<Rate> i_rates) 
{
    id = i_id;
    old_id = i_old_id;
    title = i_title;
    duration = i_duration;
    release_date = i_release_date;
    nb_genre = i_nb_genre;
    genres = i_genres;
    nb_directors = i_nb_directors;
    directors = i_directors;
    nb_actors = i_nb_actors;
    actors = i_actors;
    average_rate = i_average_rate;
    nb_ratings = i_nb_rate;
    rates = i_rates;
}

ostream& operator<<(ostream& os, const Movie& m)
{
    string genres = "";
    for(int i=0; i<m.nb_genre; i++){
        genres = genres + ", " + m.genres[i];
    }

    string dir = "";
    for(int i=0; i<m.nb_directors; i++){
        dir = dir + ", " + m.directors[i];
    }

    string actors = "";
    for(int i=0; i<m.nb_actors; i++){
        actors = actors + ", " + m.actors[i];
    }

    string rates = "";
    for(int i=0; i<m.nb_ratings; i++){
        string r =  to_string(m.rates[i].rate);
        rates = rates + ", " + m.rates[i].username + " (" + r + ")";
    }

    os << " Id: " << m.id 
       << "\n Old id: "   << m.old_id
       << "\n Title : "   << m.title
       << "\n Duration: "   << m.duration 
       << "\n Release date: "   << m.release_date
       << "\n Genre: "   << genres
       << "\n Directors: "   << dir
       << "\n Actors: "   << actors
       << "\n Average rate: " << m.average_rate
       << "\n Rates: "   << rates
       << "\n";
    return os;
}

Movie::~Movie(){
}

MovieList::MovieList() {
}

MovieList::~MovieList(){
}

void MovieList::add_movie(Movie m){
    list.push_back(m);
}

int MovieList::number(){
    return list.size();
}
