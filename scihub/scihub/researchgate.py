import time

import tool
import requests
from bs4 import BeautifulSoup
import lxml

from selenium import webdriver
import config

driver_path = "C:\\Portable\\chromedriver_win32\\chromedriver.exe"

url = 'https://www.researchgate.net/publication/312483664_National-scale_soybean_mapping_and_area_estimation_in_the_United_States_using_medium_resolution_satellite_imagery_and_field_survey/references'

url = 'https://www.researchgate.net/publication/316143157_A_multi-resolution_approach_to_national-scale_cultivated_area_estimation_of_soybean/references'

classname = 'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare'
xpath = '//*[@id="rgw2_5f1bad4a761f9"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/a'

raw_cookies = 'did=XMO7allZaxbkjBBkyKrGfUz1n1zzBtCQ84so56x5wZwkxXyKbAzq1gxXHhO7o3WS;ptc=RG1.6721881728741481298.1575035975; _ga=GA1.2.1685583702.1575036323; isResearcher=yes; classification=institution; pl=Pd7rkAa020Cb0tWcSwd8xnsO5hqKvYDvl5D1reF1avm8pYy4L3000K8p7jAXWOaO8uZxRfPq61Zv3N6ClBL10p6aLGhkbCRaQX5k9xhuvAnKGHUvmh2Z0lRxgxlbDbf6; __cfduid=d0706c872b8b585c89ed8a9eb07e0d26d1595649243; _gid=GA1.2.1896728570.1595649245; sid=gWW0D8Wex1cFp45ZhBaiIzyNzGw0JF6eyaIehBXjp0au4Wgc60U0mhycMOneccQ5HkUVzQQLkZtgqA0Iyc1owKDCDwcyFe0FbrWEazP9qYpYwa5wnibQlocQT875Tdtx; cili=_2_ZjllOTFmMTRiYjEzNzczOTNjZGU1NGYxY2Q1NWY4MTBiNTAyZjM3NmI1YThhZDg1Yjc0NjUxNDFlODAwYWFiZF8yNDkzMDQxNDsw; cirgu=_1_DBbyJ9DlHoVWSgV2bebasKmIGISv631iQBogJJMcUcJlCtrIwECGndZQJZDXWdUhuD8%3D'

cookies = {}
for line in raw_cookies.split(';'):
    key, value = line.split('=', 1)
    key = key.strip()
    cookies[key] = value


def execute_times(driver, times, second):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(second)

def get_size(html):
    soup = BeautifulSoup(html, 'lxml')

    # print(soup.prettify())

    #  all = soup.find_all('a')

    # all_elements = soup.find_all(name='a', attrs={"class": "nova-e-link--theme-bare"})
    divs = soup.find_all(name='div', attrs={"class": "nova-v-publication-item__title"})

    # for a in divs:
    #     # print(a)
    #     # print(a.find('a'))
    #     print(a.find('a').text)
    #     print('=====================')

    print("size: ", len(divs))

def main():
    driver = tool.get_driver(driver_path)

    # print(cookies)
#
    # for cookie in cookies:
    #     driver.add_cookie(cookie)

    driver.get(url)




    # execute_times(driver, 5, 5)

    times = 5
    second = 10
    # for i in range(times + 1):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(second)
    #     html = driver.page_source
    #     print("page size: ", len(html))
    #     get_size(html)

    html = driver.page_source

    # get_size(html)

    # ele = driver.find_element_by_xpath(xpath)
    # ele_2 = driver.find_elements_by_class_name(classname)

    soup = BeautifulSoup(html, 'lxml')

    print(soup.prettify())

    print("done")


def test():
    # r = requests.get(url, cookies=cookies)
    # r = requests.get(url)
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    print(soup.prettify())

    print("status_code: ", r.status_code)
    print("reason: ", r.reason)

    #  all = soup.find_all('a')

    # all_elements = soup.find_all(name='a', attrs={"class": "nova-e-link--theme-bare"})
    divs = soup.find_all(name='div', attrs={"class": "nova-v-publication-item__title"})

    # for a in divs:
    #     print(a)
    #     print(a.find('a'))
    #     print(a.find('a').text)
    #     print('=====================')

    print("size: ", len(divs))

    # print(soup.find_all('a'))


if __name__ == "__main__":
    # main()
    test()
