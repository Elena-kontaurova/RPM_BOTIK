"""Модели для БД"""
from peewee import SqliteDatabase, Model, ForeignKeyField, \
                        TimeField, IntegerField,\
                          CharField
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
    ''' таблица картинка и пользователь'''
    tg_user = IntegerField()
    image = ForeignKeyField(Image)

class ImageManager:
    # """Класс для управления отправкой картинок пользователям"""

    # @staticmethod
    # def has_sent_image(user_id, image_id):
    #     """Проверяет, была ли отправлена данная картинка данному пользователю"""
    #     try:
    #         ImageUser.get(ImageUser.tg_user == user_id, ImageUser.image == image_id)
    #         return True

    # @staticmethod
    # def send_image(user_id, image_id):
    #     """Отправляет картинку пользователю и сохраняет информацию об этом"""
    #     ImageUser.create(tg_user=user_id, image=image_id)



db.connect()
db.create_tables([User, Image, Tag, ImageTag, ImageUser],  safe=True)
db.close()
