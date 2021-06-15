import time
from playsound import playsound
from bs4 import BeautifulSoup
import requests

url = 'https://www.costco.com/kettle-collection-spinach-artichoke-dip-with-parmesan-cheese%2c-4-lbs.product.100664647.html'

def get_page_html(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
	}
	page = requests.get(url, headers=headers)
	return page.content

def check_item_in_stock(page_html):
	soup = BeautifulSoup(page_html, 'html.parser')
	out_of_stock_divs = soup.findAll("img", {"class": "oos-overlay hide"})
	return len(out_of_stock_divs) != 0

def send_notification():
	while True:
		playsound('alarm.mp3')

def check_inventory():
	page_html = get_page_html(url)
	if check_item_in_stock(page_html):
		send_notification()
	else:
		print("Still out of stock bruh")

while True:
	check_inventory()
	time.sleep(30)	# Wait in seconds and then try again
