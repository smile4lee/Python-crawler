import traceback

import tool
import sys


class SciHub(object):
    def __init__(self,
                 driver,
                 title,
                 scihub_url="https://sci-hub.tw/",
                 download_dir="C:\\Users\\lihaijun\\Desktop\\tmp",
                 xpath_search_input='//*[@id="input"]/form/input[2]',
                 id_search_btn='open',
                 xpath_download_click='//*[@id="buttons"]/ul/li/a',
                 ):
        self.driver = driver
        self.scihub_url = scihub_url
        self.title = title
        self.download_dir = download_dir
        self.xpath_search_input = xpath_search_input
        self.id_search_btn = id_search_btn
        self.xpath_download_click = xpath_download_click
        self.download_url = None

    def set_driver(self, driver):
        self.driver = driver

    def do(self):
        print("do it with params:")
        print("scihub_url: %s" % self.scihub_url)
        print("title: %s" % self.title)
        print("download_dir: %s" % self.download_dir)
        print("xpath_search_input: %s" % self.xpath_search_input)
        print("id_search_btn: %s" % self.id_search_btn)
        print("xpath_download_click: %s" % self.xpath_download_click)
        try:
            self.download_url = tool.search(self.driver, self.scihub_url, self.title)
            tool.download(self.driver, self.download_url, self.download_dir, self.title)
            tool.rename_latest_file(self.download_dir, self.title)

        except Exception as e:
            print(str(e))
            print("error with title: %s" % self.title)
            print("error with url: %s" % self.download_url)
            traceback.print_exc()
            sys.exit(1)

        sys.exit(0)
