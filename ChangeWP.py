#!/usr/bin/python3

import os
import sys
import time
import json
import time
import random
import urllib.request


def get_bing_photo_url():
    print("quering wallpaper")
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    req = urllib.request.urlopen(url)
    json_str = req.read()
    req.close()
    json_obj = json.loads(json_str)
    url = 'https://www.bing.com/' + json_obj['images'][0]['url']

    return url


def download_photo(url, name):
    print("download photo %s to %s" % (url, name))
    with urllib.request.urlopen(url) as fsock:
        with open(name, 'wb') as fout:
            fout.write(fsock.read())


def find_local_photo(dirname):
    files = os.listdir(dirname)
    images = [file for file in files if file.endswith(".jpg")]
    if len(images) == 0:
        return None

    ind = int(random.random()*len(images))

    return images[ind]


def set_photo(file):
    #ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
    abspath = os.path.abspath('.')
    fullpath = os.path.join(abspath, file)
    print("setting wallpaper: %s" % fullpath)
    os.system("gsettings set org.gnome.desktop.background picture-uri \'%s\'" % fullpath)

if __name__ == "__main__":
    num = 1234567

    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])

    old_day = 0;
    old_url = ""

    while True:
        wallpaper = "%d.jpg" % num
        try:
            day = time.localtime().tm_mday
            if day != old_day:
                url = get_bing_photo_url()
                if url != old_url:
                    print("url: %s" % url)
                    download_photo(url, wallpaper)
                    old_url = url
                else:
                    wallpaper = find_local_photo('.')
                old_day = day
            else:
                wallpaper = find_local_photo('.')
        except Exception as e:
            print("failed to download a wallpaper", e)
            wallpaper = find_local_photo('.')

        if len(wallpaper) > 0:
            set_photo(wallpaper)

        time.sleep(2*60)
