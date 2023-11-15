import bs4,requests,webbrowser,time
#planning to use pyperclip

url ='https://www2.gogoanime.sh/wonder-egg-priority-episode-1'
while not url.endswith('-22'):
    res = requests.get(url)
    res.raise_for_status()
    firstpage = bs4.BeautifulSoup(res.text,'html.parser')
    the_button = firstpage.select('#wrapper_bg > section > section.content_left > div:nth-child(1) > div.anime_video_body > div.anime_video_body_cate > div.favorites_book > ul > li.dowloads > a')
    link = str(the_button[0].get('href'))
    print('opening',link)
# page 2
    res2 = requests.get(link)
    button2 = bs4.BeautifulSoup(res2.text,'html.parser')

    #for a clearer verson

    clear = '#main > div > div.content_c > div > div:nth-child(5) > div:nth-child(3) > a'
    not_clear = '#main > div > div.content_c > div > div:nth-child(5) > div:nth-child(4) > a'

    yam = button2.select(not_clear)
    yamm = yam[0].get('href')
    webbrowser.open(yamm)
    print('downolading',url[115:])
    time.sleep(100)
#page3
    next = firstpage.select( '#wrapper_bg > section > section.content_left > div:nth-child(1) > div.anime_video_body > div.anime_video_body_episodes > div.anime_video_body_episodes_r > a')
    y = next[0].get('href')
    url ='https://gogoanime.so' + str(y)
print('done')


