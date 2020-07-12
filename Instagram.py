from selenium import webdriver
from bs4 import BeautifulSoup
import json

user_agent = {"User-Agent": "Mozilla/5.0 "
                            "(Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/80.0.3987.163 Safari/537.36"}

browser = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver.exe")

# Accounts
def username():
    username='user'
    browser.get('https://www.instagram.com/'+username+'/?hl=en')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    source = browser.page_source
    data = BeautifulSoup(source, 'lxml')
    body = data.find('body')
    script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
    page_json = script.string.split(' = ', 1)[1].rstrip(';')
    data_json = json.loads(page_json)
    data_json = data_json['entry_data']['ProfilePage'][0]['graphql']['user']
    # print(data_json)

    # with open('profile_data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data_json, f, ensure_ascii=False, indent=4)

    result = {
        'username': data_json['username'],
        'full_name': data_json['full_name'],
        'biography': data_json['biography'],
        'external_url': data_json['external_url'],
        'followers_count': data_json['edge_followed_by']['count'],
        'following_count': data_json['edge_follow']['count'],
        'is_private': data_json['is_private'],
        'total_posts': data_json['edge_owner_to_timeline_media']['count'],
        'profile_picture': data_json['profile_pic_url_hd']
    }
    for key,value in result.items():
        print(key,':',value)



# Hashtags
def hashtag():
    hashtag='deepthinking'
    browser.get('https://www.instagram.com/explore/tags/'+hashtag)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    links = []
    captions = []
    source = browser.page_source
    data = BeautifulSoup(source, 'lxml')
    body = data.find('body')
    script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
    page_json = script.string.split(' = ', 1)[1].rstrip(';')
    data_json = json.loads(page_json)
    data_json = data_json['entry_data']['TagPage'][0]['graphql']['hashtag']
    # print(data_json)

    # with open('caption_data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data_json, f, ensure_ascii=False, indent=4)

    result = {
        'id': data_json['id'],
        'tag_name': data_json['name'],
        'caption': data_json['edge_hashtag_to_media']['edges'][0]['node']['edge_media_to_caption']['edges'][0]['node']['text']
    }
    print('\n',result)

username()
hashtag()






















