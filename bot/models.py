"""Модели для БД"""
from peewee import SqliteDatabase, Model, ForeignKeyField, \
                        TimeField, IntegerField,\
                          CharField,BlobField
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

class Image(Table):
    '''  таблица картинок'''
    url = CharField()
    id = CharField(primary_key=True)

class Tag(Table):
    ''' таблица тэгов'''
    name = CharField()

class ImageTag(Table):
    ''' таблица картинка и тэг'''
    image = ForeignKeyField(
        Image,
        backref='image_tag'
    )
    tag = ForeignKeyField(
        Tag,
        backref='image_tag'
    )

class ImageUser(Table):
    """
    Модель для хранения изображений пользователей.
    """
    id = CharField(primary_key=True)
    image = BlobField()


class UserImageTag(Table):
    """
    Модель для хранения связи между пользователем, изображением и тегом.
    """
    telegram_user_id = IntegerField()
    image = ForeignKeyField(ImageUser, backref='user_image_tags')
    tag = CharField()




db.connect()
db.create_tables([User, Image, Tag, ImageTag, ImageUser, UserImageTag],  safe=True)
db.close()
