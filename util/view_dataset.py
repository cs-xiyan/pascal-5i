#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 16:57
# @Author  : Xi Yan
# @File    : view_dataset.py
# @Description : 可视化展示数据集
import os
import sys

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from tqdm import tqdm

from config import config


def view_dataset_class(mode,split):
    """mask类别可视化统计"""


    mask_dir=os.path.join(config.save_dir, mode, str(split), "SegmentationClass")

    masks = os.listdir(mask_dir)
    loop_filenames = tqdm(masks, total=len(masks), file=sys.stdout)
    class_dict = {}
    for file in loop_filenames:
        file_path = os.path.join(mask_dir, file)
        class_dict[file] = np.asarray(Image.open(file_path))
    class_info = count_class_occurrences(class_dict, config.class_list)
    print("Class occurrences in the dataset:")
    print(class_info)
    plot_bar_chart(class_info, mode, split)

def map_class(original_cls,class_list):
    # Mapping original classes to final display classes
    class_mapping = dict(zip(range(1,len(class_list)+1),class_list))
    return class_mapping.get(original_cls, f'Unknown_{original_cls}')


def count_class_occurrences(dataset,class_list):
    class_info = {}

    for (x, y) in dataset.items():
        unique_classes= set(np.unique(y)) - {0, 255}
        for cls in unique_classes:
            if cls != 0:  # 0表示背景，不统计
                mapped_cls = map_class(cls,class_list=class_list)
                if mapped_cls not in class_info:
                    class_info[mapped_cls] = 1
                else:
                    class_info[mapped_cls] += 1

    # Sort classes based on the custom order
    class_info = {k: class_info[k] for k in class_list if k in class_info}

    return class_info


def plot_bar_chart(class_info,mode,split):
    categories = list(class_info.keys())
    counts = list(class_info.values())

    # Plot bar chart with labels
    fig, ax = plt.subplots()
    bars = ax.bar(categories, counts, color='blue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

    plt.xlabel('Classes')
    plt.ylabel('Number of Images')
    plt.title('Number of Images per Class mode {} split {}'.format(mode,split))
    plt.show()

