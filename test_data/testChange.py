import json
import json
def parse_txt_to_json(txt_file):
    json_data = []

    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        i = 0

        while i < num_lines:
            if lines[i].startswith('标题：'):
                classification = lines[i].split('作诗一首')[1].split(' 根据故事')[0].strip()
                story = lines[i].split('根据故事：')[1].strip()
                content = lines[i + 1].split('诗歌：')[1].strip()

                json_entry = {
                    'classification': classification,
                    'story': story,
                    'content': content
                }

                json_data.append(json_entry)

                i += 2  # Move to the next set of lines
            else:
                i += 1  # Move to the next line

    return json_data


def save_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    txt_file = "E:\文本挖掘三\测试集分析\重新训练后的测试结果.txt"
    json_file = "E:\文本挖掘三\测试集分析\AgainOutput.json"

    data = parse_txt_to_json(txt_file)
    save_json(data, json_file)
    print("Conversion complete. JSON file saved as", json_file)
