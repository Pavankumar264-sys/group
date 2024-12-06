from flask import Flask, render_template, request, redirect, jsonify
from utils.db import db
from models.ipl_player import IPLPlayer  # Ensure this matches your file structure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IPL.db'  # Updated database for IPL players
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    players = IPLPlayer.query.all()
    return render_template('index.html', content=players)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/top_players')
def top_players():
    return render_template('top_players.html')

@app.route('/players')
def players_list():
    players = IPLPlayer.query.all()
    return render_template('players_list.html', content=players)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    player_id = form_data.get('player_id')
    player_name = form_data.get('player_name')
    team = form_data.get('team')
    matches_played = form_data.get('matches_played')
    runs_scored = form_data.get('runs_scored')
    wickets_taken = form_data.get('wickets_taken')

    # Check if the player already exists
    player = IPLPlayer.query.filter_by(player_id=player_id).first()
    if not player:
        # Create a new IPLPlayer instance
        player = IPLPlayer(
            player_id=player_id,
            player_name=player_name,
            team=team,
            matches_played=matches_played,
            runs_scored=runs_scored,
            wickets_taken=wickets_taken,
        )
        db.session.add(player)
        db.session.commit()
    print("Submitted successfully")
    return redirect('/')


@app.route('/delete/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = IPLPlayer.query.get(player_id)
    if not player:
        return jsonify({'message': 'Player not found'}), 404
    try:
        db.session.delete(player)
        db.session.commit()
        return jsonify({'message': 'Player deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'An error occurred: {e}'}),500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003,debug=True)
