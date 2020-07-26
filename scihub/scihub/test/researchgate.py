import reimport tracebackimport requestsimport timefrom bs4 import BeautifulSoupfrom selenium.common.exceptions import NoSuchElementExceptionfrom selenium.webdriver import ActionChainsfrom selenium.webdriver.common.by import Byfrom selenium.webdriver.support import expected_conditionsfrom selenium.webdriver.support.wait import WebDriverWaitfrom selenium.webdriver.support.ui import WebDriverWaitfrom selenium.webdriver.common.by import Byfrom selenium.webdriver.support import expected_conditions as ECimport tooldriver_path = "C:\\Portable\\chromedriver_win32\\chromedriver.exe"url = 'https://www.researchgate.net/publication/312483664_National-scale_soybean_mapping_and_area_estimation_in_the_United_States_using_medium_resolution_satellite_imagery_and_field_survey/references'# url = 'https://www.researchgate.net/publication/316143157_A_multi-resolution_approach_to_national# -scale_cultivated_area_estimation_of_soybean/references'classname = 'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare'xpath = '//*[@id="rgw2_5f1bad4a761f9"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/a'raw_cookies = 'did=XMO7allZaxbkjBBkyKrGfUz1n1zzBtCQ84so56x5wZwkxXyKbAzq1gxXHhO7o3WS;ptc=RG1.6721881728741481298.1575035975; _ga=GA1.2.1685583702.1575036323; isResearcher=yes; classification=institution; pl=Pd7rkAa020Cb0tWcSwd8xnsO5hqKvYDvl5D1reF1avm8pYy4L3000K8p7jAXWOaO8uZxRfPq61Zv3N6ClBL10p6aLGhkbCRaQX5k9xhuvAnKGHUvmh2Z0lRxgxlbDbf6; __cfduid=d0706c872b8b585c89ed8a9eb07e0d26d1595649243; _gid=GA1.2.1896728570.1595649245; sid=gWW0D8Wex1cFp45ZhBaiIzyNzGw0JF6eyaIehBXjp0au4Wgc60U0mhycMOneccQ5HkUVzQQLkZtgqA0Iyc1owKDCDwcyFe0FbrWEazP9qYpYwa5wnibQlocQT875Tdtx; cili=_2_ZjllOTFmMTRiYjEzNzczOTNjZGU1NGYxY2Q1NWY4MTBiNTAyZjM3NmI1YThhZDg1Yjc0NjUxNDFlODAwYWFiZF8yNDkzMDQxNDsw; cirgu=_1_DBbyJ9DlHoVWSgV2bebasKmIGISv631iQBogJJMcUcJlCtrIwECGndZQJZDXWdUhuD8%3D'cookies = {}for line in raw_cookies.split(';'):    key, value = line.split('=', 1)    key = key.strip()    cookies[key] = valuedef execute_times(driver, times, second):    for i in range(times + 1):        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        time.sleep(second)def get_references(html):    soup = BeautifulSoup(html, 'lxml')    # print(soup.prettify())    #  all = soup.find_all('a')    # all_elements = soup.find_all(name='a', attrs={"class": "nova-e-link--theme-bare"})    divs = soup.find_all(name='div', attrs={"class": "nova-v-publication-item__title"})    # for a in divs:    #     # print(a)    #     # print(a.find('a'))    #     print(a.find('a').text)    #     print('=====================')    print("page size: ", len(html))    print("references: ", len(divs))    return len(divs)def print_references(html):    soup = BeautifulSoup(html, 'lxml')    divs = soup.find_all(name='div', attrs={"class": "nova-v-publication-item__title"})    for a in divs:        print(a.find('a').text)def click_by_xpath(driver, xpath, wait_second=10):    try:        button = driver.find_element_by_xpath(xpath)        # print("Element is visible? " + str(button.is_displayed()) + ", xpath: " + xpath)        # button.click()        driver.execute_script("arguments[0].click();", button)        driver.implicitly_wait(wait_second)        time.sleep(wait_second)    except NoSuchElementException as e:        print("error, no such button by xpath: ", xpath)        # traceback.print_exc()def click_by_class_name(driver, btn_class_name, wait_second=10):    try:        button = driver.find_element_by_class_name(btn_class_name)        # print("Element is visible? " + str(button.is_displayed()) + ", class_name: " + btn_class_name)        # button.click()        driver.execute_script("arguments[0].click();", button)        driver.implicitly_wait(wait_second)        time.sleep(wait_second)    except NoSuchElementException as e:        print("error, no such button by class: ", btn_class_name)        # traceback.print_exc()def main2():    driver = tool.get_driver(driver_path)    # print(cookies)    #    # for cookie in cookies:    #     driver.add_cookie(cookie)    driver.get(url)    driver.implicitly_wait(10)    # print(driver.page_source)    ini_count = get_references(driver.page_source)    h3 = driver.find_element_by_xpath(        '//*[@id="lite-page"]/main/section/section[2]/section[2]/div/div[1]/nav/div/div[1]/button[2]/div/div/h3')    btn_ref_text = h3.text    print("btn_ref_text: ", btn_ref_text)    s = re.search(r"(\d+)", btn_ref_text)    count_ref = 0    if s:        count_ref = int(s.group(0))        print("count_ref: ", count_ref)    times = 2    # click 'references' button    click_by_class_name(driver, 'references')    driver.implicitly_wait(10)    get_references(driver.page_source)    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # driver.implicitly_wait(5)    # for i in range(1, 5, 1):    #     # driver.execute_script("arguments[0].scrollIntoView(true);", button)    #     # button.click()    #     button = driver.find_element_by_xpath('//div[@class="publication-citations__more"]/button')    #     driver.execute_script("arguments[0].click();", button)    #     driver.implicitly_wait(10)    #     get_references(driver.page_source)    '''    driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(        EC.visibility_of_element_located((By.XPATH, '//div[@class="publication-citations__more"]'))))    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="publication-citations__more"]/button'))))    driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(        EC.visibility_of_element_located((By.XPATH, '//div[@class="publication-citations__more"]/button'))))    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="publication-citations__more"]/button'))))    driver.implicitly_wait(10)    get_references(driver.page_source)    # div_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="publication-citations__more"]')))    div_element = driver.find_element_by_xpath('//div[@class="publication-citations__more"]')    driver.execute_script("arguments[0].scrollIntoView(true);", div_element)    hover = ActionChains(driver).move_to_element(div_element)    hover.perform()    # button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="publication-citations__more"]/button')))    button = driver.find_element_by_xpath('//div[@class="publication-citations__more"]/button')    driver.execute_script("arguments[0].click();", button)    driver.execute_script("arguments[0].scrollIntoView(true);", button)    hover = ActionChains(driver).move_to_element(button)    hover.perform()    print("Element is visible? " + str(button.is_displayed()))    button.click()    # button = driver.find_element_by_xpath('//div[@class="publication-citations__more"]/button')    # print("Element is visible? " + str(button.is_displayed()))    # driver.implicitly_wait(10)    # driver.execute_script("arguments[0].style.visibility = 'visible';", button)    # print("Element is visible? " + str(button.is_displayed()))    #    # new_btn = driver.find_element_by_xpath("//button[contains(text(),'Show more')]")    # new_btn.click()    #    # button.click()    get_references(driver.page_source)    # execute_times(driver, 5, 5)    '''    step = 5    # ini_count = 10    # for i in range(times + 1):    # for i in range(ini_count, count_ref, step):    for i in range(ini_count, 40, step):        # click 'show more' button        print(i)        # click(driver, 'publication-citations__more')        click_by_class_name(driver, "//div[@class='publication-citations__more']/button")        get_references(driver.page_source)    # for i in range(times + 1):    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    #     time.sleep(second)    #     html = driver.page_source    #     print("page size: ", len(html))    #     get_size(html)    html = driver.page_source    # get_size(html)    # ele = driver.find_element_by_xpath(xpath)    # ele_2 = driver.find_elements_by_class_name(classname)    soup = BeautifulSoup(html, 'lxml')    # print(soup.prettify())    print('===== done')def main():    wait_second = 5    driver = tool.get_driver(driver_path)    driver.get(url)    driver.implicitly_wait(wait_second)    ini_count = get_references(driver.page_source)    h3 = driver.find_element_by_xpath(        '//*[@id="lite-page"]/main/section/section[2]/section[2]/div/div[1]/nav/div/div[1]/button[2]/div/div/h3')    btn_ref_text = h3.text    print("btn_ref_text: ", btn_ref_text)    s = re.search(r"(\d+)", btn_ref_text)    count_ref = 0    if s:        count_ref = int(s.group(0))        print("count_ref: ", count_ref)    # click by class name: 'references' button    click_by_class_name(driver, 'references')    get_references(driver.page_source)    step = 5    for i in range(ini_count, count_ref, step):        # click by xpath: 'Show more' button        click_by_xpath(driver, "//div[@class='publication-citations__more']/button")        get_references(driver.page_source)    print_references(driver.page_source)    print('===== done')def test():    # r = requests.get(url, cookies=cookies)    # r = requests.get(url)    r = requests.get(url, headers={        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})    html = r.text    soup = BeautifulSoup(html, 'lxml')    print(soup.prettify())    print("status_code: ", r.status_code)    print("reason: ", r.reason)    #  all = soup.find_all('a')    # all_elements = soup.find_all(name='a', attrs={"class": "nova-e-link--theme-bare"})    divs = soup.find_all(name='div', attrs={"class": "nova-v-publication-item__title"})    # for a in divs:    #     print(a)    #     print(a.find('a'))    #     print(a.find('a').text)    #     print('=====================')    print("size: ", len(divs))    # print(soup.find_all('a'))if __name__ == "__main__":    main()    # test()