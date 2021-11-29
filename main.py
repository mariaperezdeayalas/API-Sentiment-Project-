from flask import Flask, request, jsonify
import SRC.main_tools as mt

app = Flask(__name__)

@app.route("/")
def initial():
    return "Welcome Friends' fans!"

@app.route("/characters")
def gimmethecharacters():
    charact = mt.authors()
    return jsonify(charact)

@app.route("/lines")
def gimmethelines():
    line = mt.lines()
    return jsonify(line)

@app.route("/episodes")
def gimmetheepisodes():
    episode = mt.episode_title()
    return jsonify(episode)

@app.route("/quotes/<author>")
def quotes(author):
    line = mt.quotes(author)
    return jsonify(line)

@app.route("/quotes/<author>/<episode>")
def quotes_episode(author,episode):
    line_episode = mt.quotes_episode(author,episode)
    return jsonify(line_episode)

@app.route("/newquote", methods=["POST"])
def insertquote():
    quote = request.form.get('quote')
    author = request.form.get('author')
    episode = request.form.get('episode')
    return mt.new_quote(quote,author,episode)

@app.route("/sentiment/<author>/<episode>")
def sentiment_author(author,episode):
    df = mt.sentiment_analysis(author,episode)
    df['Tokenized'] = df['Text'].apply(mt.tokenizer)
    df['Sentiments'] = df['Tokenized'].apply(mt.sentiment)
    return str(df.Sentiments.mean())

if __name__ == '__main__':
    app.run(debug=True)

