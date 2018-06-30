from app import db


class Lawyer(db.Model):
    __tablename__ = "lawyers"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(20))
    lastname = db.Column("lastname", db.Strinng(20))

    def to_string(self):
        return "Name:" + self.name
