## Flask API for TV Show Episodes and Guests
## Project Overview
This project is a RESTful API built using Flask, which manages episodes, guests, and their appearances on a TV show. The API provides endpoints for retrieving, creating, and managing information related to episodes and guests through appearances. Each appearance includes a guest's rating for their performance on a specific episode.

Table of Contents
Project Structure
Models
Technologies Used
Routes and API Endpoints
Implementation Details
Seeding the Database
Running the Project
Future Improvements
Project Structure
The project follows a simple yet scalable structure to manage the Flask application, models, and routes.


.
├── app.py               # Main application file
├── models.py            # Contains SQLAlchemy models
├── app.py            # API routes (combined into app.py)
├── seed.py              # Script to seed the database with data
├── migrations/          # Directory to handle database migrations
├── instance/            # Holds the database (SQLite in this case)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
Key Files:
app.py: The main entry point for the application, initializes Flask, sets up routes, and configures the database.
models.py: Contains the SQLAlchemy models (Episode, Guest, Appearance) and relationships.
routes.py: Defines API endpoints for interacting with the episodes, guests, and appearances.
seed.py: Script that populates the database with sample or randomized data using the Faker library.
migrations/: Directory managed by Flask-Migrate for handling database migrations.
Models
The project uses SQLAlchemy to define models and relationships. There are three main models:

1. Episode
Represents an episode of a TV show.

Attribute	Type	Description
id	Integer	Primary key
date	String	Date of the episode
number	Integer	Unique episode number
2. Guest
Represents a guest appearing on the show.

Attribute	Type	Description
id	Integer	Primary key
name	String	Name of the guest
occupation	String	Job title or occupation of the guest
3. Appearance
Represents a guest's appearance on an episode and includes a rating for that appearance.

Attribute	Type	Description
id	Integer	Primary key
rating	Integer	Rating of the guest's appearance (1-5)
episode_id	Integer	Foreign key linked to Episode
guest_id	Integer	Foreign key linked to Guest
Model Relationships:
An Episode has many Guests through Appearance.
A Guest has many Episodes through Appearance.
An Appearance belongs to a Guest and an Episode (many-to-many relationship).
Technologies Used
Backend:
Flask: A micro-framework for building the web application.
Flask-RESTful: Extends Flask to easily build REST APIs.
SQLAlchemy: An ORM to manage database models and queries.
Flask-Migrate: Handles database migrations with Alembic.
Faker: A library used to generate fake data for database seeding.
Database:
SQLite: A lightweight, serverless database used for local development.
Routes and API Endpoints
1. Home Route
GET /: Returns a welcome message in JSON format.
Example:

json
Copy code
{
  "message": "Welcome to the Show! We hope you enjoy the episodes and guest appearances. Have a sweet day!"
}
2. Episodes
GET /episodes: Returns a list of all episodes.
GET /episodes/
: Returns details of a specific episode, including its appearances.
Example of an episode with appearances:

json
Copy code
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 4
    }
  ]
}
3. Guests
GET /guests: Returns a list of all guests.
Example:

json
Copy code
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "comedian"
  }
]
4. Appearances
POST /appearances: Creates a new appearance by associating an existing guest and episode. Requires rating, guest_id, and episode_id in the request body.
Example of a request body:

json
Copy code
{
  "rating": 5,
  "episode_id": 100,
  "guest_id": 123
}
Example of a successful response:

json
Copy code
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "date": "1/12/99",
    "id": 2,
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
Implementation Details
Model Serialization: Each model (Episode, Guest, Appearance) includes a method to serialize the object into a dictionary using to_dict(). This allows easy conversion to JSON format for API responses.

Validations:

The Appearance model ensures that ratings are between 1 and 5. If the rating is out of this range, an error is returned.
Proper error handling is included for invalid guest IDs or episode IDs in the POST /appearances route.
Database Relationships: Episode, Guest, and Appearance are linked using foreign keys, ensuring that cascaded deletions are managed properly. When an episode or guest is deleted, their associated appearances are also deleted.

Seeding the Database
The project includes a seed.py script that uses the Faker library to populate the database with random data.

##  to run the seed script:
Install the required dependencies:


pip install -r requirements.txt
Run the seed script:

python seed.py
This will populate the database with random episodes, guests, and appearances.

Running the Project
1. Install Dependencies
Make sure you have Python 3 and pip installed. Install the dependencies using the following command:


pip install -r requirements.txt
2. Migrate the Database
Run the following commands to create the database tables:


flask db init
flask db migrate
flask db upgrade
3. Run the Application
Start the Flask development server:

bash
Copy code
python app.py
By default, the application will be available at http://localhost:5555.

Future Improvements
Authentication: Add user authentication to control access to certain endpoints.
Pagination: Implement pagination for large datasets (e.g., when listing episodes or guests).
Error Handling: Expand error handling to catch more edge cases and provide clearer error messages.
Contributing
Feel free to fork this repository and submit pull requests for improvements. Contributions are always welcome!


This README.md gives a thorough overview of the project, including the structure, models, routes, and how to get the project running. Let me know if you need more details or have any questions!

## author 
isaac odhiambo 






