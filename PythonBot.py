import telebot;

bot = telebot.TeleBot('1859290083:AAFeWwyUYYrHp6Rxb_zYX6A7PhBrarO5Qy4');

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

        if message.text == "Привет":
              bot.send_message(message.from_user.id, "Привет")
        elif message.text == "Кто ты?":
              bot.send_message(message.from_user.id, "Я тестовый чатбот для учебного примера.")
        elif message.text == "Как тебя зовут?":
              bot.send_message(message.from_user.id, "Меня зовут Bot.")
        else:
              bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши что-то другое.")

bot.polling(none_stop=True, interval=0)