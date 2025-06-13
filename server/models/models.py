from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    codeforces_handle = db.Column(db.String(50))
    leetcode_username = db.Column(db.String(50))
    codechef_username = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PlatformStats(db.Model):
    __tablename__ = 'platform_stats'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    platform = db.Column(db.String(20))  
    rating = db.Column(db.Integer)
    max_rating = db.Column(db.Integer)
    rank = db.Column(db.String(50))
    total_solved = db.Column(db.Integer)
    easy_solved = db.Column(db.Integer)
    medium_solved = db.Column(db.Integer)
    hard_solved = db.Column(db.Integer)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class ProblemLog(db.Model):
    __tablename__ = 'problem_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    platform = db.Column(db.String(20))
    problem_name = db.Column(db.String(100))
    verdict = db.Column(db.String(30))
    language = db.Column(db.String(50))
    submission_time = db.Column(db.DateTime)

class RatingHistory(db.Model):
    __tablename__ = 'rating_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    platform = db.Column(db.String(20))
    contest_name = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    date = db.Column(db.Date)
