#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-22 16:48
# @Author  : Xi Yan
# @File    : main.py.py
# @Description :
import os.path

import numpy as np
from PIL import Image
from tqdm import tqdm

from config import config
from util.generate_class_txt import generate_class
from util.io_tools import txt_to_list
from util.view_dataset import view_dataset_class


def get_query_range(split):
    """
    定义query_set范围
    :param split:
    :return:
    """
    return [i + 1 for i in range(5 * split, 5 * split + 5)]


def save_dataset(dataset, split, mode):
    for file_name in tqdm(dataset):
        img_path = os.path.join(config.img_path, file_name + ".jpg")
        mask_path = os.path.join(config.mask_path, file_name + ".png")
        img = Image.open(img_path)
        mask = Image.open(mask_path)
        mask_ar = np.array(mask)
        for cls in range(1, 21):
            select_pix = np.where(mask_ar == cls)
            # 从图片中提取出该类
            if cls in get_query_range(split):
                mask_ar[select_pix[0], select_pix[1]] = cls
            else:
                mask_ar[select_pix[0], select_pix[1]] = 0
        # 还原回图像
        mask = Image.fromarray(mask_ar)
        save_image(file_name, img, mask, split, mode)


def save_image(name, img, mask, split, mode):
    root_dir = os.path.join(config.save_dir)
    os.makedirs(root_dir, exist_ok=True)
    os.makedirs(os.path.join(root_dir, mode), exist_ok=True)
    os.makedirs(os.path.join(root_dir, mode, str(split)), exist_ok=True)
    img_dir = os.path.join(root_dir, mode, str(split), "JPEGImages")
    mask_dir = os.path.join(root_dir, mode, str(split), "SegmentationClass")
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(mask_dir, exist_ok=True)
    img.save(os.path.join(img_dir, name + '.jpg'))
    mask.save(os.path.join(mask_dir, name + '.png'))


# 类别进行归类
# 然后根据归类的列表生成pascal-5i
def get_data_dic(mode):
    """
    获取数据列表
    :return:
    """
    dic = {}
    for cls in range(1, config.num_classes + 1):
        txt_path = os.path.join(config.class_txt, mode, str(cls) + '.txt')
        if cls not in dic:
            dic[cls] = []
        dic[cls] = txt_to_list(txt_path)
    return dic


def crate_dataset(data, split, mode):
    """
    创建数据集
    :param data: 数据
    :param split: 分割
    :return:
    """
    queryDataSet = []
    queryRange = get_query_range(split)
    for cls in queryRange:
        queryDataSet += data[cls]
    save_dataset(queryDataSet, split, mode)


def main():
    for mode in ['train', 'val']:
        # 生成类文件
        # generate_class(mode)
        # data = get_data_dic(mode)
        for split in range(config.fold):
            # crate_dataset(data, split, mode)
            view_dataset_class(mode=mode, split=split)


if __name__ == '__main__':
    main()
