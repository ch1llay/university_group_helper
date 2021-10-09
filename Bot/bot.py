# # -*- coding: utf-8 -*-
#
# """основной файл функционала бота"""
#
# from modules import *
# from threading import Thread
# import time as tm
#
#
# class Keyboards:
#     @staticmethod
#     def get_keyboard():
#         keyboard = VkKeyboard(one_time=False)
#         keyboard.add_button("Меню", color=VkKeyboardColor.SECONDARY, payload={"payload": "/menu"})
#         keyboard.add_line()
#         keyboard.add_openlink_button("Ссылка на диск", "https://yadi.sk/d/0W7wTf29wwaOYw")
#         return keyboard.get_keyboard()
#
#     @staticmethod
#     def get_menu():
#         # inline клавиатура для браузера
#         menu = VkKeyboard(inline=True)
#         menu.add_callback_button("Расписание на неделю", color=VkKeyboardColor.POSITIVE,
#                                  payload='{"payload":"/week"}')
#         menu.add_line()
#         menu.add_callback_button("Текущее актуальное расписание", color=VkKeyboardColor.POSITIVE,
#                                  payload='{"payload":"/current_timetable"}')
#         menu.add_callback_button("Расписание на сегодня", color=VkKeyboardColor.POSITIVE,
#                                  payload='{"payload":"/today"}')
#         menu.add_line()
#         menu.add_callback_button("Расписание на завтра", color=VkKeyboardColor.POSITIVE,
#                                  payload='{"payload":"/tomorrow"}')
#         menu.add_line()
#         menu.add_callback_button("Расписание пар", color=VkKeyboardColor.POSITIVE,
#                                  payload='{"payload":"/timetable"}')
#         menu.add_line()
#         menu.add_callback_button("ФИО преподавателей", color=VkKeyboardColor.POSITIVE,
#                                  payload='{"payload":"/teachers"}')
#         menu.add_line()
#         menu.add_callback_button("Помощь", payload={"payload": "/help"})
#
#         return menu.get_keyboard()
#
#     @staticmethod
#     def get_subjects_keyboard():
#         # клавиатура для получения информации о преподавателях
#         subjects_keyboard = VkKeyboard(inline=True)
#         subjects_keyboard.add_callback_button("Английский", payload={"payload": "/english"})
#         subjects_keyboard.add_callback_button("ИТвПД", payload={"payload": "/itvpd"})
#         subjects_keyboard.add_line()
#         subjects_keyboard.add_callback_button("Математика", payload={"payload": "/math"})
#         subjects_keyboard.add_callback_button("МЛиТА", payload={"payload": "/mlita"})
#         subjects_keyboard.add_line()
#         subjects_keyboard.add_callback_button("Правоведение", payload={"payload": "/pravo"})
#         subjects_keyboard.add_callback_button("Программирование", payload={"payload": "/proga"})
#         subjects_keyboard.add_line()
#         subjects_keyboard.add_callback_button("ТРИР", payload={"payload": "/trir"})
#         subjects_keyboard.add_callback_button("Физика", payload={"payload": "/phisic"})
#         subjects_keyboard.add_line()
#         subjects_keyboard.add_callback_button("Назад", payload={"payload": "/menu"})
#         return subjects_keyboard.get_keyboard()
#
#     @staticmethod
#     def get_admin_keyboard():
#         keyboard = VkKeyboard()
#         keyboard.add_button("get admins")
#         # keyboard.add_button("add admin") TODO: сохрнаять последнее сообщение и добавлять админа и следующего сообщения
#         return keyboard.get_keyboard()
#         # TODO: Дописать
#
#
# # token = cfg.get('vk', 'token')
# # vk = vk_api.VkApi(token=token).get_api()
#
#
# class Rights:
#     user = dict(get_homework_and_timetable=True)
#     elder = user.copy()
#     elder.update(dict(work_with_homework_and_timetable=True, set_elder=True))
#     admin = elder.copy()
#     elder.update(dict(set_admin=True))
#
#
# class Bot:
#     keyboard = Keyboards.get_keyboard()
#     menu = Keyboards.get_menu()
#     subjects_keyboard = Keyboards.get_subjects_keyboard()
#     admin_keyboard = Keyboards.get_admin_keyboard()
#     # group_id = cfg.get("vk", "group")
#     all_impossible_types_subject = [PRACTICE, THEORY, "практика", "лекция", "лек", "прак", "пр", "лк"]
#
#     # для translate
#     rus = "абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
#     eng = r"f,dult`;pbqrkvyjghcnea[wxioms]'.zF<DULT~:PBQRKVYJGHCNEA{WXIOMS}" + '"' + ">Z"
#     rus_eng = {str("f,dult`;pbqrkvyjghcnea[wxioms]'.zF<DULT~:PBQRKVYJGHCNEA{WXIOMS}" + '"' + ">Z")[i]: "абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"[i] for i in range(len(rus))}
#
#     @staticmethod
#     def translate(s):
#         new_s = ""
#         for i in s:
#             if i in Bot.rus_eng:
#                 new_s += Bot.rus_eng[i]
#             else:
#                 new_s += i
#         return new_s
#     @staticmethod
#     def reply(**kwargs):
#         general = dict(random_id=random.randint(0, 343439483948), keyboard=Keyboards.get_keyboard())
#         general.update(kwargs)
#         return vk.messages.send(**general)
#
#     @staticmethod
#     def reply_with_event(peer_id, event_id, user_id, text):
#         return vk.messages.sendMessageEventAnswer(peer_id=peer_id, event_id=event_id, user_id=user_id,
#                                                   event_data=json.dumps(
#                                                       {"type": "show_snackbar", "text": text}))
#
#     @staticmethod
#     def get_last_message(peer_id):
#         print(peer_id)
#         return [item["id"] for item in vk.messages.getHistory(count=1, peer_id=peer_id) if
#                 item["from_id"] == -Bot.group_id]
#
#     @staticmethod
#     def delete_messages(ids, t=15):
#         print(ids, 112)
#         print("поток заснул")
#         tm.sleep(t)
#         print("поток проснулся")
#         vk.messages.delete(message_ids=ids, delete_for_all=True, group_id=Bot.group_id)
#         print(f"удалил {ids}")
#
#     @staticmethod
#     def notification(user_id):
#         result = set_notification(user_id)
#         if result:
#             message = "Уведомления включены\nТеперь каждое утро ты будешь получать расписание на день"
#         else:
#             message = "Уведомления выключены"
#         return message
#
#     @staticmethod
#     def get_id_on_link(link):
#         if type(link) == int:
#             return link
#         if link.isdigit():
#             return int(link)
#         if "@" in link:
#             link = link.replace("@", '')
#         if link.startswith("http"):
#             link = link.split("://vk.com/")[1]
#         if link[2:].isdigit() and link[:2] == "id":
#             return int(link[2:])
#         else:
#             try:
#                 user_id = vk.utils.resolveScreenName(screen_name=link)['object_id']
#                 return int(user_id)
#             except Exception as e:
#                 print("произошла какая-то ошибка при выяснении id пользователя", e)
#         return None
#
#     @staticmethod
#     def parse_date(word):
#         """можно пропарсить дату -> возвращает объект date
#         если нельзя возращает None
#
#         дата
#         5
#         05
#         05.04
#         05.4
#         05.4.21
#         05.4.2021
#         проверять существует ли дата
#
#         """
#         pass
#
#     @staticmethod
#     def parse_subject(word, type_=None):
#         """можно пропарсить предмет -> возвращает объект (<предмет>, <тип_предмета>) или None
#         предмет
#         предмет из бд
#         type_ in [PRACTICE, THEORY, "практика", "лекция", "лек", "прак", "пр", "лк"]
#         проверять существует ли предмет
#         возвращает None если предмета нет в базе данных или же предмет не предмет :)
#         если предмет существует в базе данных но type_ == None то возвращает кортеж (subject, PRACTICE)
#         примечаение: если у предмета отсутсвует практика, то вовзращает тип следущий по приоритности
#         if type_: return (subject, type_)
#         """
#         # TODO: добавит список приоритетности типов предметов 1) практика 2)лекция 3)семинар
#         # TODO: создать глобальный список со всеми типами предметов которые возможно введет пользователь
#         pass
#
#     @staticmethod
#     def parse_text(text: list, type_=None):
#         text = ' '.join([text[i] for i in range(4) if text[i] and
#                 not Bot.parse_date(text[i]) and not text[i] not in Bot.all_impossible_types_subject and
#                 not Subject.exists(name=text[i])] + text[4:])
#         return text
#
#     @staticmethod
#     def administrating(command, user_id, peer_id):
#         successful_setting_marker = False
#         base_msg = dict(user_id=user_id, peer_id=peer_id)
#         # настройка старостой/админом типа беседы
#         if "/set_conv" in command:
#             command, name = command.split()
#             if user_id in [i.user_id for i in User.select() if
#                            i.rank.name in ["admin", "elder"]] and peer_id != user_id:
#                 add_conversation(peer_id, name)
#                 base_msg.update(message=f"Беседа объявлена как {name}")
#                 successful_setting_marker = True
#         # если пишет в беседе для настройки бота админ или староста, то перейти в функцию настройки бота
#         # if peer_id in get_conversaton("setting") and user_id in [i.user_id for i in User.select() if
#         #                                                          i.rank.name in ["admin",
#         #                                                                          "elder"] and i.group.name == STUDY_GROUP]:
#         #     if Bot.settings_bot(command, dict(peer_id=peer_id)):
#         #         successful_setting_marker = True
#         # если сообщение пришло в лс
#         if user_id == peer_id:
#             # настройка бота админом
#             if Bot.admin_settings(command, dict(peer_id=peer_id, user_id=user_id)):
#                 successful_setting_marker = True
#         return successful_setting_marker
#
#     # TODO: ПРОЧИТАТЬ ДОКУМНЕТАЦИЮ ПО ПОНИ!!!
#     @staticmethod
#     @db_session
#     def homework(text: str, base_msg: dict):
#         command, *params = text.split(" ")
#         different_subject = False
#         print(command)
#         # /добавить_дз математика 22.03.2021 номер раз два три елочка гори
#         # /добавить_дз математика лк. 22.03.2021 номер раз два три елочка гори
#         # /добавить_дз математика лек 22.03.2021 номер раз два три елочка гори
#         # /добавить_дз физика лек 22.03.2021 номер раз два три елочка гори
#         # /получить_дз дата
#         # /получить_дз предмет -> возращает и по лекции и по практике
#         # /получить_дз предмет дата - если есть и лекция и практика в этот день то возратить все дз по этому предмету
#         # TODO: /изменить_дз предмет тип дата
#         if command in ["/добавить_дз", "/изменить_дз", "/получить_дз", "/удалить_дз"]:
#             # date_ = Bot.parse_date(params[0]) or Bot.parse_date(params[1]) or Bot.parse_date(params[2])
#             # subject = Bot.parse_subject(*params[0:2])  # (<предмет>, <тип_предмета>) или None
#             # text = Bot.parse_text(params) # TODO: реализовать домашку нормально
#             print(command)
#             subject = params[0]
#             if subject == "физика" or params[1] in [PRACTICE, THEORY, "практика", "лекция", "лек", "прак"]:
#                 different_subject = True
#                 subject_type = params[1]
#                 if subject_type in ["практика", "прак"]:
#                     subject_type = PRACTICE
#                 elif subject_type in ["лекция", "лек"]:
#                     subject_type = THEORY
#                 d = params[2]
#             else:
#                 subject_type = PRACTICE
#                 d = params[1]
#             d = d.replace(" ", '')
#             d = tuple(map(int, d.split(".")))
#             subject = subject.replace(" ", '')
#             subject = subject.title()
#             subject = subject, subject_type
#             if command in ["/добавить_дз", "/изменить_дз"]:
#                 if not User[base_msg["user_id"]].in_black_list:
#                     if different_subject:
#                         home_task = params[3]
#                     else:
#                         home_task = params[2]
#                     params = [subject, home_task, date(d[2], d[1], d[0])]
#                     if command == "/добавить_дз":
#                         if "fwd_messages" in base_msg.keys():
#                             params.append(base_msg["fwd_messages"])
#                         add_home_task(*params)
#                         base_msg.update(dict(
#                             message=f"""Добавил дз {subject[0]} {subject[1]}{params[2].day}.{'0' + str(params[2].month)
#                             if len(str(params[2].month)) == 1 else params[2].month}.{params[2].year}"""))
#                     # elif command == "/изменить_дз":
#                     #     change_homework_on_day(*params)
#                     #     base_msg.update(dict(
#                     #         message=f"Изменил дз {subject[0]} {subject[1]}{params[2].day}.{'0' + str(params[2].month) if len(str(params[2].month)) == 1 else params[2].month}.{params[2].year}"))
#                 elif command == "/получить_дз":
#                     home_task = get_home_task(subject, date(d[2], d[1], d[0]))
#                     base_msg.update(dict(message=home_task))
#                 elif command == "/удалить_дз":
#                     print("удалил")
#                     home_task = delete_home_task_from_subject_date(subject, date(d[2], d[1], d[0]))
#                     params = [subject, date(d[2], d[1], d[0])]
#
#                     print(subject, params)
#                     base_msg.update(dict(
#                         message=f"Удалил дз {subject[0]} {subject[1]}{params[1].day}.{'0' + str(params[1].month) if len(str(params[1].month)) == 1 else params[1].month}.{params[1].year}"))
#             if "user_id" in base_msg:
#                 base_msg.pop("user_id")
#             Bot.reply(**base_msg)
#             return True
#         return False
#
#     # @staticmethod
#     # @db_session
#     # def settings_bot(command: str, base_msg: dict):
#     #     admins = [i.user_id for i in User.select() if i.rank.name == "admin"]
#     #     elders = [i.user_id for i in User.select() if i.rank.name == "elder"]
#     #     admins_elders = admins + elders
#     #     if base_msg["user_id"] in admins_elders:
#     #
#
#     @staticmethod
#     @db_session
#     def admin_settings(command: str, base_msg: dict):
#         if not command.startswith(("add admins", "get admins")):
#             return False
#         user_id = base_msg["user_id"]
#         peer_id = base_msg["peer_id"]
#         msg_from = (user_id, peer_id)
#         admins = [i.user_id for i in User.select() if i.rank.name == "admin" and i.group.name == STUDY_GROUP]
#         print(admins, user_id)
#         if user_id in admins:
#             admin = User[user_id]
#             print(admin.last_messages)
#             if command.startswith("add admins"):
#                 params = command.lstrip("add admins").split()
#                 to_add_admins = [Bot.get_id_on_link(i) for i in params]
#                 if not set(to_add_admins).issubset(admins):
#                     added_admins = [str(add_user_rank(Bot.get_id_on_link(i), "admin", user_id, Bot)) for i in params]
#                     print(added_admins)
#                     base_msg.update(dict(message=', '.join(
#                         list(map(lambda i: 'https://vk.com/id' + str(i), added_admins))) + " добавлены в админы"))
#                 else:
#                     base_msg.update(dict(message="такие пользователи уже админы"))
#             if command.startswith("get admins"):
#                 base_msg.update(dict(message=', '.join(list(map(lambda i: 'https://vk.com/id' + str(i), admins)))))
#
#             print(base_msg)
#             if "message" in base_msg:
#                 Bot.reply(**base_msg)
#                 return True
#             return False
#
#     @staticmethod
#     @db_session
#     def msg_processing(data):
#         type_ = data["type"]
#         if type_ == 'confirmation':
#             return cfg.get('vk', 'confirmation')
#         elif type_ == "message_new":
#             message = data["object"]["message"]
#             print(message["id"], 199)
#             try:
#                 Bot.delete_messages([message["id"]], 0)
#             except Exception as e:
#                 print(e)
#             user_id = message["from_id"]
#             peer_id = message["peer_id"]
#             fwd_messages = [i["id"] for i in message["fwd_messages"]]
#             base_msg = dict(peer_id=peer_id, keyboard=Bot.keyboard)
#             print("message_new")
#             text = message["text"]
#             # отлавливание сообщения с упоминананием
#             if "] " in text:
#                 text = text.split("] ")[1]
#                 print(text)
#             command = text
#             send_method = Bot.reply
#         elif type_ == "message_event":
#             peer_id = data["object"]["peer_id"]
#             user_id = data["object"]["user_id"]
#             payload = data["object"]["payload"]
#             if payload:
#                 payload = payload["payload"]
#                 command = payload
#             event_id = data["object"]["event_id"]
#             base_msg = dict(peer_id=peer_id, event_id=event_id, user_id=user_id)
#             send_method = Bot.reply_with_event
#         if "command" in locals():
#             print(command)
#         else:
#             return "ok"
#         # /translate
#         if command.lower().startswith("/translate"):
#             _, s = command.lower().split("/translate")
#             base_msg.update(dict(message=f"{s} = {Bot.translate(s)}"))
#         one_word_commands = [
#             {("/start", "начать"): dict(msg_text_fnctn=lambda: get_phrase("start"))},
#             {("/menu", "меню"): dict(msg_text_fnctn=lambda: "Главное меню", keyboard=Bot.menu)},
#             {(
#                 "/current_timetable", "/расписание", "бот расписание", "бот, расписание",
#                 "бот скинь расписание на сегодня",
#                 "бот, скинь расписание на сегодня",): dict(
#                 msg_text_fnctn=lambda: get_current_timetable())},
#             {("/today", "бот расписание на сегодня", "бот, расписание на сегодня", "бот скинь расписание на сегодня",
#               "бот, скинь расписание на сегодня",): dict(
#                 msg_text_fnctn=lambda: get_timetable_day(datetime.today().date()))},
#             {("/tomorrow", "бот расписание на завтра", "бот, расписание на завтра", "бот скинь расписание на завтра",
#               "бот, скинь расписание на завтра",): dict(
#                 msg_text_fnctn=lambda: get_timetable_day((datetime.today() + dt.timedelta(days=1)).date()))},
#             {("/week", "бот расписание на неделю", "бот, расписание на неделю", "бот скинь расписание на неделю",
#               "бот, скинь расписание на неделю",): dict(msg_text_fnctn=lambda: get_timetable_week())},
#             {("/timetable", "бот расписание пар", "бот, расписание пар", "бот скинь расписание пар",
#               "бот, скинь расписание пар",): dict(msg_text_fnctn=lambda: get_phrase("timetable"))},
#             {("/teachers", "бот преподы", "бот, преподы",): dict(msg_text_fnctn=lambda: "Выберете предмет",
#                                                                  keyboard=Bot.subjects_keyboard)},
#             {("/english", "бот английский преподы", "бот преподы английский", "бот, английский преподы",
#               "бот, преподы английский"): dict(
#                 msg_text_fnctn=lambda: get_teachers("Английский 1") + get_teachers("Английский 2"))},
#             {("/itvpd", "бот итвпд преподы", "бот преподы итвпд", "бот, ивпд преподы", "бот, преподы итвпд"): dict(
#                 msg_text_fnctn=lambda: get_teachers("ИТвПД"))},
#             {("/math", "бот математика преподы", "бот преподы математика", "бот, математика преподы",
#               "бот, преподы математика"): dict(msg_text_fnctn=lambda: get_teachers("Математика"))},
#             {("/mlita", "бот млита преподы", "бот преподы млита", "бот, млита преподы", "бот, преподы млита"): dict(
#                 msg_text_fnctn=lambda: get_teachers("МЛиТА"))},
#             {("/pravo", "бот право преподы", "бот преподы право", "бот, право преподы", "бот, преподы право"): dict(
#                 msg_text_fnctn=lambda: get_teachers("Правоведение"))},
#             {("/proga", "бот прога преподы", "бот преподы прога", "бот, прога преподы", "бот, преподы прога"): dict(
#                 msg_text_fnctn=lambda: get_teachers("Программирование"))},
#             {("/trir", "бот трир преподы", "бот преподы трир", "бот, трир преподы", "бот, преподы трир"): dict(
#                 msg_text_fnctn=lambda: get_teachers("ТРИР"))},
#             {(
#                 "/phisic", "бот физика преподы", "бот преподы физика", "бот, физика преподы",
#                 "бот, преподы физика"): dict(
#                 msg_text_fnctn=lambda: get_teachers("Физика"))},
#             {("/notification", "бот уведомления"): dict(
#                 msg_text_fnctn=lambda: Bot.notification(user_id))},
#             {("/help", "бот помощь", "бот команды", "бот, помощь", "бот, команды"): dict(
#                 msg_text_fnctn=lambda: get_phrase("/help"))}
#         ]
#         add_user(user_id)  # добавляет пользователя, если его еще нет в базе данных
#         # работа с домашкой
#         base = dict(peer_id=peer_id, user_id=user_id)
#         if "fwd_messages" in locals():
#             base.update(dict(fwd_messages=fwd_messages))
#         if Bot.homework(command, base):
#             return "ok"
#         # TODO: добавить команду занять очередь\выбрать тему
#         # администрирование
#         if Bot.administrating(command, user_id, peer_id):
#             return "ok"
#         # обычные команды
#         for commands in one_word_commands:
#             for excpected_command_list, d, in commands.items():
#                 if command.lower() in excpected_command_list:
#                     message = d["msg_text_fnctn"]()
#                     d.pop("msg_text_fnctn")
#                     if len(message) < 10:
#                         message += " ничего)"
#                     elif len(message) > 70 or "keyboard" in d.keys():
#                         if send_method == Bot.reply_with_event:
#                             print(event_id)
#                             Bot.reply_with_event(peer_id=peer_id, user_id=user_id, event_id=event_id,
#                                                  text="Сообщение слишком велико для всплывающего уведомления.\nОтправляю обычное сообщение")
#                         send_method = Bot.reply
#                     if send_method == Bot.reply:
#                         base_msg.update({"message": message})
#                         if "user_id" in base_msg.keys():
#                             base_msg.pop("user_id")
#                             base_msg.pop("event_id")
#                     elif send_method == Bot.reply_with_event:
#                         base_msg.update({"text": message})
#                     base_msg.update(d)
#                     break
#
#         if "text" in base_msg.keys() or "message" in base_msg.keys():
#             print(base_msg, send_method)
#             id_ = send_method(**base_msg)
#             print(id_)
#             if "message" in base_msg.keys(): Thread(target=lambda: Bot.delete_messages([id_])).start()
#         return "ok"