"""get references titles in an article by the given article's references url on researchgate.@author smile4lee"""import argparseimport osimport reimport textwrapimport timefrom bs4 import BeautifulSoupfrom selenium.common.exceptions import NoSuchElementExceptionimport toolimport yml_logging.configimport configyml_logging.config.fileConfig(fname='conf/logging.conf', disable_existing_loggers=False)logger = yml_logging.getLogger(__name__)# url = 'https://www.researchgate.net/publication/312483664_National-scale_soybean_mapping_and_area_estimation_in_the_United_States_using_medium_resolution_satellite_imagery_and_field_survey/references'driver_path = config.driver_pathreference_click_class_name = 'references'reference_title_class_name = "nova-v-publication-item__title"count_ref_xpath = '//*[@id="lite-page"]/main/section/section[2]/section[2]/div/div[1]/nav/div/div[1]/button[2]/div/div/h3'show_more_btn_xpath = "//div[@class='publication-citations__more']/button"def get_references_count(html):    soup = BeautifulSoup(html, 'lxml')    # print(soup.prettify())    divs = soup.find_all(name='div', attrs={"class": reference_title_class_name})    logger.info("page size: %s, references: %s", len(html), len(divs))    return len(divs)def print_references_titles(html):    soup = BeautifulSoup(html, 'lxml')    divs = soup.find_all(name='div', attrs={"class": reference_title_class_name})    title = ''    for a in divs:        title += a.find('a').text        logger.info("reference title: %s", title)    return titledef save_to_file(content, filepath='titles.txt'):    text_file = open(filepath, "w")    text_file.write(content)    text_file.close()def click_by_xpath(driver, xpath, wait_second=10):    try:        button = driver.find_element_by_xpath(xpath)        # print("Element is visible? " + str(button.is_displayed()) + ", xpath: " + xpath)        # button.click()        driver.execute_script("arguments[0].click();", button)        driver.implicitly_wait(wait_second)        time.sleep(wait_second)    except NoSuchElementException as e:        logger.error("error, no such button by xpath: %s", xpath)        logger.error(e)        # traceback.print_exc()def click_by_class_name(driver, btn_class_name, wait_second=10):    try:        button = driver.find_element_by_class_name(btn_class_name)        # print("Element is visible? " + str(button.is_displayed()) + ", class_name: " + btn_class_name)        # button.click()        driver.execute_script("arguments[0].click();", button)        driver.implicitly_wait(wait_second)        time.sleep(wait_second)    except NoSuchElementException as e:        print("error, no such button by class: %s", btn_class_name)        logger.error(e)        # traceback.print_exc()def do(url, filepath):    driver = None    try:        wait_second = 5        driver = tool.get_driver(driver_path)        driver.get(url)        driver.implicitly_wait(wait_second)        ini_count = get_references_count(driver.page_source)        h3 = driver.find_element_by_xpath(count_ref_xpath)        btn_ref_text = h3.text        logger.info("btn_ref_text: %s", btn_ref_text)        s = re.search(r"(\d+)", btn_ref_text)        count_ref = 0        if s:            count_ref = int(s.group(0))            logger.info("count_ref: %s", count_ref)        # click by class name: 'references' button        logger.info("click 'references' button")        click_by_class_name(driver, reference_click_class_name)        get_references_count(driver.page_source)        step = 5        for i in range(ini_count, count_ref, step):            logger.info("click 'Show more' button")            # click by xpath: 'Show more' button            click_by_xpath(driver, show_more_btn_xpath)            get_references_count(driver.page_source)        titles = print_references_titles(driver.page_source)        save_to_file(titles, filepath)        logger.info('done')    except Exception as e:        logger.error(e)        yml_logging.exception(e)        raise    finally:        if not driver:            driver.quit()def main():    parser = argparse.ArgumentParser(        prog="researchgate",        formatter_class=argparse.RawDescriptionHelpFormatter,        description=textwrap.dedent('''\           researchgate           ----------------------------------------------------           get references titles in an article by the given article's references url on researchgate.           Given a bibtex file           $ researchgate --url 'https://www.researchgate.net/publication/sample_article/references' --filepath 'C:\\Users\\lihaijun\Desktop\\tmp\\titles.txt'            ----------------------------------------------------           @author: smile4lee           ''')    )    parser.add_argument(        "--url", "-u",        dest="url",        help="article's references url on researchgate"    )    parser.add_argument(        "--filepath", "-f",        dest="filepath",        help="titles will be save in the file"    )    parser.set_defaults(filepath='titles.txt')    args = parser.parse_known_args()    url = args[0].url    filepath = os.path.abspath(args[0].filepath)    do(url, filepath)if __name__ == "__main__":    main()    # test()