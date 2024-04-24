#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-22 16:44
# @Author  : Xi Yan
# @File    : config.py.py
# @Description : 项目配置文件
import os

from easydict import EasyDict as edict

config = edict()
config.class_list = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
                     'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train',
                     'tvmonitor']
config.color_map = [[128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128], [0, 128, 128], [128, 128, 128],
                    [64, 0, 0], [192, 0, 0], [64, 128, 0], [192, 128, 0], [64, 0, 128], [192, 0, 128], [64, 128, 128],
                    [192, 128, 128], [0, 64, 0], [128, 64, 0], [0, 192, 0], [128, 192, 0], [0, 64, 128]]
config.num_classes = 20
# 数据集目录
config.root_path = r'E:\OfficalProject\data\pascal_voc_aug'
config.txt_path = os.path.join(config.root_path)
config.img_path = os.path.join(config.root_path, 'JPEGImages')
config.mask_path = os.path.join(config.root_path, 'SegmentationClassAug')
# 保存地址
config.save_dir = os.path.join(config.root_path, '..', 'pascal-5i')
config.class_txt = os.path.join(config.root_path, '..', 'pascal-5i', 'Segmentation')

config.fold = 4
