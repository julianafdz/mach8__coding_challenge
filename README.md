# Mach 8 Coding Challenge

## How to execute the app:

### Install and activate your virtualenv
- pip install virtualenv
- virtualenv env
- env/Scripts/activate (or source env/bin/activate)

### Clone Django project
https://github.com/julianafdz/mach8__coding_challenge.git

### Install requirements
- pip install -r requirements.txt

### Run project
- execute python manage.py runserver

### Run Test
- execute python manage.py test

## About the code:
The idea behind the search algorithm was to develop an efficient system that did not require iterating through each data item in a double loop (nested loop).

First I organize the data into a dictionary whose keys are all the heights available in the data.

As I iterate through the data and create the keys, I also add the content of the players to their corresponding key.

This creates new data organized in a height dictionary.

Finally, the search algorithm is based on a main iteration through the height dictionary (which is notably shorter to go through) and then subtracting each of those heights (keys) from the user input, since in this way I find if that height has another matching height with which, added, they give as a result the user's input.

If the subtract (or result of the subtraction), is not found in the dictionary, the height (key) and therefore all the players that this key contains, are not used to make pairs with others (given the user's input).

Otherwise, if the subtract is found in the dictionary, I iterate through the list of players of each of the heights (keys), to create the pairs (I don't iterate doing a lookup, just to group the players into tuples).

Likewise, to avoid repeated data and time wasting, as a height (key) is revised or with which it has been paired, I add it to a list of keys that have already been revised, in order to avoid going back to go through it. With the latter, the iteration through the height dictionary becomes even shorter as it goes through the dictionary.

## Documents in which the code is located
As it is a django project, it has several documents that are generated instantly and that do not contain any useful code for this app. Therefore, the documents in which the developed App is found are the following:

- methods.py (contains the data organization method and the search algorithm)
- tests.py (contains the unit test)
- views.py (contains a single view that handles the requests and executes the methods)
- urls.py (contains the matching url)
- templates/Searcher folder with a signle page template index.html
