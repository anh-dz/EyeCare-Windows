from base64 import b64decode
from os import path, remove, getlogin, makedirs

user = getlogin()

if not path.exists(f"C://Users//{user}//AppData//Roaming//EyeCare"):
    makedirs(f"C://Users//{user}//AppData//Roaming//EyeCare")

def decode_(encode_f):
	decode_f = list(b64decode(encode_f).decode("utf-8"))

	for i, j in enumerate(decode_f):
		if not j.isnumeric():
			decode_f[i] = None
	
	string_decode = ""
	temp = ""
	for i in decode_f:
		if i != None:
			temp+=i
		else:
			if temp.replace(' ', '') != '':
				temp_ = int(temp)-10
				string_decode+=chr(temp_)
				temp = ""
	return string_decode.split('\n')

def open_un():
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//un.set', 'rb') as f:
			lget = decode_(f.readline())
			shortcut, lang = lget[0].replace('\n', ''), int(lget[1].replace('\n', ''))
	except:
		shortcut = 'Ctrl+Alt'
		lang = 0
	return shortcut, lang

def open_data():
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//data.set', 'rb') as f:
			temp = decode_(f.readline())
			temp = [i.split(' ') for i in temp]
			_time, _data = [], []
			for i in temp:
				_data.append(i[0])
				_time.append(float(i[1]))
	except:
		_data, _time = None, None
	return _data, _time

def open_time():
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//time.set', 'rb') as f:
			_time = decode_(f.readline())
			_time = [i.split() for i in _time]
	except:
		_time = [['00', '20', '00'], ['00', '00', '20']]
	return _time

def open_setting():
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//setting.set', 'rb') as f:
			temp = decode_(f.readline())
			_setting = temp[0].split()
			_setting = [int(i) for i in _setting]
			if len(temp)>1:
				_pass = temp[1]
	except:
		_setting, _pass = [0, 1, 1, 2, 0], 'eyecare'
	return _setting, _pass

def open_sleep():
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//sleep.set', 'r') as f:
			temp = decode_(f.readline())
			temp = temp[0].split(' ')
			_time_sleep = [[temp[0], temp[1]], [temp[2], temp[3]]]
			_setting_sleep = [int(temp[4]), int(temp[5]), int(temp[6])]
	except:
		_time_sleep, _setting_sleep = [['06', '00'], ['10', '00']], [0, 0, 1]
	return _time_sleep, _setting_sleep

def open_sleep_data():
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//sleep_data.set', 'rb') as f:
			temp = decode_(f.readline())
			sleep_data = temp[0].split(' ')
			sleep_data = sleep_data[len(sleep_data)-7:]
	except:
		sleep_data = []
	return sleep_data

def open_det():
	shortcut, lang = open_un()
	try:
		with open(f'C://Users//{user}//AppData//Roaming//EyeCare//det.set', 'rb') as f:
			det = decode_(f.readline())
			det = [i.strip() for i in det]
			if det[1] == "Stand up and take a break!!!" or det[1] == ["Tạm dừng công viêc lại và nghỉ ngơi một lúc nào!"]:
				if lang == 0:
					det[1] = "Stand up and take a break!!!"
				else:
					det[1] = "Tạm dừng công viêc lại và nghỉ ngơi một lúc nào!"
	except:
		if lang == 0:
			det = ["C:/", "Stand up and take a break!!!"]
		else:
			det = ["C:/", "Tạm dừng công viêc lại và nghỉ ngơi một lúc"]
	return det

def delete_file(file):
	if path.exists(f'C://Users//{user}//AppData//Roaming//{file}'):
		remove(f'C://Users//{user}//AppData//Roaming//{file}')
