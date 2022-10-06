from flask import Flask, jsonify, request, redirect, url_for, flash
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = "sk"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置資料庫為sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(basedir, 'data_register.sqlite')
# app.config['SECRET_KEY']='your key'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
