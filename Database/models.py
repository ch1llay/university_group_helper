# -*- coding: utf-8 -*-

"""Документация к коду"""

"""смена дирректори для корректной работы проекта"""
if __name__ == '__main__':
    from os.path import split as os_split
    import sys

    sys.path += [os_split(os_split(os_split(os_split(__file__)[0])[0])[0])[0]]

import os

from datetime import date
from datetime import time
from datetime import datetime

from pony.orm import *

from app.db.db_base_func import AddArrtInDbClass

from app.settings.config import *

db = Database()

pony.options.CUT_TRACEBACK = False


class Timetable(db.Entity):
    id = PrimaryKey(int, auto=True)
    subject = Optional('Subject')
    number_week = Optional(int)
    weekday = Optional(int)
    time = Optional(time)
    link = Optional(str)  # ссылка на конференцию или номер аудитории # TODO: добавить номер индентификатор и пароль



class Subject(db.Entity):
    name = Required(str)
    type_subject = Required(str, default="пр.")
    time_tables = Set(Timetable)
    home_tasks = Set('Hometask')
    teachers = Set('Teacher')
    PrimaryKey(name, type_subject)


class Hometask(db.Entity):
    id = PrimaryKey(int, auto=True)
    subject = Optional(Subject)
    text = Optional(str)
    task_on_photo = Optional(Json)
    task_date = Optional(date)
    task_time = Optional(time)
    messages_ids = Optional(Json)  # адишники пересланных сообщений с дз например фото


class Teacher(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    subjects = Set(Subject)
    email = Optional(str)
    phone_number = Optional(str)
    vk_url = Optional(str)


class Phrase_(db.Entity):
    name = PrimaryKey(str)
    text = Optional(str)


class Rank(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    user = Optional('User')


class User(db.Entity):
    user_id = PrimaryKey(int)
    keyboard = Optional(str)
    last_messages = Optional(Json)
    rank = Optional(Rank)
    group = Optional('Group')
    notification = Optional(bool)
    in_black_list = Required(bool, default=False)


class Conversation(db.Entity):
    id = PrimaryKey(int, auto=True)
    type = Optional(str)
    group = Optional('Group')


class Group(db.Entity):
    name = PrimaryKey(str)
    institut = Optional(str)
    users = Set(User)
    conversations = Set(Conversation)
class Message(db.Entity):
    message_id = Required(int)
    peer_id = Required(int)
    text = Optional(str)
    user_id = Optional(int)
    PrimaryKey(message_id, peer_id)


# connect_with_db(db_path="database.sqlite", db_l=db)
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
# for name, ent in db.entities.items():
#     ent.__bases__ = (tuple(list(ent.__bases__) + [AddArrtInDbClass])
#                      if AddArrtInDbClass not in list(ent.__bases__)
#                      else tuple(list(ent.__bases__)))

# def ddd(cls, key1, key2='пр.'):
#     if type(cls) == type(Subject):
#         print('----', key1, key2)
#         cls.__getattribute__(key1, key2)
#
# setattr(Subject, "__getattribute__", classmethod(ddd))

# Subject.__getattribute__()
