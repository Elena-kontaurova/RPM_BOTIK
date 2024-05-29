"""Модели для БД"""
from peewee import SqliteDatabase, Model, ForeignKeyField, \
                        TimeField, IntegerField,\
<<<<<<< HEAD
                          CharField,BlobField
=======
                        CharField, BlobField
>>>>>>> abf9465209556c64a8c68c1af0628ec2ba2db3cc
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

<<<<<<< HEAD
class Image(Table):
    '''  таблица картинок'''
    url = CharField()
    id = CharField(primary_key=True)
=======
>>>>>>> abf9465209556c64a8c68c1af0628ec2ba2db3cc

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

<<<<<<< HEAD
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


=======
 
class ImageUser(Table): 
    """ 
    Модель для хранения изображений пользователей. 
    """ 
    id = CharField(primary_key=True) 
    image = BlobField() 
>>>>>>> abf9465209556c64a8c68c1af0628ec2ba2db3cc

class UserImageTag(Table):
    """Класс для управления отправкой картинок пользователям"""
    tg_user_id = IntegerField()
    image = ForeignKeyField(ImageUser, backref='user_image_tags')
    tag = CharField()

db.connect()
db.create_tables([User, Image, Tag, ImageTag, ImageUser, UserImageTag],  safe=True)
<<<<<<< HEAD
db.close()
=======
db.close()
>>>>>>> abf9465209556c64a8c68c1af0628ec2ba2db3cc
