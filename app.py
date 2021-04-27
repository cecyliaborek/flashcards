import os

from flask import Flask, render_template
from flask_migrate import Migrate


from models import WordsModel, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def hello():
    english_word = 'apron'
    return render_template('flashcard_index.html', english_word=english_word)

if __name__ == '__main__':
    app.run()