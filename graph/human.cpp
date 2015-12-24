#include "human.h"
#include <string>
#include <algorithm>

Human::Human(int i_id, string cat, string i_name){
    id = i_id;
    category = cat;
    name = i_name;
}

Human::Human(){
    }

Human::~Human(){}

bool Human::operator==(const Human& other) const
{
    return (name == other.name);
}

ostream& operator<<(ostream& os, const Human& h)
{
    os << " Id: " << h.id 
       << "\n Category: "   << h.category
       << "\n Name : "   << h.name
       << "\n";
    return os;
}

DirectorList::DirectorList(){
}

DirectorList::~DirectorList(){
}

bool DirectorList::add_director(Human human){
    if (human.category=="director" && std::find(list.begin(), list.end(), human) == list.end()) {
        list.push_back(human);
        return true;
    }
    return false;
}

int DirectorList::number(){
    return list.size();
}

ActorList::ActorList(){
}

ActorList::~ActorList(){
}

int ActorList::number(){
    return list.size();
}

bool ActorList::add_actor(Human human){
    if (human.category=="actor" && std::find(list.begin(), list.end(), human) == list.end()) {
        list.push_back(human);
        return true;
    }
    return false;
}

UserList::UserList(){
}

UserList::~UserList(){
}

int UserList::number(){
    return list.size();
}

bool UserList::add_user(Human human){
    if (human.category=="user" && std::find(list.begin(), list.end(), human) == list.end()) {
        list.push_back(human);
        return true;
    }
    return false;
}
