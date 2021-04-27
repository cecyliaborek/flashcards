from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class WordsModel(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String())
    polish_translation = db.Column(db.String())
    english_definition = db.Column(db.String())

    def __init__(self, english_word, polish_translation, english_definition):
        self.english_word = english_word
        self.polish_translation = polish_translation
        self.english_definition = english_definition

    def __repr__(self):
        return self.english_word
