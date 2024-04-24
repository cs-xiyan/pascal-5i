#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-22 21:34
# @Author  : Xi Yan
# @File    : io_tools.py
# @Description :
import os

from config import config


def txt_to_list(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data_list = [line.strip() for line in lines]
    return data_list

def list_to_txt(file_path,data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(line.strip() + "\n")
