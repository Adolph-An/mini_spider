#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Seed file load

Description:
    This file implement seed file load module
"""
#
# modification history:
# ---------------------
# 2017/08/16, by An Chun Lin, Create
#

import os
import sys

import spider_exception


class SeedFile(object):
    """Seed file object

    Attributes:
        url_list: url list loaded from seed file
    """

    def __int__(self):
        self.url_list = []

    def load(self, seedfile_path):
        """Load seed file

        Args:
            seedfile_path

        Returns:
            None
        """

        if not os.path.isfile(seedfile_path):
            raise SpiderException("Invalid seed file: %s" % seedfile_path)

        try:
            seed_file = open(seedfile_path)
        except IOError as e:
            raise SpiderException("Open seed file error: %s" % e[1])

        for url in seed_file:
            self.url_list.extend(url.strip('\n'))
