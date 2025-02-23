import os
import pandas as pd
import json

# 定义data文件夹的路径
data_folder = '/content/data'

# 获取data文件夹下所有JSON文件的文件名
json_files = [file for file in os.listdir(data_folder) if file.endswith('.json')]

# 用于存储所有JSON文件数据的列表
json_data = []

# 逐个读取JSON文件并添加到列表中
for file in json_files:
    file_path = os.path.join(data_folder, file)
    with open(file_path, 'r') as f:
        json_content = json.load(f)
        json_data.extend(json_content)

# 将数据转换为 JSON Lines 格式字符串
json_lines = '\n'.join(json.dumps(entry) for entry in json_data)

# 将 JSON Lines 格式字符串写入文件
with open('/content/combined_data.jsonl', 'w') as f:
    f.write(json_lines)

# 使用pandas的read_json函数将JSON Lines数据读取为DataFrame
df = pd.read_json('/content/combined_data.jsonl', lines=True)

# 重新设置索引，确保每一行都有唯一的索引
df.reset_index(drop=True, inplace=True)

print(df)


import re

# 定义函数用于分类诗歌形式
def classify_chinese_poem(poem):
    # 按逗号或句号拆分诗句
    lines = re.split(r'[，。]', poem)
    # 去掉空行
    lines = [line.strip() for line in lines if line.strip()]
    # 获取每行的字数
    line_lengths = [len(line) for line in lines]

    if len(lines) == 4:
        if all(length == 5 for length in line_lengths):
            return "五言绝句"
        elif all(length == 7 for length in line_lengths):
            return "七言绝句"
        else:
            return None
    elif len(lines) == 8:
        if all(length == 5 for length in line_lengths):
            return "五言律诗"
        elif all(length == 7 for length in line_lengths):
            return "七言律诗"
        else:
            return None
    else:
        return None

# 应用分类函数筛选诗歌形式
def filter_poems(dataframe):
    filtered_poems = []
    for index, row in dataframe.iterrows():
        poem_data = row.to_dict()  # 将每一行转换为字典
        poem_content = poem_data.get('content', '')  # 获取诗歌内容，如果内容为空则返回空字符串
        classification = classify_chinese_poem(poem_content)
        if classification:
            poem_data['classification'] = classification
            filtered_poems.append(poem_data)
    filtered_df = pd.DataFrame(filtered_poems)
    filtered_df.drop_duplicates(subset=['content'], inplace=True)
    return filtered_df

# 对数据框进行筛选
filtered_df = filter_poems(df)
print(filtered_df)


import json

# 将 DataFrame 转换为 Python 字典
filtered_data_dict = filtered_df.to_dict(orient='records')

# 保存数据到 JSON 文件
with open('/content/filtered_data.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data_dict, f, indent=4, ensure_ascii=False)
