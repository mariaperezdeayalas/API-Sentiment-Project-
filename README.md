# Friends Sentiment API

## ![Friends](friends.png)

### Overview:
#
In this project I had created an API of Friends TV Show (my favourite!!) dialogue of the 6 main characters with multiple endpoints, and then I had analyzed the sentiments with TextBlob.

The database has been taken from Kaggle, you can find it [here](https://www.kaggle.com/ryanstonebraker/friends-transcript).

### Process:
# 
**Firstly**, I have cleaned the dataset to just get the 6 main characters of the TV show: Rachel, Ross, Monica, Chandler, Phoebe & Joey, and also to have the data in the format desired for the analysis. 

**Secondly**, I had imported the data into SQL with the functions included in `SRC.sql_tools.py`. Note my original dataset had around 50k rows, And I have just included 5k.
There were 2 key functions here:
1. Check function to make sure the data was only included once in SQL.
2. Insert function to insert the data considering the 4 tables of the diagram.

**Thirdly**, the key part of the project, which was creating the API with Flask API. There are 2 main parts on this point:

#### @get:
To see the data already included in the API, below the 5 endpoints created:
- /characters: to obtain the characters
- /lines: to obtain all the lines
- /episodes: to obtain all the episodes
- /quotes/<author>: to get all the lines by character
- /quotes/<author>/<episode>: to get all the lines of a character by episode

#### @post:
To include lines which have not been included yet as I have only taken 10% of the total rows. 
An example of how users can include data below: 

`endpoint = "http://127.0.0.1:5000/newquote"
insert = {"quote": "ON A CAT??!!!!", "author" : 2, "episode" : 4}
requests.post(endpoint, data = insert)`

**Finally**, by doing requests to the API we can analyze the sentiments punctuation of a specific character in a specific episode, to see if the character in that episode was happy or sad. 

To do it, a new endpoint has been created ("/sentiment/<author>/<episode>"), and it will show the mean of all the phrases appearing in the episode of that character. 

### Structure of project files:
#
This project contains:
- A folder with 3 Jupyter Notebooks, one for cleaning, another to include the data in SQL, and one last one to check if the API requests were working. 
- A SRC folder with 3 function files, following the same logic as the notebooks above, except for `main_tools.py` which has all the functions needed for the `main.py` file.
- A Configuration folder with the key data to connect to SQL. 
- A `main.py` file with all the endpoint requests to the API.
- A Data folder containing the data used. 

### Libraries
# 
[sys](https://docs.python.org/3/library/sys.html)

[pandas](https://pypi.org/project/pandas/)

[sqlalchemy](https://www.sqlalchemy.org/)

[re](https://docs.python.org/3/library/re.html)

[textblob](https://textblob.readthedocs.io/en/dev/)

[spacy](https://spacy.io/api/doc)

[nltk](https://www.nltk.org/)

[requests](https://docs.python-requests.org/en/latest/)

[os](https://www.geeksforgeeks.org/os-module-python-examples/)

[dotenv](https://www.npmjs.com/package/dotenv)

[flask](https://flask.palletsprojects.com/en/2.0.x/)













