from app import db, app, Article

with app.app_context():
    print("Resetting database...")
    db.drop_all()
    db.create_all()

    print("Seeding articles...")
    articles = [
        Article(id=1, title="Article One", author="Author One", content="Content for article one", preview="Preview of article one", minutes_to_read=5, date="2024-01-01"),
        Article(id=2, title="Article Two", author="Author Two", content="Content for article two", preview="Preview of article two", minutes_to_read=3, date="2024-01-02"),
        Article(id=3, title="Article Three", author="Author Three", content="Content for article three", preview="Preview of article three", minutes_to_read=7, date="2024-01-03"),
        Article(id=4, title="Article Four", author="Author Four", content="Content for article four", preview="Preview of article four", minutes_to_read=4, date="2024-01-04")
    ]

    db.session.add_all(articles)
    db.session.commit()
    print("Seeding complete.")
