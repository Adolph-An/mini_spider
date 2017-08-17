#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Spider exception

Description:
    This file defined mini spider exception
"""
#
# modification history:
# ---------------------
# 2017/08/16, by An Chun Lin, Create
#


class SpiderException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg
