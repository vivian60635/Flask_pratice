from flask import Flask, jsonify, request, redirect, url_for, flash
from flask import render_template
from form import RegistrationForm, LoginForm, SearchForm, EditForm
import os

from app import app
from model import UserModel, RoleModel, BookModel, AuthorModel, db

@app.route('/')
def index():
    # return render_template('Score.html')
    #return render_template('Login.html')
    # return redirect(url_for('register'))
    return redirect(url_for('login'))

@app.route('/Editbook', methods=['POST', 'GET'])
def editbook():
    """
        use wtforms to generate the regisiter structure
    """
    form = EditForm(request.form)

    if request.method == 'POST' and form.validate_on_submit:
        try:
            book_info = BookModel.query.filter_by(book_name=form.book_name.data).first()
        except:
            book_info=None

        try:
            author = AuthorModel.query.filter_by(author_name=form.author.data).first()
        except:
            author=None
        
        try:
            dele_book_info = BookModel.query.filter_by(book_name=form.book_name.data,  author_id=author.id).first()
        except:
            dele_book_info=None

        if form.add.data:
            
            
            if book_info:
                flash('Already has this book')
            else:
                if not author:
                    new_author = AuthorModel(author_name=form.author.data)
                    db.session.add(new_author)
                    db.session.commit()
                    flash('Add author: {} into library',  form.author.data )

                author = AuthorModel.query.filter_by(author_name=form.author.data).first()
                new_book = BookModel(book_name=form.book_name.data, author_id=author.id)
                db.session.add(new_book)
                db.session.commit()
                flash('Add book: {} into library'.format(form.book_name.data ))

        if form.delete.data:

            if dele_book_info:

                db.session.delete(dele_book_info)
                db.session.commit()
                flash('Delete book: {} into library'.format(form.book_name.data ))
            
            else:
                flash('The book: {} author:{} not in library'.format(form.book_name.data, form.author.data))

                


            
    return render_template('edit.html', form=form)

@app.route('/Search', methods=['POST', 'GET'])
def search():
    """
        use wtforms to generate the regisiter structure
    """
    form = SearchForm(request.form)

    if request.method == 'POST':
        if form.edit.data:

            return redirect(url_for('editbook'))

        if form.book_name.data:
            book_info = BookModel.query.filter_by(book_name=form.book_name.data).all()
            return render_template('search.html', form=form, info=book_info)
    
        elif form.author.data:
            author = AuthorModel.query.filter_by(author_name=form.author.data).first()
            book_info = author.book
            return render_template('search.html', form=form, info=book_info)


    

    return render_template('search.html', form=form, info=[])

    
@app.route('/Login', methods=['POST', 'GET'])
def login():
    """
    use wtforms to generate the regisiter structure
    """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.registr.data:
        return redirect(url_for('register'))

    if request.method == 'POST' and form.validate():
        user_info = [form.username.data,  form.password.data]

        return redirect(url_for('search'))
    
    return render_template('login.html', form=form)


@app.route('/Register', methods=['POST', 'GET'])
def register():
    """
    use wtforms to generate the regisiter structure
    """
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        print('validate_on_submit is',  form.validate_on_submit())
        user_info = [form.username.data, form.accept_tos.data, form.password.data]
        user = UserModel(
            name = form.username.data,
            email = form.email.data,
            password = form.password.data,
            role_id = 2
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()

    # role1 = RoleModel(role_name='admin')
    # role2 = RoleModel(role_name='user')
    
    # user = UserModel(name = 'vivi', email = 'vivi@gmail',password = '1234',role_id = 1)

    # b1 = BookModel(book_name='How are you', author_id=1)
    # b2 = BookModel(book_name='python', author_id=1)
    # b3 = BookModel(book_name='java', author_id=2)
    # b4 = BookModel(book_name='c', author_id=2)
    # b5 = BookModel(book_name='c#', author_id=3)

    # a1 = AuthorModel(author_name='hea')
    # a2 = AuthorModel(author_name='lee')
    # a3 = AuthorModel(author_name='kim')
    # a4 = AuthorModel(author_name='hung')
    # a5 = AuthorModel(author_name='chen')

       
    # db.session.add_all([role1, role2])
    # db.session.add_all([a1, a2, a3, a4, a5])
    # db.session.add_all([b1, b2, b3, b4, b5])
    # db.session.add(user)
    # db.session.commit()


   
    app.run(debug=True)
