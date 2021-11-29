import requests
import sqlalchemy as alch
import pymysql
from Configuration.configuration import engine
import dotenv
import os


def check(what,string):
    """
    Parameterized function that checks in every table if the author, quote or episode title exists.
    It will return True if it exists and False if it does not
    """
    if what == "author":
        query = list(engine.execute(f"SELECT Name_Author FROM Authors WHERE Name_Author = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif what == "episode_title":
        query = list(engine.execute(f"SELECT Title_Episode FROM Episodes WHERE Title_Episode = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif what == "quote":
        query = list(engine.execute(f"SELECT Text FROM Quotes WHERE Text = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False


def check2(what, number):
    """
    Second version of the above function but this time for numbers not strings
    """
    if what == "season":
        query = list(engine.execute(f"SELECT Season_Number FROM Seasons WHERE Season_Number = {number}"))
        if len(query) > 0:
            return True
        else:
            return False


def insertAuthor(authors):
    """
    This function receives a list and then calls to the check function defined above to check if the author already exists in the database
    if not, it inserts the author
    """
    for i in authors:
        if check("author", i):
            return "the author already exists"
        else:
            engine.execute(f"INSERT INTO Authors (Name_Author) VALUES ('{i}');")


def insertSeason(seasons):
    """
    This function receives a list and then calls to the check function defined above to check if the season already exists in the database
    if not, it inserts the number of season
    """
    for i in seasons:
        if check2("season", i):
            return "the season already exists"
        else:
            engine.execute(f"INSERT INTO Seasons (Season_Number) VALUES ({i});")


def insertEpisode(df):
    """
    This function receives a list and then calls to the check function defined above to check if the episode already exists in the database
    if not, it inserts the episode
    """
    for i,r in df.iterrows():
        if check("episode", r.episode_title):
            return "the episode already exists"
        else:
            engine.execute(f"INSERT INTO Episodes (Title_Episode, Seasons_id_Season) VALUES ('{r.episode_title}', {r.season});")


def givemetheId(what,string):
    """
    It gives us the ID of what we ask knowing the element exists
    """
    if what == "author":
        return list(engine.execute(f"SELECT id_Author FROM Authors WHERE Name_Author ='{string}';"))[0][0]
    elif what == "episode_title":
        return list(engine.execute(f"SELECT id_Episode FROM Episodes WHERE Title_Episode ='{string}';"))[0][0]


def insertQuote(row):
    """
    Final function to insert the quotes 
    """
    if check("quote", row["quote"]):
        return "the quote already exists"
    else:
        if check("author", row["author"]):
            id_Author = givemetheId("author", row["author"])
        else:
            insertAuthor(row["author"])
            id_Author = givemetheId("author", row["author"])
        
        if check("episode_title", row["episode_title"]):
            id_Episode = givemetheId("episode_title", row["episode_title"])
        else:
            insertEpisode(row["episode_title"])
            id_Episode = givemetheId("episode_title", row["episode_title"])
            
        engine.execute(f"""
        INSERT INTO Quotes (Text, Authors_id_Author, Episodes_id_Episode) VALUES
        ("{row['quote']}", {id_Author}, {id_Episode});
        """)
            