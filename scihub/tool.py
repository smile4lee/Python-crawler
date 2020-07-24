import sys
import glob
import os
import shutil

from selenium import webdriver


def getDriver(driver_path, download_dir):
    # Disable Chrome's PDF Viewer
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option("prefs", profile)
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome(driver_path, chrome_options=options)

    return driver


def search(driver, url, title):
    driver.get(url)

    # 等待一定时间，让js脚本加载完毕
    driver.implicitly_wait(3)

    # 找到搜索框
    text = driver.find_element_by_xpath('//*[@id="input"]/form/input[2]')

    # 清空搜索框的文字
    text.clear()

    # 填写搜索框的文字
    text.send_keys(title)

    # 找到submit按钮
    button = driver.find_element_by_id('open')

    # 点击按钮 提交搜索请求
    button.click()

    # 查看当前浏览器标题
    print("current title: %s " % driver.title)
    print("current url: %s " % driver.current_url)

    return driver.current_url


def download(driver, download_url, download_dir, title):
    print("try to download pdf file to dest dir: %s" % download_dir)

    driver.get(download_url)

    try:
        driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a').click()
    except Exception:
        print("error with title: %s" % title)
        print("error with url: %s" % download_url)
        sys.exit(1)

    print("download finished with title: %s" % title)
    print("download finished with url: %s" % download_url)


def rename_latest_file(dir, title, extension="/*.pdf"):
    # * means all if need specific format then *.csv
    list_of_files = glob.glob(dir + extension)
    latest_file = max(list_of_files, key=os.path.getctime)
    print("latest_file: %s" % latest_file)
    # os.rename(latest_file, os.path.join(dir, title + ".pdf"))
    shutil.move(latest_file, os.path.join(dir, title + ".pdf"))
    print("rename finished with dir: %s" % dir)
    print("rename finished with title: %s" % title)

