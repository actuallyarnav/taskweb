from app import app, db  # adjust if your file isn't named app.py

with app.app_context():
    db.create_all()
    print("Database created.")
