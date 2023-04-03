
import telebot
token = "5697360861:AAFnoM95q3kzaYAJw0XVRaHiNGgTZpbJFGM"
bot = telebot.TeleBot(token)
print("running")
@bot.message_handler(commands =["start"])
def starts(message):
    file ="https://t.me/gsvsvsvsc/3"
    bot.send_document(message.chat.id,file)
bot.infinity_polling()
