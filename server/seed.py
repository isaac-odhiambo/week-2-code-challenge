from models import db, Episode, Guest, Appearance
from app import app
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Seed data for the database
def seed_data():
    # Create the tables (if they don't exist already)
    with app.app_context():
        db.create_all()

        # Lists to hold created objects
        episodes = []
        guests = []

        # Seed Episodes
        for _ in range(10):  # Generate 10 episodes
            episode = Episode(
                date=fake.date(pattern="%m/%d/%y"),  # Random date
                number=fake.unique.random_int(min=1, max=100)  # Unique episode number
            )
            episodes.append(episode)
            db.session.add(episode)

        # Seed Guests
        for _ in range(15):  # Generate 15 guests
            guest = Guest(
                name=fake.name(),  # Random name
                occupation=fake.job()  # Random job/occupation
            )
            guests.append(guest)
            db.session.add(guest)

        # Commit episodes and guests to the database
        db.session.commit()

        # Seed Appearances (linking guests to episodes)
        for _ in range(30):  # Generate 30 appearances
            appearance = Appearance(
                rating=random.randint(1, 5),  # Random rating between 1 and 5
                guest=random.choice(guests),  # Randomly select a guest
                episode=random.choice(episodes)  # Randomly select an episode
            )
            db.session.add(appearance)

        # Commit all appearances to the database
        db.session.commit()

        print("Database seeded successfully with Faker data!")

# Run the seed function
if __name__ == "__main__":
    seed_data()
