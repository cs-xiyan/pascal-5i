#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-22 21:11
# @Author  : Xi Yan
# @File    : generate_class_txt.py
# @Description : 按照类别和mode(train、val)进行归类
import os

import numpy as np
from PIL import Image
from tqdm import tqdm

from config import config
from util.io_tools import txt_to_list, list_to_txt


def generate_class(mode):
    """
    将图片进行归类
    :param mode: train or val
    :return:
    """
    dic={}
    data_list = txt_to_list(mode)
    for file_name in tqdm(data_list):
        mask_path = os.path.join(config.mask_path, file_name + ".png")
        mask = Image.open(mask_path)
        mask_arr=np.array(mask)
        class_set=set(np.unique(mask_arr)) - {0, 255}
        for cls in class_set:
            if cls not in dic.keys():
                dic[cls]=[]
            dic[cls].append(file_name)
    os.makedirs(config.class_txt, exist_ok=True)
    os.makedirs(os.path.join(config.class_txt,mode), exist_ok=True)

    for cls in dic:
        file_path=os.path.join(config.class_txt,mode,str(cls)+'.txt')
        list_to_txt(file_path,dic[cls])










