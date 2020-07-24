from scihub import SciHub
import tool

scihub_url = 'https://sci-hub.tw/'
download_dir = "C:\\Users\\lihaijun\\Desktop\\tmp"
xpath_search_input = '//*[@id="input"]/form/input[2]'
id_search_btn = 'open'
xpath_download_click = '//*[@id="buttons"]/ul/li/a'
driver_path = "C:\\Portable\\chromedriver_win32\\chromedriver.exe"

# title = 'Remote sensing and land cover area estimation'
title = 'aaaa'


sci_hub = SciHub(
    tool.getDriver(driver_path, download_dir),
    title,
    scihub_url,
    download_dir,
    xpath_search_input,
    id_search_btn,
    xpath_download_click,
)


def main():
    sci_hub.do()


if __name__ == "__main__":
    main()
