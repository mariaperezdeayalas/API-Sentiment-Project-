import requests
import sqlalchemy as alch
import pymysql
from Configuration.configuration import engine

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