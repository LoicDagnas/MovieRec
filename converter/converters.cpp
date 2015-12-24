#include <iostream>
#include <fstream>
#include "../graph/movie.cpp"
#include "../graph/human.cpp"

using namespace std;

void get_movies_and_atributes_from_file(string inputFile, MovieList& movie_list, DirectorList& director_list,
                                        ActorList& actor_list, UserList& user_list)
{
    // Try to open the file an catch an exception if doesn't exist
    try {
        std::ifstream in(inputFile.c_str());  
    
        // The file input file is opened
        cout<<inputFile<<" Open \n\n";

        // Attribute to get
        int id, old_id, nb_genre, nb_directors, nb_actors, nb_rate, rate;
        float average_rate;
        string title, genre, release_date, duration, actor, director, rater;
        int count_directors=0;
        int count_actors = 0;
        int count_users = 0;

        while (!in.eof()) { 

            if(!in.good()) {
                break;
            }

            // Get the new id
            in >> id;
            // Get the old_id
            in >> old_id;

            // Get the title
            in>> title;

            // Get the duration
            in>> duration;

            // Get the release date
            in>> release_date;

            // Get the number of genre
            in>> nb_genre;

            // Get the number of genre
            vector<string> genres(0);
            for(int i=0; i<nb_genre; i++){
                in >> genre;
                genres.push_back(genre);
            }

            // Get the number of directors
            in >> nb_directors;

            // Get the list of directors and add them to the list (unique)
            vector<string> directors(0);
            for(int i=0; i<nb_directors; i++){
                in >> director;
                directors.push_back(director);
                if(director_list.add_director(Human(count_directors, "director", director))){
                    count_directors++;
                }
            }

            // Get the number of actors
            in >> nb_actors;

            // Get the list of actors and add them to the list
            vector<string> actors(0);
            for(int i=0; i<nb_actors; i++){
                in >> actor;
                actors.push_back(actor);
                if(actor_list.add_actor(Human(count_actors, "actor", actor))){
                    count_actors++;
                }
            }

            // Get the average rate
            in >> average_rate;

            // Get the number of rate
            in >> nb_rate;

            // Get the list of rate and list of user
            vector<Rate> rates(0);
            for(int i=0; i<nb_rate; i++){
                in >> rater;
                in >> rate;
                Rate the_rate(rater, rate);
                rates.push_back(the_rate);
                if(user_list.add_user(Human(count_users, "user", rater))){
                    count_users++;
                }
            }        


            // Final Movie object to add to the list
            Movie the_movie(id, old_id, title, duration, release_date, nb_genre, genres, nb_directors, directors, nb_actors, 
                            actors, average_rate, nb_rate, rates);
            
            movie_list.add_movie(the_movie);

        }
        in.close();
    }
    catch (const std::exception& e) {
        std::cout << "Opening file '" << inputFile << "' failed.";
    }

}