# Movie Recommendation system 
### Based on the Weisfeller-Lehman kernel 
##### Basile Van Cooten & Loïc Dagnas

## General
This is our final project for the course "Graphs in Machine Learning" taught by Pr. Michal Valko in the fall semester of 2015 (master MVA, Paris). It concentrates on a recommendation algorithm based on the approximate Weisfeller-Lehman kernel. We will apply it to a movie recommendation system and use the database scraped from the website Sens Critique. We realized this project under the direction of Jan Ramon. 

## Architecture
* The directory `scrappers` contains Python3 scrappers, which scrap movies and users data on http://www.senscritique.com
* The directory `gaph` contains the C++ (and Boost Graph Library) graph structure (constructed with the data scrapped) and the recommendation algorithm.
* The directory `converters` gives a conversion from text file wrote with the python scraper to C++ object (list of movies, directors, actors and users)

 
## Progression
Up to now, the scrappers and C++ converters are ready to be used, but the project is not finished yet (that is why some comments are missing in our code, all our class attributes are public ...). We are currently working on the graph construction with BGL and the recommendation algorithm... 

## First project installation
* clone the repository with `git clone https://github.com/LoicDagnas/MovieRec.git`
* `cd MovieRec`
* create a Python3 virtualenv if you do not already have one with: `virtualenv -p path_to_python3` 
* install the python dependencies `pip install -r requirements.txt`
* install boost for your OS configuration
* build the C++ part `cd graph && make`

If everything went well, you are ready to use the scrappers (it could take hours to scrap the whole database and please be kind with senscritique servers and use our code with sparingly), the converter to text file with `python3 converter.py` in the scrapper directory and the gaph part executing the main with `./main` from the directory `graph`

## Questions?
For any questions feel free to open an issue or find a way to contact us.

