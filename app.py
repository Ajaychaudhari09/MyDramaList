from flask import Flask, render_template,request
import json

app = Flask(__name__)

# Load movie data from JSON file
def load_movie_data():
    with open('movies.json', 'r') as file:
        return json.load(file)

# Search for movies based on user input
def search_movies(query, movie_data):
    query = query.lower()
    for movie in movie_data:
        if query == movie['Name'].lower():
            return movie
    return None

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/movie.html')
def movie():
    return render_template('movie.html')

@app.route('/AnimeQuote.html')
def AnimeQuote():
    return render_template('AnimeQuote.html')

@app.route('/script.js')
def script():
    return render_template('script.js')

@app.route('/animeweb.css')
def css():
    return render_template('animeweb.css')

@app.route('/style.css')
def css1():
    return render_template('style.css')

@app.route('/styles.css')
def css2():
    return render_template('styles.css')



@app.route('/animelist.html')
def anime():
    return render_template('animelist.html')

@app.route('/index.js')
def index1():
    return render_template('index.js')


@app.route('/about.html')
def About():
    return render_template('about.html')



@app.route('/search', methods=['POST'])
def search():
    movie_data = load_movie_data()
    user_input = request.form['user_input'].strip()

    if not user_input:
        return 'Please enter a movie name.'
    elif user_input.lower() == 'quit':
        return 'Goodbye!'
    else:
        found_movie = search_movies(user_input, movie_data)
        if found_movie:
            movie_details = f"Name: {found_movie['Name']}, Year: {found_movie['Year']}, Genre: {found_movie['Genre']}, Duration: {found_movie['Duration']}, Ratings: {found_movie['Rating']}"
            return movie_details
        else:
            return 'Movie not found. Please try again.'

if __name__ == "__main__":
    app.run(debug=True)
