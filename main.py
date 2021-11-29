from flask import Flask, request, jsonify
import SRC.main_tools as mt
import SRC.sql_tools as sq

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



if __name__ == '__main__':
    app.run(debug=True)

