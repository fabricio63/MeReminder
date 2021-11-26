from peewee import *
db = SqliteDatabase('people.db')

class Users(Model):
    username = CharField()
    email = CharField()
    password = CharField()
    class Meta:
        database = db 

class Tablero(Model):
    user = ForeignKeyField(Users, backref = 'fotos')
    link = CharField()
    class Meta:
        database = db 

class Holder(Model):
    username = CharField()
    class Meta:
        database = db 
db.connect()

db.create_tables([Users,Tablero,Holder])
NewUser = Holder.create(username = 'username')