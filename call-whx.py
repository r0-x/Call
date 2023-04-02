import os
os.system("pip install pyTelegramBotAPI")
import telebot
token = "5697360861:AAHaKeaVQNl1-Bt0z66LyfU2czSUbBuW5BE"
bot = telebot.TeleBot(token)
print("running")
@bot.message_handler(commands =["start"])
def starts(message):
    file ="https://t.me/gsvsvsvsc/3"
    bot.send_document(message.chat.id,file)
bot.infinity_polling()
