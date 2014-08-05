# coding = utf-8
import time
import urllib2
import json
import os
import sys
import socket

citydict = {}

class GetWeather():
	def __init__(self):
		pass
	
	def get_weather(self, city):
		socket.setdefaulttimeout(9.0)
		if city in citydict.keys():
			id = citydict[city]
		if id:
			urlpath = 'http://www.weather.com.cn/data/cityinfo/' + id + '.html'
		try:
			weatherHtml = urllib2.urlopen(urlpath).read()
			weatherJSON = json.JSONDecoder().decode(weatherHtml)
		except:
			print "the web connecting or json decode error!"
			return -1
		weatherInfo = weatherJSON['weatherinfo']
		line_printer("Weather")
		print "\n"
		print 'city\t', weatherInfo['city']
		print 'highest temp\t',weatherInfo['temp1']
		print 'lowest temp\t',weatherInfo['temp2']
		print 'weather situation\t',weatherInfo['weather']	
		print "\n\n\n"
		return weatherInfo
	
class JumpHandler():
	def __init__(self, welcomPage, getWeather):
		self.welcompage = welcomPage
		self.getweather = getWeather
	def input_handle(self):
		input = raw_input("input your select:")
		update_console()
		if input == "1":
			line_printer('Curent Time')
			gettime = GetTime()
			print '\n'
			print gettime.get_current_time()
			print '\n\n\n'
			line_printer('-')
			self.welcompage.cont_page()
			self.input_handle()
		if input == "2":
			#open the city-id file
			dictpath = './dict.txt'
			with open(dictpath, 'r') as fp:
				for line in fp:
					try:
						cityname = line.split(' ')[0].decode('utf-8')
						citycode = line.split(' ')[1].decode('utf-8').strip('\n')
					except Exception:
						continue
					citydict[cityname] = citycode
					
			city = raw_input("please input a city:")
			if self.getweather.get_weather(city) == -1:
				return -1
			self.welcompage.cont_page()
			self.input_handle()
		else:
			self.welcompage.quit_page()
			exit(0)
		
class WelcomPage():
	def __init__(self):
		global input
		pass
		
	def start_page(self):
		print "Welcome to Visit AutoBot"
		print "\n\n"
		print "You can choose what to do:"
		print "1.Show current time"
		print "2.Show current weather of a city which city you want to know"
		print "3.quit"
		print "\n\n"

	def cont_page(self):
		print "You can choose what to do:"
		print "1.Show current time"
		print "2.Show current weather of a city which city you want to know"
		print "3.quit"

	def quit_page(self):
		print "Thanks for your using"
		print "Bye bye"
	

class GetTime():
	def __init__(self):
		pass
	
	def get_current_time(self):
		current_time = time.time()
		current_time = time.localtime(current_time)
		return time.strftime('%Y-%m-%d %H:%M:%S',current_time)

def line_printer(input):
	print '----------' + input + '----------'

		
def update_console():
	os.system('cls')
	

if __name__ == '__main__':
	welcomPage = WelcomPage()
	welcomPage.start_page()
	getWeather = GetWeather()
	handler = JumpHandler(welcomPage, getWeather)
	if handler.input_handle() == -1:
		exit(-1)
	exit(0)
