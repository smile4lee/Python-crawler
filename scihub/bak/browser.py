# from selenium import webdriver
#
# # 设置访问的url
# url = "https://sci-hub.tw/10.1080/01431160310001619607"
#
# options = webdriver.ChromeOptions()
#
# options.add_argument("download.default_directory=C:/Downloads")
#
# driver = webdriver.Chrome(chrome_options=options)
#
# # profile = webdriver.chrome()
# # profile.set_preference("browser.download.folderList", 2)
# # profile.set_preference("browser.download.manager.showWhenStarting", False)
# # profile.set_preference("browser.download.dir", 'PATH TO DESKTOP')
# # profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "pdf")
# #
# # driver = webdriver.Firefox(firefox_profile=profile)
#
#
# driver.get(url)
# driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a').click()
#


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = "https://sci-hub.tw/10.1080/01431160310001619607"
driver_path = "C:\\Portable\\chromedriver_win32\\chromedriver.exe"

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
# driver.get(url)
# driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a').click()




download_dir = "C:\\Users\\lihaijun\\Desktop\\tmp"  # for linux/*nix,
# download_dir="/usr/Public"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(driver_path, chrome_options=options)  # Optional argument, if not specified will search path.

driver.get(url)
driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a').click()