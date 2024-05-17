"""Модели для БД"""
from peewee import SqliteDatabase, Model, TimeField, IntegerField

db = SqliteDatabase('sqlite.db')

class Table(Model):
    """Базова таблица, Не будет создана"""
    class Meta:
        """Все таблицы будет сохраняться в одной БД"""
        database = db

class User(Table):
    """Пользователь"""
    tg_user = IntegerField()
    time = TimeField(null=True)

db.connect()
db.create_tables([User],  safe=True)
db.close()
