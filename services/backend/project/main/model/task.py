from project import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"Task('{self.content}')"
