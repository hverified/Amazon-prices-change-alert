import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Test-Exclusive-611/dp/B07HGMLBW1/ref=sr_1_1?keywords=oneplus&qid=1564219280&s=gateway&sr=8-1'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'lxml')

def get_price():
	
	price = soup.find(id = 'priceblock_ourprice').text[2:8]
	convertedPrice = float(''.join(price.split(',')))

	return  convertedPrice

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('Senders Email address', 'password')

	subject = 'Price Change notification !!'
	body = 'Price of the product has changed VISIT the link:- https://www.amazon.in/Test-Exclusive-611/dp/B07HGMLBW1/ref=sr_1_1?keywords=oneplus&qid=1564219280&s=gateway&sr=8-1.'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'SenderEmailAddress',
		'ReceiverEmailAddress',
		msg
		)
	server.quit()
	print('Email sent successfully.')

if __name__ == "__main__":
	initialPrice = 32999
	if(get_price()< initialPrice):
		print(get_price())
		send_mail()

