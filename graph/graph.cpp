#include <iostream>
#include <utility>                   
#include <algorithm>
#include <string>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/graph_traits.hpp>
#include "../graph/movie.h"
#include "../graph/human.h"

using namespace boost;
using namespace std;

// Structure of nodes: movies, directors or actors
struct VertexProperties {
    // Global id 
    unsigned id;
    // Local id of the node, the couple (id, type) should be unique 
    int local_id;
    // type value should be in ['movie', 'director', 'actor']
    string type; 
    // Basic constructor for VertexProperties
    VertexProperties() : type(""), id(0), local_id(-1) {}
    VertexProperties(string const& t, unsigned i, int j) : type(t), id(i), local_id(j) {}
};

struct EdgeProperties { 
    float weight;
    float distance;
    EdgeProperties() : weight(0.0), distance(0.0) {}
    EdgeProperties(float w, float d) : weight(w), distance(d) {}
};


// create a types for the graph, vertex and edge type
typedef adjacency_list< vecS, vecS, bidirectionalS, VertexProperties, EdgeProperties > Graph;
typedef boost::graph_traits<Graph>::vertex_descriptor vertex_t;
typedef boost::graph_traits<Graph>::edge_descriptor edge_t;


// Add all note with the well-defined ids 
void add_nodes(MovieList& movie_list, DirectorList& director_list, ActorList& actor_list, Graph& g) {
    int node_counter = 0;

    for(vector<Movie>::iterator it = movie_list.list.begin(); it != movie_list.list.end(); ++it) {
        vertex_t v2 = boost::add_vertex(VertexProperties("movie", node_counter, it->id), g);
        node_counter++;
    }

    for(vector<Human>::iterator it = director_list.list.begin(); it != director_list.list.end(); ++it) {
        vertex_t v2 = boost::add_vertex(VertexProperties("director", node_counter, it->id), g);
        node_counter++;
    }

    for(vector<Human>::iterator it = actor_list.list.begin(); it != actor_list.list.end(); ++it) {
        vertex_t v2 = boost::add_vertex(VertexProperties("actor", node_counter, it->id), g);
        node_counter++;
    }
}
