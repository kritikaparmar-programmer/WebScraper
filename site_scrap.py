from bs4 import BeautifulSoup
import requests


## webscrap.html in the same repo..
with open('webscrap.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())
match = soup.title.text
match1 = soup.div
match2 = soup.find('div')
match3 = soup.find('div', class_ = 'footer')
print(match)
print(match1)
print(match2)
print(match3)

# the find all method will return the list of all the tags that match those arguments
for article in soup.find_all('div', class_='article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.p.text
	print(summary)

	print()
