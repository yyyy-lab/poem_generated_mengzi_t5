import json
from collections import defaultdict
import matplotlib.pyplot as plt

# 读取并合并JSON文件
data = []
#for filename in [ 'E:\文本挖掘三\\finalData\\reqData.json']:
for filename in ['E:\文本挖掘三\\finalData\deal21868lvshi.json','E:\文本挖掘三\\finalData\deal13655jueju.json']:
#for filename in ['E:\文本挖掘三\\finalData\\tweThousand.json']:
    with open(filename, 'r', encoding='utf-8') as f:
        data += json.load(f)

# 根据内容去重
unique_data = {entry['s_content']: entry for entry in data}.values()

# 根据分类计数
classification_counts = defaultdict(int)
for entry in unique_data:
    classification_counts[entry['classification']] += 1

# 可视化结果
labels = classification_counts.keys()
counts = classification_counts.values()

plt.bar(labels, counts)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 指定中文字体
plt.xlabel('Classification')
plt.ylabel('Count')
plt.title('No.1 Classification Counts')
plt.savefig("newTrain_classification.png")
plt.show()

