"""SQLAlchemy models and utility functions for TwitOff."""
from flask_sqlalchemy import SQLAlchemy

TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                'common_squirrel', 'KenJennings', 'conanobrien', 'big_ben_clock',
                'IAM_Shakespeare']

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return 'User {}'.format(self.name)

def add_test_users():
    for i, name in enumerate(TWITTER_USERS):
        user = User(id=i, name=name)
        DB.session.add(user)
    DB.session.commit()