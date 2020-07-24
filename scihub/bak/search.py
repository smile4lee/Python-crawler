'''
使用Selenium模拟浏览器
抓取百度查询结果
'''

# 导入selenium模块中的web引擎

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


base_url = "https://sci-hub.tw/"
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

driver.get(base_url)
# driver.find_element_by_xpath('//*[@id="buttons"]/ul/li/a').click()


# 等待一定时间，让js脚本加载完毕
driver.implicitly_wait(3)

# 找到搜索框
text = driver.find_element_by_xpath('//*[@id="input"]/form/input[2]')

# 清空搜索框的文字
text.clear()

# 填写搜索框的文字
text.send_keys('Remote sensing and land cover area estimation')

# 找到submit按钮
button = driver.find_element_by_id('open')

# 点击按钮 提交搜索请求
button.click()


# 查看当前浏览器标题
print(driver.title)
print(driver.current_url)

# 以截图的方式查看浏览器的页面
driver.save_screenshot('text.png')

