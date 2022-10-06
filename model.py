from app import db
# ---------------------------LOGIN INFO DATA-----------------------------------------------------#
class UserModel(db.Model):
    __tablename__ = 'User_Info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer,  db.ForeignKey('Role_Info.id'))

    def __repr__(self):
        return 'username:%s, password:%s' % (self.name, self.password)

class RoleModel(db.Model):
    __tablename__ = 'Role_Info'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)

    users = db.relationship('UserModel', backref='role')

    def __repr__(self):
        return 'username:%s, password:%s' % (self.name, self.role_name)

# ---------------------------BOOK INFO DATA-----------------------------------------------------#

class BookModel(db.Model):
    __tablename__ = 'Book_Info'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author_id = db.Column(db.Integer,  db.ForeignKey('Author_Info.id'))

    def __repr__(self):
        return 'Book_name:%s, author_id:%s' % (self.book_name, self.author_id)

class AuthorModel(db.Model):
    __tablename__ = 'Author_Info'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(80), unique=True, nullable=False)

    book = db.relationship('BookModel', backref='author')

    def __repr__(self):
        return 'author_name:%s' % (self.author_name)
