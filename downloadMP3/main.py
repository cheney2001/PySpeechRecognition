# -*- coding: utf-8 -*-

from urllib.request import urlretrieve
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download():
    with open('data.txt', 'r') as file:
        urls = file.readlines()
        # 计算链接地址条数
        n_urls = len(urls)
        # 遍历链接地址下载图片
        for i, url in enumerate(urls):
            try:
                path = os.path.abspath('.')
                path = os.path.join(path, str(i+1) + '.mp3')
                urlretrieve(url, path)
                print('download success :' + url)
            except:
                print('no file: '+url)


if __name__ == '__main__':
    download()
