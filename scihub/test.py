from scihub import SciHub
import tool

scihub_url = 'https://sci-hub.tw/'
download_dir = "download"
xpath_search_input = '//*[@id="input"]/form/input[2]'
id_search_btn = 'open'
xpath_download_click = '//*[@id="buttons"]/ul/li/a'
driver_path = "C:\\Portable\\chromedriver_win32\\chromedriver.exe"

title = 'Remote sensing and land cover area estimation'
# title = 'aaaa'

download_url = 'http://sci-hub.tw/10.1080/01431160310001619607'


def main():
    driver = tool.getDriver(driver_path, download_dir)
    driver.get(download_url)
    driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a')
    driver.find_element_by_xpath('//*[@id="pdf"]')
    find1 = driver.find_element_by_tag_name("iframe")

    print("done")


if __name__ == "__main__":
    main()
