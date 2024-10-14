from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import db, Episode, Guest, Appearance

# Initialize the Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Flask-RESTful
api = Api(app)

# Resources
# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to the Show! We hope you enjoy the episodes and guest appearances. Have a sweet day!")

class EpisodeListResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes])

class EpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200

class GuestListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

class AppearanceResource(Resource):
    def post(self):
        data = request.get_json()

        # Check if required fields are present
        if not all(key in data for key in ['rating', 'guest_id', 'episode_id']):
            return {"errors": ["Missing required fields: rating, guest_id, episode_id"]}, 400

        rating = data.get('rating')
        guest_id = data.get('guest_id')
        episode_id = data.get('episode_id')

        # Validate rating (1-5)
        if not Appearance.validate_rating(rating):
            return {"errors": ["Rating must be between 1 and 5"]}, 400

        # Check if the guest and episode exist
        guest = Guest.query.get(guest_id)
        episode = Episode.query.get(episode_id)

        if not guest or not episode:
            return {"errors": ["Invalid guest or episode"]}, 400

        # Create new appearance
        new_appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(new_appearance)
        db.session.commit()

        return new_appearance.to_dict(), 201

# Register Resources with routes
api.add_resource(EpisodeListResource, '/episodes')
api.add_resource(EpisodeResource, '/episodes/<int:id>')
api.add_resource(GuestListResource, '/guests')
api.add_resource(AppearanceResource, '/appearances')

# Initialize the app
if __name__ == "__main__":
    app.run(debug=True, port=5555)