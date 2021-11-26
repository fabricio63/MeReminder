from flask import Flask, render_template, request, redirect, url_for

import json
from peewee import *
#base de datos
db = SqliteDatabase('people.db')

class Users(Model):
    username = CharField()
    email = CharField()
    password = CharField()
    class Meta:
        database = db 

class Posts(Model):
    post = CharField()
    username = ForeignKeyField(Users)
    class Meta:
        database = db 

db.connect()

db.create_tables([Users,Posts])
#--------------------------------------------

app = Flask(__name__)

# render login / index
@app.route('/', methods =['GET', 'POST'])
def logIn():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        dbuser = Users.select().where(Users.username == username).get()
        
        if(dbuser.password == password):
            posts = []
            for i in Posts.select().join(Users).where(Users.username == username):
                posts.append(i.post)
            
            return render_template('index.html', username = username,links = posts)
    
    else:
        return render_template('login.html')
@app.route('/home', methods=['GET','POST'])
def home():
    username = request.form['homeUser']
    posts = []
    for i in Posts.select().join(Users).where(Users.username == username):
        posts.append(i.post)
    
    return render_template('index.html', links=posts, username=username)
@app.route('/profile', methods=['GET','POST'])
def profile():
    username = request.form['profileUser']
    posts = []
    for i in Posts.select().join(Users).where(Users.username == username):
        posts.append(i.post)
    
    return render_template('profile.html', links=posts, username=username)
#render signup
@app.route('/signup', methods =['GET', 'POST'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        NewUser = Users.create(username = username,email = email, password = password)
        NewUser.save()
        return render_template('login.html')
    
    else:
        return render_template('signup.html')

@app.route('/search', methods=['GET','POST'])
def search():
  username = request.form['searchuser']
  search = request.form["search"]
  searchtag = '#'+ search
  posts = []
  for i in Posts.select().join(Users).where(Users.username == username):
    posts.append(i.post)
  posts_final = []
  for i in posts:
      if searchtag in i:
          posts_final.append(i)
  return render_template('index.html', links = posts_final, username = username)

@app.route('/adder', methods=['GET','POST'])
def adder():
  username = request.form['adderuser']
  post = request.form["post"]
  dbuser = Users.select().where(Users.username == username).get()
  NewUser = Posts.create(post = post,  username = dbuser)
  NewUser.save()
  posts = []
  for i in Posts.select().join(Users).where(Users.username == username):
    posts.append(i.post)

  return render_template('index.html', links = posts, username = username)

@app.route('/delete', methods=['GET','POST'])
def delete():
    username = request.form['adderUser']
    posti = request.form["link"]
    
    post = Posts.get(Posts.post == posti)
    post.delete_instance()
    posts = []
    for i in Posts.select().join(Users).where(Users.username == username):
        posts.append(i.post)

    return render_template('index.html', links = posts, username = username)

if __name__ == "__main__":
  app.run(debug=True)