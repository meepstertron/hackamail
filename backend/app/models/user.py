from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(80)) # 'admin', 'moderator', 'user'
    # admin:
    # - can create, update, delete users
    # - can create (on their behalf), delete messages
    # - can acceess all messages
    # - can hand out roles
    # - ban users
    # - mod panel
    # - edit config (filter words, etc.)
    # moderator:
    # - can create (on their behalf), delete messages
    # - can only access messages that have been flagged
    # - mod panel
    # - Ban users
    # user:
    # - can create messages
    # - can only delete their own messages
    # - can only access their own messages
    # - can flag messages
    # - can edit their profile
