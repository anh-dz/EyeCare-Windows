import random
from base64 import b64encode

def encode_(string_encode):
	string_temp = ""
	for i in string_encode:
		string_temp += str(ord(i)+10)
		for i in range(random.randint(1,3)):
			string_temp += random.choice('EyeCareENcOdeD')

	return b64encode(string_temp.encode("utf-8"))

def write_two_file(user, file, st1, st2):
	with open(f'C://Users//{user}//AppData//Roaming//EyeCare//{file}.set', 'wb') as f:
		f.write(encode_(f"{st1}\n{st2}"))

def write_data(user, days, data):
	st = ""
	for i, j in zip(days, data):
		st += (i+' '+j+'\n')
	st = st[:len(st)-1]
	with open(f'C://Users//{user}//AppData//Roaming//EyeCare//data.set', 'wb') as f:
		f.write(encode_(st))

def write_chart_file(location, st):
	with open(location, 'w', encoding='utf-8') as f:
		f.write(st)

def write_sleep_data(user, file, lis):
	with open(f'C://Users//{user}//AppData//Roaming//EyeCare//{file}.set', 'wb') as f:
		f.write(encode_(" ".join(lis)))