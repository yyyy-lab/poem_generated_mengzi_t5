import json
import re


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


def process_json_file(input_file, output_file):
    classified_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            content = item.get('content', '')
            poem_type = classify_chinese_poem(content)
            if poem_type:
                item['true_classification'] = poem_type
            else:
                item['true_classification'] = None  # 设置为None
            classified_data.append(item)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(classified_data, f, ensure_ascii=False, indent=4)


input_file = 'E:\文本挖掘三\测试集分析\AgainOutput.json'
output_file = 'E:\文本挖掘三\测试集分析\\AgainChangeOutput.json'
process_json_file(input_file, output_file)


def adjust_json_format(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    formatted_data = []
    for item in data:
        formatted_item = {
            "classification": item['classification'],
            "story": item['story'],
            "content": item['content'],
            "true_classification": item['true_classification'],
        }
        formatted_data.append(formatted_item)

    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=4)


input_file = 'E:\文本挖掘三\测试集分析\\AgainChangeOutput.json'
adjust_json_format(input_file)
