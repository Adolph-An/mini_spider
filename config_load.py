#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Config load

Description:
    This file implement config load module
"""
#
# modification history:
# ---------------------
# 2017/08/16, by An Chun Lin, Create
#

import os
import sys
import ConfigParser

import spider_exception


class ConfigLoad(object):
    """Load config file

    Attributes:
        url_list_file: seed file path
        output_directory: path to save pages
        max_depth: max crawl depth(default 0)
        crawl_interval:
        crawl_timeout:
        target_url: pattern of target url
        thread_count: max number of thread(default 1)
    """

    def __init__(self):
        self.url_list_file = None
        self.output_directory = None
        self.max_depth = 0
        self.crawl_interval = None
        self.crawl_timeout = None
        self.target_url = None
        self.thread_count = 1

    def config_file_load(self, file_path):
        """Load config file from `file_path`

        Args:
            file_path: config file path

        Return:
            None
        """

        if not os.path.isfile(file_path):
            raise SpiderException('Error file path')
        cf = ConfigParser.ConfigParser()
        cf.read(file_path)
        try:
            self.url_list_file = cf.get("spider", "url_list_file")
            self.output_directory = cf.get("spider", "output_directory")
            self.max_depth = cf.getint("spider", "max_depth")
            self.crawl_interval = cf.getint("spider", "crawl_interval")
            self.crawl_timeout = cf.getint("spider", "crawl_timeout")
            self.target_url = cf.get("spider", "target_url")
            self.thread_count = cf.getint("spider", "thread_count")
        except ConfigParser.Error as e:
            raise SpiderException('ConfigParser error %s' % e)
