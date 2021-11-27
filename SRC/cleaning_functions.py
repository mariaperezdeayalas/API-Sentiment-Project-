def substitute(x):
    """
    Function to substitute the quotation marks in the string elements
    so we do not have errors later when doing the sentiment analysis
    """
    x = str(x).replace('"', "`")
    x = str(x).replace("'", "`")
    return x