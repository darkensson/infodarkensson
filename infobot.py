#tokken: 1061765774:AAEnTsBD0DRh21D3sYlbHLQevKHjKJ5BVdM
import telebot
from telebot.types import Message




TOKEN = '865916092:AAH1iWxjRCHoY8vc7fiCuwZSiVcMzGHFzn8'

bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Найди одноклассника(одногруппника) 😄')


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, 'С кем учился с 1 по 9 класс')	


#Коля
@bot.message_handler(regexp="коля")
@bot.message_handler(regexp="никол")
@bot.message_handler(regexp="пес")
def handle_message(message):
	photo = open('photo/kolya.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/vky96')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/vky96')


#Мирослав
@bot.message_handler(regexp="миросл")
@bot.message_handler(regexp="матыл")
@bot.message_handler(regexp="мотыл")
def handle_message(message):
	photo = open('photo/mir.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id248493275')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id248493275')


#Архип
@bot.message_handler(regexp="архип")
@bot.message_handler(regexp="анто")
def handle_message(message):
	photo = open('photo/arh.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id186287106')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id186287106')


#Гера
@bot.message_handler(regexp="герма")
@bot.message_handler(regexp="аста")
@bot.message_handler(regexp="гера")
def handle_message(message):
	photo = open('photo/gera.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/astap_g')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/astap_g')


#Соня
@bot.message_handler(regexp="соня")
@bot.message_handler(regexp="софья")
@bot.message_handler(regexp="колдор")
def handle_message(message):
	photo = open('photo/sonya.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id137993867')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id137993867')


#Игорь
@bot.message_handler(regexp="игорь")
@bot.message_handler(regexp="танаг")
def handle_message(message):
	photo = open('photo/igor.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/igr_tng')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/igr_tng')

#Некит
@bot.message_handler(regexp="чж")
@bot.message_handler(regexp="некит")
@bot.message_handler(regexp="никит")
def handle_message(message):
	photo = open('photo/nekit.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/nekitazhao')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/nekitazhao')


#Артем
@bot.message_handler(regexp="артем")
@bot.message_handler(regexp="мочал")
def handle_message(message):
	photo = open('photo/artem.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/temamochalov')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/temamochalov')


#Алена
@bot.message_handler(regexp="ален")
@bot.message_handler(regexp="гулим")
def handle_message(message):
	photo = open('photo/alena.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id171454612')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id171454612')


#Конопленко
@bot.message_handler(regexp="алин")
@bot.message_handler(regexp="конопл")
def handle_message(message):
	photo = open('photo/alina.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id168970759')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id168970759')


#Машраб
@bot.message_handler(regexp="машр")
@bot.message_handler(regexp="ахма")
def handle_message(message):
	photo = open('photo/mashrab.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id314553215')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id314553215')


#Макеев
@bot.message_handler(regexp="макее")
@bot.message_handler(regexp="дима")
@bot.message_handler(regexp="дмит")
@bot.message_handler(regexp="макеша")
def handle_message(message):
	photo = open('photo/dima.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id193289545')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id193289545')


#Могилевец
@bot.message_handler(regexp="ваня")
@bot.message_handler(regexp="иван")
@bot.message_handler(regexp="могил")
@bot.message_handler(regexp="могел")
def handle_message(message):
	photo = open('photo/vanya.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/ivan_mogilevec')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/ivan_mogilevec')


#Катя Андреева
@bot.message_handler(regexp="андре")
def handle_message(message):
	photo = open('photo/andreeva.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id404808913')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id404808913')


#Катя Яблонская
@bot.message_handler(regexp="яблонс")
def handle_message(message):
	photo = open('photo/yabl.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id482067881')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id482067881')


#Даша
@bot.message_handler(regexp="доро")
@bot.message_handler(regexp="даша")
@bot.message_handler(regexp="дарья")
def handle_message(message):
	photo = open('photo/dasha.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id163148142')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id163148142')


#Власова
@bot.message_handler(regexp="власова")
def handle_message(message):
	photo = open('photo/dasha.jpg', 'rb')
	if message.from_user.id == 456193135:
		bot.send_photo(456193135, photo)
		bot.send_message(456193135, 'https://vk.com/id163148142')
	else:
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, 'https://vk.com/id163148142')


#Кати
@bot.message_handler(regexp="Катя")
@bot.message_handler(regexp="Екатер")
def handle_message(message):
	if message.from_user.id == 456193135:
		bot.send_message(456193135, 'Фамилия?')
	else:
		bot.send_message(message.chat.id, 'Фамилия?')


@bot.message_handler(func=lambda message: True)
def upper(message):
	if message.from_user.id == 456193135:
		bot.send_message(456193135, 'ты админ')
	else:
		bot.send_message(message.chat.id, 'нет такого васичка')




bot.polling()