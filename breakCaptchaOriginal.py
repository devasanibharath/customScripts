#!/usr/bin/python

# @author t1nyb0y
# Break captcha and submit form data

from PIL import Image
import urllib, os , re, time, sys
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup


URL_SUBMIT="https://istrac.remotexs.in/user/login"
URL_HOME="https://istrac.remotexs.in/user/login"
BASE_URL="https://istrac.remotexs.in"

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))


# Fetch Session Parameters

resp = opener.open(URL_HOME)
content = resp.read()

#print (content)

soup = BeautifulSoup(content, 'html.parser')
form = soup.find('form', id='user-login')

#print (form.prettify())

URL_CAPTCHA = BASE_URL + form.find('img').get('src').split('&')[0]

captcha = 'captcha.jpg'

f_captcha = opener.open(URL_CAPTCHA)
data_captcha = f_captcha.read()
f_captcha.close()

with open(captcha, 'wb') as data:
    data.write(data_captcha)


picture = Image.open(captcha)
black = (0,0,0)
white = (255,255,255)

width, height = picture.size

for x in range(0,width):
	for y in range(0,height):
		r,g,b = picture.getpixel( (x,y) )
		if r is 0 and g is 0 and b is 255: # blue
			picture.putpixel( (x,y), white)
		elif r is 64 and g is 64 and b is 64: # gray
			picture.putpixel( (x,y), white)
		elif r is 0 and g is 0 and b is 0: # black
			picture.putpixel( (x,y), white)
		elif r is 122 and g is 111 and b is 255: # text
			picture.putpixel( (x,y), black)
		else:
			pass

resize = 2

picture = picture.resize((int(width*resize), int(height*resize)), Image.ANTIALIAS) # BICUBIC is awesome
picture.save('result.png')


os.system('convert -median 4 result.png result.tif')
os.system('tesseract -l eng -psm 8 result.tif result 2>/dev/null')

#print(URL_CAPTCHA)

f = open('result.txt','r')
val = f.read().replace("\n", "").replace(" ","")
print 'raw: ',val
f.close()

# 4.1 manual tuning
# problem: see 'y' as 'g', see 'A' as 'Q', see 'y' as 'U'
val = val.replace('1:.','t')
val = val.replace('l\'1','M')

if len(val) > 6: # error corrections
	val = val.replace('l-J','W')
	val = val.replace('l~J','W')
	val = val.replace('l-I','W')
	val = val.replace('I-J','W')
	val = val.replace('I~J','W')
	val = val.replace('l-l','W')
	val = val.replace('lsl','W')
	val = val.replace('luJ','W')

	val = val.replace('T\'1','M')
	val = val.replace('r\'1','M')
	val = val.replace('I\'1','M')
	val = val.replace('I-‘','f')
	val = val.replace('Pl','M')
	val = val.replace('P1','M')
	val = val.replace('<F','f')
	val = val.replace('ﬂ','M')
	val = val.replace('F‘','f')
	val = val.replace('{‘','f')
	val = val.replace('¥‘','f')
	val = val.replace('r‘','r')
	val = val.replace('Cl','q')
	val = val.replace('C1','q')
	val = val.replace('CI','q')
	val = val.replace('c1','q')
	val = val.replace('cI','q')
	val = val.replace('cl','q')
	val = val.replace(']-','j')
	val = val.replace(')(','X')
	val = val.replace('\\/','v')
	val = val.replace('ld','W')
	val = val.replace('“','W')
	val = val.replace('8\'','g')
	val = val.replace('ﬁ','A')

val = val.replace('1','l')
val = val.replace('2','Z')
val = val.replace('5','S')
val = val.replace('8','g')
val = val.replace('0','O') # Q
val = val.replace('/','g')
val = val.replace('-','a')
val = val.replace('\\','j')

val = ''.join(re.findall("[a-zA-Z0-9]+", val))
print ('submit: ',val)
