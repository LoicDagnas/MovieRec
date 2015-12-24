#include "../converter/converters.cpp"
#include <iostream>                  
#include <utility>                   
#include <algorithm>                 
#include <boost/graph/graph_traits.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>

using namespace boost;

int main(int,char*[]) {
	
    MovieList movie_list;
    DirectorList director_list;
    ActorList actor_list;
    UserList user_list;
    get_movies_and_atributes_from_file("../data/movie_list", movie_list, director_list, actor_list, user_list);	

    cout << "There are " << director_list.number() << " directors in the database, e.g.:"<< endl;
    cout << director_list.list[0] << endl;
    cout << "There are " << actor_list.number() << " actors in the database, e.g.:"<< endl;
    cout << actor_list.list[0] << endl;
    cout << "There are " << user_list.number() << " users in the database, e.g.:"<< endl;
    cout << user_list.list[0] << endl;
    cout << "There are " << movie_list.number() << " movies in the database, e.g.:"<< endl;
    cout << movie_list.list[0] << endl;

    // create a typedef for the Graph type
    // typedef adjacency_list<vecS, vecS, bidirectionalS> Graph;

    // // Make convenient labels for the vertices
    // enum { A, B, C, D, E, N };
    // const int num_vertices = N;
    // const char* name = "ABCDE";

    // // writing out the edges in the graph
    // typedef std::pair<int, int> Edge;
    // Edge edge_array[] = 
    // { Edge(A,B), Edge(A,D), Edge(C,A), Edge(D,C),
    //   Edge(C,E), Edge(B,D), Edge(D,E) };
    // const int num_edges = sizeof(edge_array)/sizeof(edge_array[0]);

    // // declare a graph object
    // Graph g(num_vertices);

    // // add the edges to the graph object
    // for (int i = 0; i < num_edges; ++i)
    //   add_edge(edge_array[i].first, edge_array[i].second, g);

return 0;
}
