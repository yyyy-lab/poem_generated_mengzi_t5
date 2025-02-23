import re
import requests

url = requests.get("https://so.gushiwen.cn/gushi/tangshi.aspx")#唐诗300
# url = requests.get("https://so.gushiwen.cn/gushi/libie.aspx")#libie古诗
# url = requests.get("https://so.gushiwen.cn/gushi/zheli.aspx")#高中古诗
# url = requests.get("https://so.gushiwen.cn/gushi/songsan.aspx")#宋词300
data = url.text
data2 = re.findall(r'<span><a href="(.*?)" target="_blank">(.*?)</a>(.*?)</span>', data)
# print(data2[0])

data = []
for i in data2:
    url2 = 'https://so.gushiwen.cn/' + i[0]
    # url2 = i[0]
    # print(url2)
    data2 = requests.get(url2).text

    # print(data2)
    gushi = re.findall('name="description" content="(.*?)" /', data2)
    # gushi = re.sub(r"[\[\]']", '',str(re.findall('name="description" content="(.*?)" /',data2)))
    # yiwen1 = re.findall('<p><strong>译文</strong><br />(.*?)<br />',data2)
    yiwen2 = re.findall('<p><strong>译文</strong><br />(.*?)。</p>',data2)
    yiwenshai = re.sub(r"[a-z0-9.,_=\[\]<br />']", '', str(yiwen2))
    # beijing = re.findall('[\u4e00-\u9fa5]+',str(re.findall('<p>　　(.*?)。</p>',data2)))
    # beijing = re.sub(r"[a-z0-9.,_=\[\]<br />']", '',str(re.findall('<p>　　(.*?)。</p>',data2)))
    # print(f'诗名：{i[1]}，作者：{i[2]}，古诗内容：{gushi},译文：{yiwenshai+"。"},背景：{str(beijing)+"。"}')
    print(f'诗名：{i[1]}，作者：{i[2]}，古诗内容：{gushi},译文：{yiwenshai + "。"}')
    data.append({"poem_name":i[1],"author":i[2],"content":gushi,"story":yiwenshai})

print(data)

import json



# # 指定要保存的JSON文件路径
# # file_path = 'songci300poemdata.json'
# file_path = 'chuzhonggushi300poemdata.json'
#
# # 将数据写入JSON文件
# with open(file_path, 'w') as json_file:
#     json.dump(data, json_file)