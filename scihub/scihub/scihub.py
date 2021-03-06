import logging
import os

import time

import config
import tool

logger = logging.getLogger(__name__)


class SciHub(object):
    def __init__(self,
                 title,
                 ):
        # absolute full path of download path
        abs_download_dir = os.path.abspath(config.download_dir)
        self.driver = tool.get_driver(config.driver_path, abs_download_dir)
        self.scihub_url = config.scihub_url
        self.title = title
        self.download_dir = abs_download_dir
        self.xpath_search_input = config.xpath_search_input
        self.id_search_btn = config.id_search_btn
        self.xpath_download_click = config.xpath_download_click
        self.download_url = None

    def set_driver(self, driver):
        self.driver = driver

    def do(self):
        logger.info("title: %s", self.title)
        try:
            self.download_url = tool.search(self.driver, self.scihub_url, self.title)
            tool.download(self.driver, self.download_url, self.download_dir, self.title)

            # sleep to wait for the download finishing
            time.sleep(10)
            tool.rename_latest_file(self.download_dir, self.title)
        except Exception as e:
            logger.error("error with title: %s, url: %s", self.title, self.download_url)
            logging.exception(e)
        finally:
            if self.driver is not None:
                logger.info("close and quit driver")
                self.driver.close()
                self.driver.quit()