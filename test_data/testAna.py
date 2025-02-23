import json
import re
from collections import defaultdict

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def split_content_by_punctuation(content):
    # 按逗号或句号拆分content
    segments = re.split(r'["? ，。]', content)
    # 去掉空段
    segments = [seg.strip() for seg in segments if seg.strip()]
    return segments

def visualize_data(data):
    num_counts = defaultdict(int)
    for item in data:
        num_counts[item['num']] += 1

    sorted_counts = sorted(num_counts.items())

    nums, counts = zip(*sorted_counts)

    plt.bar(nums, counts)
    plt.xlabel('Number of Segments')
    plt.ylabel('Frequency')
    plt.title('Distribution of Number of Segments')
    plt.show()

def analyze_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取 true_classification 为 None 的项
    none_class_items = [item for item in data if item['true_classification'] is None]
    print("-------------------------------------------------------------------------------------")
    print("Original items:", len(none_class_items))
    for item in none_class_items:
        print(item)

    # 初始化字典，用于存储不同长度 content 的列表
    content_by_length = defaultdict(list)

    # 根据逗号和句号将 content 划分为不同长度的部分
    for item in none_class_items:
        segments = split_content_by_punctuation(item['content'])
        num_segments = len(segments)  # 计算句子数量
        item['num'] = num_segments  # 将句子数量添加到数据中
        for seg in segments:
            content_by_length[len(seg)].append(seg)
    # 可视化数据
    visualize_data(none_class_items)


    print("-------------------------------------------------------------------------------------")
    print("New items:",len(none_class_items))
    for item in none_class_items:
        print(item)

    # 输出不同数量的数据总数以及每条数据的内容
    num_counts = defaultdict(list)
    for item in none_class_items:
        num_counts[item['num']].append(item)

    for num, items in num_counts.items():
        print("**********************************************")
        print(f"num {num}: {len(items)} data items")
        for item in items:
            print(item)
        print("**********************************************")

    # 可视化 length 分布
    lengths = list(content_by_length.keys())
    counts = [len(content_by_length[length]) for length in lengths]

    plt.figure(figsize=(10, 6))
    plt.bar(lengths, counts, color='skyblue')
    plt.xlabel('Length of Segments')
    plt.ylabel('Number of Data Items')
    plt.title('Distribution of Segment Lengths')
    plt.xticks(lengths)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


    # 输出不同长度的 content
    for length, content_list in content_by_length.items():
        print(f"Length {length}:")
        print(content_list)
        print()

    # 聚类分析
    lengths = list(content_by_length.keys())
    X = np.array(lengths).reshape(-1, 1)  # 将长度转换为二维数组
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    print("Cluster Centers:")
    print(kmeans.cluster_centers_)


json_file = 'E:\测试集\\finaloOutput.json'
analyze_data(json_file)
