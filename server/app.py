from flask import Flask, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)

# ----------------- MODEL -----------------
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    preview = db.Column(db.String, nullable=False)
    minutes_to_read = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "content": self.content,
            "preview": self.preview,
            "minutes_to_read": self.minutes_to_read,
            "date": self.date
        }

# ----------------- ROUTES -----------------
@app.route('/articles/<int:id>', methods=['GET'])
def show_article(id):
    article = db.session.get(Article, id)
    if not article:
        return jsonify({'error': 'Article not found'}), 404

    # Initialize and increment page_views
    session['page_views'] = session.get('page_views', 0) + 1

    # Enforce paywall
    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    return jsonify(article.to_dict()), 200


@app.route('/clear', methods=['GET'])
def clear_session():
    session.clear()
    return jsonify({'message': 'Session cleared'}), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
