if __name__ == '__main__':
    from os.path import split as os_split
    import sys

    sys.path += [os_split(os_split(os_split(os_split(__file__)[0])[0])[0])[0]]

"""
subject = (subject_name, type_subject)
Subject[subject]
"""
from itertools import chain

from app.bot.botdatabase.bot_model import *

import datetime as dt

PRACTICE = "пр."
THEORY = "лк."
STUDY_GROUP = "20vp1"


@db_session
def create_default_db():
    # TODO: метод будет только создавать поля
    #  (спросить у пользователя n предметов, и составить n полей для этих предметов), а сделать заполнение предложить
    #  в сторонней программе
    subjects = [{"name": "Математика"},
                {"name": "Математика", "type_subject": "лк."},

                {"name": "Программирование"},
                {"name": "Программирование", "type_subject": "лк."},

                {"name": "Физика"},
                {"name": "Физика", "type_subject": "лк."},

                {"name": "Правоведение"},
                {"name": "Правоведение", "type_subject": "лк."},

                {"name": "ТРИР"},
                {"name": "ТРИР", "type_subject": "лк."},

                {"name": "ИТвПД"},

                {"name": "МЛиТА"},
                {"name": "МЛиТА", "type_subject": "лк."},

                {"name": "Английский 1"},
                {"name": "Английский 2"},

                {"name": "Кураторский час", "type_subject": "-"},
                {"name": "Физ-ра", "type_subject": "-"},
                ]
    [Subject(**i) for i in subjects]
    commit()
    teachers = [
        dict(name="Купряшина Лилия Александовна", subjects=Subject.select(lambda i: i.name == "Математика")[:]),
        dict(name="Данилова Валерия Александровна", subjects=Subject.select(lambda i: i.name == "Правоведение")[:]),
        dict(name="Казакова Ирина Анатольевна", subjects=Subject.select(lambda i: i.name == "МЛиТА")[:]),
        dict(name="Костина Наталья Владимировна",
             subjects=[Subject["Физика", PRACTICE]]),
        dict(name="Суровицкая Галина Владимировна",
             subjects=[Subject["Физика", THEORY]]),
        dict(name="Гурьянов Лев Вячеславович", subjects=Subject.select(lambda i: i.name == "Программирование")[:]),
        dict(name="Такташкин Денис Витальевич",
             subjects=Subject.select(lambda i: i.name == "ТРИР" or i.name == "Кураторский час")[:]),
        dict(name="Голобокова Елена Михайловна",
             subjects=[Subject["ИТвПД", PRACTICE]]),
        dict(name="Данкова Наталья Владимировна",
             subjects=[Subject["Английский 1", PRACTICE]]),
        dict(name="Юрасова Ольга Николаевна",
             subjects=[Subject["Английский 2", PRACTICE]])
    ]
    [Teacher(**i) for i in teachers]
    commit()
    timetable = [
        {"number_week": 1, "subject": Subject["Физика", PRACTICE], "time": time(11, 40), "link": "8-507",
         "weekday": 0},
        {"number_week": 1, "subject": Subject["Математика", PRACTICE], "time": time(13, 45), "link": "8-216",
         "weekday": 0},

        {"number_week": 1, "subject": Subject["Математика", PRACTICE], "time": time(9, 50), "link": "7б-205",
         "weekday": 1},
        {"number_week": 1, "subject": Subject["Физ-ра", "-"], "time": time(11, 40), "link": "",
         "weekday": 1},
        {"number_week": 1, "subject": Subject["ИТвПД", PRACTICE], "time": time(13, 45), "link": "7а-405а",
         "weekday": 1},

        {"number_week": 1, "subject": Subject["ТРИР", THEORY], "time": time(9, 50), "link": "7а-425", "weekday": 2},
        {"number_week": 1, "subject": Subject["Программирование", THEORY], "time": time(11, 40), "link": "7а-418",
         "weekday": 2},
        {"number_week": 1, "subject": Subject["Программирование", PRACTICE], "time": time(13, 45), "link": "7а-307",
         "weekday": 2},
        {"number_week": 1, "subject": Subject["МЛиТА", PRACTICE], "time": time(15, 35), "link": "7а-307",
         "weekday": 2},

        {"number_week": 1, "subject": Subject["Физика", THEORY], "time": time(8, 0),
         "link": r"https://us04web.zoom.us/j/3881678889?pwd=KzlRejJ0dnB6SCszOVVzSkhOUm9UUT09#success идентификатор 3881678889 пароль 1GnL1S дата обновления 9.02.2021",
         "weekday": 3},
        {"number_week": 1, "subject": Subject["Математика", THEORY], "time": time(9, 50),
         "link": r"https://us04web.zoom.us/j/75974098629?pwd=MUxSMDZ4bnBaeElaQ1llMmJzekVTdz09#success идентификатор 74153390010 пароль 1nU6TH дата обновления 11.02.2021",
         "weekday": 3},

        {"number_week": 1, "subject": Subject["ТРИР", PRACTICE], "time": time(8, 0), "link": "7а-108",
         "weekday": 4},
        {"number_week": 1, "subject": Subject["Английский 1", PRACTICE], "time": time(9, 50), "link": "8-807",
         "weekday": 4},
        {"number_week": 1, "subject": Subject["Английский 2", PRACTICE], "time": time(9, 50), "link": "8-807б",
         "weekday": 4},
        {"number_week": 1, "subject": Subject["Физ-ра", "-"], "time": time(11, 40), "link": "",
         "weekday": 4},

        {"number_week": 1, "subject": Subject["Правоведение", THEORY], "time": time(8, 0),
         "link": r"https://us04web.zoom.us/j/5981307260?pwd=VDBhWnFzUUtLVlBNWEUzS2Z3em5Ydz09 идентификатор 5981307260 пароль uQDta5 дата обновления 20.02.2021",
         "weekday": 5},
        {"number_week": 1, "subject": Subject["МЛиТА", THEORY], "time": time(9, 50),
         "link": "https://us04web.zoom.us/j/74153390010?pwd=RXdZRUVRMWJUd29GczYwSDhJNC9YZz09 идентификатор 74153390010 пароль 2Hhng0 дата обновления 18.02.2021",
         "weekday": 5},

        {"number_week": 2, "subject": Subject["Кураторский час", "-"], "time": time(9, 50), "link": "7а-307",
         "weekday": 0},
        {"number_week": 2, "subject": Subject["Физика", PRACTICE], "time": time(11, 40), "link": "",
         "weekday": 0},

        {"number_week": 2, "subject": Subject["Математика", PRACTICE], "time": time(9, 50), "link": "7б-205",
         "weekday": 1},
        {"number_week": 2, "subject": Subject["Физ-ра", "-"], "time": time(11, 40), "link": "",
         "weekday": 1},
        {"number_week": 2, "subject": Subject["ИТвПД", PRACTICE], "time": time(13, 45), "link": "7а-405а",
         "weekday": 1},

        {"number_week": 2, "subject": Subject["Программирование", THEORY], "time": time(11, 40), "link": "7а-418",
         "weekday": 2},
        {"number_week": 2, "subject": Subject["Программирование", PRACTICE], "time": time(13, 45), "link": "7а-307",
         "weekday": 2},
        {"number_week": 2, "subject": Subject["Правоведение", PRACTICE], "time": time(15, 35), "link": "7а-425",
         "weekday": 2},

        {"number_week": 2, "subject": Subject["Физика", THEORY], "time": time(8, 0),
         "link": r"https://us04web.zoom.us/j/3881678889?pwd=KzlRejJ0dnB6SCszOVVzSkhOUm9UUT09#success идентификатор 3881678889 пароль 1GnL1S дата изменения 9.02.2021",
         "weekday": 3},
        {"number_week": 2, "subject": Subject["Математика", THEORY], "time": time(9, 50),
         "link": r"https://us04web.zoom.us/j/75974098629?pwd=MUxSMDZ4bnBaeElaQ1llMmJzekVTdz09#success идентификатор 75974098629 пароль 1nU6TH дата изменения 11.02.2021",
         "weekday": 3},

        {"number_week": 2, "subject": Subject["ТРИР", PRACTICE], "time": time(8, 0), "link": "7а-108", "weekday": 4},
        {"number_week": 2, "subject": Subject["Английский 1", PRACTICE], "time": time(9, 50), "link": "8-807",
         "weekday": 4},
        {"number_week": 2, "subject": Subject["Английский 2", PRACTICE], "time": time(9, 50), "link": "8-807б",
         "weekday": 4},
        {"number_week": 2, "subject": Subject["Физ-ра", "-"], "time": time(11, 40), "link": "",
         "weekday": 4}
    ]
    [Timetable(**i) for i in timetable]
    commit()

    phrases = [
        dict(name="start",
             text="Привет! У меня ты сможешь узнать расписание, домашнее задание, и что-нибудь еще, если это что-то в меня добавят)"),
        dict(name="timetable",
             text="1)8:00-9:35\n2)9:50-11:25\n3)11:40-13:15\n4)13:45-15:20\n5)15:35-17:10"),
        dict(name="/help",
             text="start, начать - приветсвенное сообщение\n"
                  "/current_timetable - актуальное расписание"
                  "/today, бот скинь расписание на сегодня - скидывает расписание на сегодня/в понедельник, если спросить в середине дня в субботу\n"
                  "/tomorrow, бот скинь расписание на завтра - скидывает расписание на завтра/понедельник, если спросить в субботу\n"
                  "/week, бот скинь расписание на неделю - скидывает расписание на неделю(на следующую, если спросить в субботу в середине дня или воскресенье\n"
                  "/timetable, бот скинь расписание пар - скидывает расписание пар\n"
                  "/<название предмета латиницей>, бот <предмет на русском> преподы - скидывает преподов по предмету\n"
                  "/menu, меню - возвращает в главное меню\n"
                  "---------------------------------------\n"
                  "работа с дз\n"
                  "/<команда на русском> предмет (для физики тип предмета(практика, лекция) дата(формат дд.мм.гггг (если добавление)домашка\n"
                  "Виды комманд:\n"
                  "/получить_дз физика практика 22.03.2021\n"
                  "---------------------------------------\n"
                  "/help, помощь - скидывает список комманд"),
    ]

    [Phrase_(**i) for i in phrases]
    commit()

    Group(name="20vp1")
    commit()
    conversations = [dict(type="important", group=Group["20vp1"])]
    [Conversation(**i) for i in conversations]
    commit()
    users = [dict(user_id=159526068, rank=Rank(name="admin"), group=Group["20vp1"])]
    [User(**i) for i in users]
    commit()
    ranks = [dict(name="admin", user=User.select(lambda i: i.user_id == 159526068)[:][0])]
    [Rank(**i) for i in ranks]
    commit()


weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]


@db_session
def add_subject(name, type_subject="пр."):
    Subject(name=name, type_subject=type_subject)
    commit()


# @Subject.only_func
@db_session
def add_home_task(subject, text, d, fwd_messages=None):
    base = dict(subject=Subject[subject], text=text, task_date=d)
    if fwd_messages:
        base.update(dict(messages_ids=fwd_messages))
    Hometask(**base)
    commit()


# @Subject.only_func
@db_session
def delete_home_task_from_subject_date(subject, d):
    [i.delete() for i in Subject[subject].home_tasks.select() if lambda i: i.task_date == d]


@db_session
def delete_home_all_task_date(d):
    map(lambda i: i.delete(),
        Hometask.select(lambda i: i.task_date == d)[:])


@db_session
def get_home_task(d) -> list:
    task = []
    if not d:
        task = list(map(lambda i: i.text, Hometask.select()[:]))
    else:
        task = [(i.text, i.task_date) for i in Hometask.select() if i.task_date == d]
    return task


# @Subject.only_func
@db_session
def get_home_task(subject, d: date):
    if not d:
        task = [i.text for i in Subject[subject].home_tasks.select()]
    else:
        task = [i.text for i in Subject[subject].home_tasks.select() if i.task_date == d]
    task_s = f"{subject[0]} {subject[1]} {d.day}.{'0' + str(d.month) if len(str(d.month)) == 1 else d.month}.{d.year}" "\n" + '\n\t'.join(
        task)
    return task_s


@db_session
def get_teachers(subject):
    subjects = [i for i in Subject.select() if i.name == subject]
    # print(subjects)
    teachers_s = subject
    for i in subjects:
        if i.type_subject == PRACTICE:
            teachers_s += f"\nпрактика {list(i.teachers)[0].name}\n"
        elif i.type_subject == THEORY:
            teachers_s += f"лекция {list(i.teachers)[0].name}\n"
        else:
            teachers_s += f"{list(i.teachers)[0].name}\n"
    return teachers_s


@db_session
def get_timetable_day(day):
    msg = ""
    weekday = day.weekday() if day.weekday() < 6 else 0
    wk = day.isocalendar()[1]
    if day.weekday() < 6:
        number_week = 1 if wk % 2 else 2
    elif day.weekday() == 5 and day.hour < 11:
        number_week = 1 if wk % 2 else 2
    else:
        msg = "Я тебя понял, расписание на понедельник следующей недели"
        number_week = 2 if wk % 2 else 1
    timetable = [(i.time, i.subject, i.link) for i in Timetable.select() if
                 i.number_week == number_week and i.weekday == weekday]
    timetable_s = f"{msg}\n{weekdays[weekday]}\n"
    print(weekday, number_week)
    # print(str(timetable))
    for t, s, l in timetable:
        timetable_s += f"{t.hour}:{'00' if str(t.minute) == '0' else t.minute} {s.name} {s.type_subject} {l}\n"
        # print(timetable_s)
    return timetable_s


@db_session
def get_timetable_week():
    msg = ""
    today = datetime.today()
    weekday = today.weekday()
    week = today.isocalendar()[1]
    if (weekday == 5 and today.time().hour > 11) or weekday == 6:
        msg = "Я тебя понял, даю расписанию на следующую неделю\n"
        number_week = 2 if week % 2 else 1
    else:
        number_week = 1 if week % 2 else 2
    timetable_s = f"{msg}неделя {number_week}\n"
    for _ in range(0, 6):
        timetable_s += f"{weekdays[_]}\n"
        timetable = [dict(time=i.time, subject=i.subject, link=i.link) for i in Timetable.select()
                     if i.number_week == number_week and i.weekday == _]
        for j in timetable:
            timetable_s += f'{str(j["time"])[0:-3]} {j["subject"].name} {j["subject"].type_subject} {j["link"]}' + '\n'
    return timetable_s


def get_ids_on_rank(name):
    pass


@db_session
def get_phrase(name):
    return Phrase_[name].text


@db_session
def change_homework_on_day(subject, homework, d):
    for i in Subject[subject].home_tasks.select():
        if i.task_date == d:
            i.text = homework


def executable(function):
    with db_session:
        return function()


@db_session
def add_user(user_id):
    if not User.exists(user_id=user_id):
        User(user_id=user_id)
        commit()


@db_session
def add_user_rank(user_id, t, from_user_id=None, class_Bot=None):
    if type(user_id) != int:
        if from_user_id and class_Bot:
            class_Bot.reply(user_id=from_user_id, message=f"не удалось распознать {user_id}")
        return
    try:
        User[user_id].rank.name = t
    except Exception as e:
        print(e)
        User(user_id=user_id, rank=Rank(name=t), group=Group[STUDY_GROUP])
        commit()
        rank = dict(name=t, user=User.select(lambda i: i.user_id == user_id)[:][0])
        Rank(**rank)
    return user_id


def set_notification(user_id):
    notification = User[user_id].notification
    notification = not notification
    User[user_id].notification = notification
    return notification


@db_session
def get_current_timetable():
    today = datetime.today()
    wk = today.isocalendar()[1]
    if today.weekday() < 5:
        if today.hour > 17:
            weekday = (today + dt.timedelta(days=1)).date().weekday()
        else:
            weekday = today.weekday()
        number_week = 1 if wk % 2 else 2
    elif today.weekday() == 5 and today.hour < 11:
        weekday = today.weekday()
        number_week = 1 if wk % 2 else 2
    else:
        weekday = 0
        number_week = 2 if wk % 2 else 1
    timetable = [(i.time, i.subject, i.link) for i in Timetable.select() if
                 i.number_week == number_week and i.weekday == weekday]
    timetable_s = f"{weekdays[weekday]}\n"
    for t, s, l in timetable:
        timetable_s += f"{t.hour}:{'00' if str(t.minute) == '0' else t.minute} {s.name} {s.type_subject} {l}\n"
    return timetable_s


@db_session
def get_timetable_day_time(day, t):
    today = day
    wk = today.isocalendar()[1]
    if today.weekday() < 5:
        if today.hour > 17:
            weekday = (today + dt.timedelta(days=1)).date().weekday()
        else:
            weekday = today.weekday()
        number_week = 1 if wk % 2 else 2

    elif today.weekday() == 5 and today.hour < 11:
        weekday = today.weekday()
        number_week = 1 if wk % 2 else 2
    else:
        weekday = 0
        number_week = 2 if wk % 2 else 1
    timetable = [(i.time, i.subject, i.link) for i in Timetable.select() if
                 i.number_week == number_week and i.weekday == weekday and i.time == t]
    timetable_s = ""
    for t, s, l in timetable:
        timetable_s += f"{t.hour}:{'00' if str(t.minute) == '0' else t.minute} {s.name} {s.type_subject} {l}\n"
    return timetable_s


@db_session
def add_conversation(peer_id, t):
    Conversation(id=peer_id, type=t, group=Group[STUDY_GROUP])


@db_session
def get_conversaton(t):
    ids = [i.id for i in Conversation.select() if i.group.name == STUDY_GROUP and i.type == t]
    return ids


# @db_session
# def change_timetable(day, t, subject, link):
#     pass


if __name__ == "__main__":
    create_default_db()
    print(get_timetable_week())
    # add_home_task(("Математика", PRACTICE), "номер 1", date(2021, 3, 20))
    # with db_session:
    #     show(Hometask.select())

    # with db_session:
    #     User[159526068].last_messages = {}
# get_timetable_day(datetime.today().date())
# with db_session:
# create_default_db()
# print(Subject.__class_getitem__())
# print(get_timetable_day((datetime.today()+dt.timedelta(days=1)).date()))
# print(Subject["МатеМатика", PRAKTIKA])
# # create_default_db()
#     # sbjt = "Английский 2"
#     # subject_type = PRAKTIKA
#     # subject = Subject[sbjt, subject_type]
#     # subject.add_home_task("подготовить топик", (2021, 3, 11))
#     # # subject.delete_home_task_from_date((2021, 3, 11))
#     # print(subject.get_home_task((2021, 3, 11)))
#     print([i.subject for i in Timetable.select() if i.weekday == 0 and i.number_week == 1])
