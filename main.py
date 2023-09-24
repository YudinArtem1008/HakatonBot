import telebot
import os

token = "5953953594:AAGBxi382uvtPM682uSuIj_CJ_uDCoJWSD4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Я - телеграмм бот, определяющий детали по фотографии для "
                                      "предприятия Koblik по фотографии. Чтобы это сделать, "
                                      "отправь мне фотографию детали")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Привет. Я - телеграмм бот, определяющий детали по фотографии для "
                                      "предприятия Koblik по фотографии. Чтобы это сделать, "
                                      "отправь мне фотографию детали.")
    bot.send_message(message.chat.id, "Детали, которые наш сервис умеет распознавать:\n"
                                      "1) CS120.01.413\n"
                                      "2) CS120.07.442\n"
                                      "3) CS150.01.427-01\n"
                                      "4) SU160.00.404\n"
                                      "5) SU80.01.426\n"
                                      "6) SU80.10.409A\n"
                                      "7) 3BT86.103K-02\n"
                                      "8) CBM.37.060\n"
                                      "9) CBM.37.060A\n"
                                      "10) СВП-120.00.060\n"
                                      "11) СВП120.42.020\n"
                                      "12) СВП120.42.030\n"
                                      "13) CK20.01.01.01.406\n"
                                      "14) CK20.01.01.02.402\n"
                                      "15) CK30.01.01.02.402\n"
                                      "16) CK30.01.01.03.403\n"
                                      "17) CK50.01.01.404\n"
                                      "18) CK50.02.01.411\n"
                                      "19) СПО250.14.190\n")


@bot.message_handler(content_types=['photo'])
def recognition(message):
    photo = message.photo[-1]
    res = sending_to_the_server(photo)
    bot.send_message(message.chat.id, f"Я отправил на опознание деталь. Результат: {res}. Если надо ещё отправить "
                                      f"детали на опознание - отправь мне фотографию детали")


def sending_to_the_server(image):
    file_id = str(image.file_id)
    file_name = os.path.join("server", file_id + ".jpg")
    file_info = bot.get_file(image.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    res = None
    return res


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
