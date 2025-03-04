import click
from app import initialize_db, app
from models import db, User, UserPokemon, Pokemon


@app.cli.command("init", help="Creates and initializes the database")
def initialize():
  initialize_db()
  print('database initialized')
  
@app.cli.command("testHash")
def testHash():
  User.check_password_hash_for_user(1)