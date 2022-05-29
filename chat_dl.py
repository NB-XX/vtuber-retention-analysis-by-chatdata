from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from chat_downloader import ChatDownloader
import os
# 这里加的是我自己电脑的代理
os.environ["http_proxy"] = f"http://127.0.0.1:7890"
os.environ["https_proxy"] = f"http://127.0.0.1:7890"


def get_chat_id(url):
    id_list = []
    try:
        chat = ChatDownloader().get_chat(url, message_groups=[
            'messages'])
        print("chat获取成功，正在解析id")
        for message in chat:
            id = message['author']['id']
            id_list.append(id)
        return id_list
    except:
        print("你这链接有问题啊")


def get_video_urls(url, sort):
    driver = webdriver.Chrome(service=Service(
        r'd:\code\chromedriver_win32\chromedriver.exe'))
    video_link_list = []
    # 设置排序模式
    if sort == 'new':
        full_url = f'{url}/videos?view=0&sort=da&flow=grid'
    else:
        full_url = f'{url}/videos?view=0&sort=dd&flow=grid'
    driver.get(full_url)
    xpath = '//ytd-thumbnail[@class="style-scope ytd-grid-video-renderer"]/a'
    # 获取A标签中的herf 不过好像没有设置模拟下拉所以获取的并不全 但是够用了
    try:
        for content in driver.find_elements(by=By.XPATH, value=xpath):
            link = content.get_attribute("href")
            video_link_list.append(link)
        print('获取视频列表完毕')
        return video_link_list[:5]
    except:
        print('好像妹找到有视频')
