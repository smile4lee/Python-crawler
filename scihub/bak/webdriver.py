'''
使用Selenium模拟浏览器
抓取百度查询结果
'''

# 导入selenium模块中的web引擎
from selenium import webdriver


# 建立浏览器对象 ，通过Phantomjs
browser = webdriver.PhantomJS()

# 设置访问的url
url = "https://sci-hub.tw/10.1080/01431160310001619607"

# 访问url
browser.get(url)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)



# 找到submit按钮
button = browser.find_element_by_id('buttons')

# save_btn = browser.find_element_by_tag_name("save")

ele = browser.find_element_by_xpath('//*[@id="buttons"]/ul/li/a')

# 点击按钮 提交搜索请求
# button.click()

print(ele)

ele.click()

