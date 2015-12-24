#pragma once
#include <vector>
using namespace std;

class Human {
    public:
        // The pair (id,category) should be unique 
        int id;
        string category;
        // The complete name or username for user
        string name;
        // Constructors
        Human(int id, string cat, string name);
        Human();
        // Destructor
        ~Human();
        // Comparison operator useful for find in lists (compare only the names)
        bool operator==(const Human& other) const;
        // Printer
        friend ostream& operator<<(ostream& os, const Human& dt);
};


class DirectorList {
    public:
        // A list of human with category: 'director'
        vector<Human> list;
        // Constructor
        DirectorList();
        // Destructor
        ~DirectorList();
        // Add a director to the list
        bool add_director(Human human);
        // Return the number of unique Directors
        int number();
};


class ActorList {
    public:
        // A list of humans with category: 'actor'
        vector<Human> list;
        // Constructor
        ActorList();
        // Destructor
        ~ActorList();
        // Add an actor to the list
        bool add_actor(Human human);
        // Return the number of unique Actors
        int number();
};


class UserList {
    public:
        // A list of humans with category: 'user'
        vector<Human> list;
        // Constructor
        UserList();
        // Destructor
        ~UserList();
        // Add a user to the list
        bool add_user(Human human);
        // Return the number of unique Users
        int number();
};
