from utils.db import db

class IPLPlayer(db.Model):  # Specify the table name for IPL players

    # Defining the columns for the table
    player_id = db.Column(db.Integer, primary_key=True)  # Unique ID for each player
    player_name = db.Column(db.String(255), nullable=False)  # Name of the player
    team = db.Column(db.String(255), nullable=False)  # Name of the team
    matches_played = db.Column(db.Integer, nullable=False)  # Total matches played by the player
    runs_scored = db.Column(db.Integer, nullable=False)  # Total runs scored by the player
    wickets_taken = db.Column(db.Integer, nullable=False)  # Total wickets taken by the player