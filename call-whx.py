import telebot 
import requests

tok = "5697360861:AAHaKeaVQNl1-Bt0z66LyfU2czSUbBuW5BE"

bot = telebot.TeleBot(tok)

@bot.message_handler()

def starts(message):
	
	id = int(message.chat.id)
	ch = "Professional_school"
	if  int((id)):
		ch = "Professional_school"
		url =f"https://api.telegram.org/bot{tok}/getChatMember?chat_id=@Professional_school&user_id={id}"
		
		x = requests.get(url).text
		
		if x.count("left") or x.count("Bad Request: user not found"):			
			print("not join")
			bot.send_message(message.chat.id,text=f" ** الرجاء الاشتراك لتفعيل البوت \n @[Professional_school]** ",parse_mode ="markdown")
		else:
			if message.text.isnumeric():
				url = f"https://7amodytools.mahmoidayman.repl.co/Spam-Call/?phone={message.text}"
				x = requests.get(url).json()
				res = x['result']
				if res =="sent":
					bot.send_message(message.chat.id,text =f"تم الاتصال تابعنا هنا @{ch}")
				elif res =="Phone number limit reached":
					bot.send_messagw(message.chat.id,text =f" كثير من المحاولات جرب غير رقم. \n @Professional_school")
				elif res =="not sent":
					bot.send_message(message.chat.id,text =f"لم يتم الاتصال حدث خطأ في الرقم. \n @{ch}")
			else:
				bot.send_message(message.chat.id,"اهلا بك في يوت الاتصال المتكرر ارسل رقم الهاتف مع رقم الدولة بدون + . \n welcome in bot spam call send number without + just number and code of country \n مثال | Ex.  : 964771*****  ")
		
bot.polling()