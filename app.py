from flask import Flask, render_template
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

# Fake Premier League teams
teams = [
    "Manchester United", "Liverpool", "Chelsea", "Manchester City", "Arsenal",
    "Tottenham Hotspur", "Leicester City", "Everton", "Aston Villa", "Leeds United"
]

@app.route('/')
def home():
    scores = []
    for _ in range(5):  # Generate 5 random match scores
        match = {
            'home_team': random.choice(teams),
            'away_team': random.choice(teams),
            'home_score': random.randint(0, 5),
            'away_score': random.randint(0, 5)
        }
        scores.append(match)
    return render_template('index.html', scores=scores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
