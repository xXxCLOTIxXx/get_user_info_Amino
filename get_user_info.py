import os, time
time.sleep(1)
print("\n\n\nСкрипт запущен на телефоне, или на пк?")
while True:
	g = input("телефон (1), Компьютер (2)>> ")
	if g == "1":
		clear = "clear"
		break
	elif g == "2":
		clear = "cls"
		break
	else:
		print("\n\nНе верный ответ, выберите 1, или 2\n\n")
os.system(clear)

try:
	import aminofix
except:
	os.system("pip install amino.fix")
	import aminofix

try:
	from rich.console import Console
except:
	os.system("pip install rich")
	from rich.console import Console



import random, pyfiglet
import pyfiglet
from threading import Thread

client = aminofix.Client()
console = Console()
os.system(clear)
console.print("[magenta]" + pyfiglet.figlet_format("Amino-Info V2", font="slant") + "[/magenta]")
console.print("[bold cyan] made by CLOTI (Xsarz)[/] [bold yellow]Telegram: t.me/DXsarz    GITHUB: https://github.com/xXxCLOTIxXx[/]")
while True:
	try:
		client.login(email=input("\nПочта>> "), password=input("\nПароль>> "))
		break
	except Exception as ex:
		print("\n\n\nОшибка при входе в аккаунт\n\n\n")


while True:
	try:
			url = client.get_from_code(input("\nСсылка на пользователя>> ")).objectId
			g = client.get_user_info(userId=url).json
			console.print(f"\n\n[bold cyan]Имя: {g['nickname']}\nФото в глобальном профиле: {g['icon']}\nАмино айди: {g['aminoId']}\nДата регистрации: {g['createdTime']}\nАйди юзера: {g['uid']}[/]")
			break
	except:
		console.print('\n\n[bold red]Произошла ошибка[/]\n\n')