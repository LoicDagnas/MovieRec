#include <iostream>                  
#include <utility>                   
#include <algorithm>                 
#include "graph.cpp"
#include <boost/graph/graph_traits.hpp>
#include "../converter/converters.cpp"
#include "../graph/movie.cpp"
#include "../graph/human.cpp"

int main(int,char*[]) {
	
    // Get the list of Movies, Directors and Actors
    MovieList movie_list;
    DirectorList director_list;
    ActorList actor_list;
    UserList user_list;
    get_movies_and_atributes_from_file("../data/movie_list", movie_list, director_list, actor_list, user_list);	

    Graph g;

    add_nodes(movie_list, director_list, actor_list, g);

return 0;
}
