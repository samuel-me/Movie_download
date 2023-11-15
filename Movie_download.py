import requests, webbrowser, pyperclip, bs4
""" a webscrrapper that checks movie rating 
for sexual contents
goes to a download page if there isnt any"""

movie_name = pyperclip.paste()
# trying to fit it with the rotentommatoes address
for i in string.punctuation:
	if i in movie_name:
		x = movie_name.replace(i,'_')
		x = x.replace(' ','_')

res1 = requests.get('https://www.rottentomatoes.com/m/'+ x)
res1.raise_for_status()

soup = bs4.BeautifulSoup(res1.text,'html.parser')
first = soup.select('.meta-value')
print(str(first[0]))
ye = 'R (for sexual content and some nudity)'
# tesla
y = str(first[0].getText())


if 'sexual content'  and 'nudity' in y:
    print('sorry brah!!!!!!!!!!!!!!!')
else:
    res2 = requests.get('https://www.thenetnaija.com/search?t='+ movie_name)
    res2.raise_for_status()
    soup2 = bs4.BeautifulSoup(res2.text,'html.parser')
    second = soup2.select('h3 a')# h3 a is the css selector
    hell = str(second[0].get('href'))

    res3 = requests.get(hell)
    res3.raise_for_status()
    soup3 = bs4.BeautifulSoup(res3.text,'html.parser')
    third = soup3.select('p a')

    heaven = str(third[4].get('href'))
    print('opening download page',heaven)

    res4 = requests.get(heaven)
    res4.raise_for_status()
    webbrowser.open(heaven)

