# poem_generated_mengzi_t5
根据场景描述创作对应的古诗AI

训练数据：
第一部分：21868条律诗唐诗和 13655条绝句唐诗。
来源：https://github.com/chinese-poetry/chinese-poetry
获取poet.tang.[0-49].json共50000条唐诗
繁体字转为简体字
进行古诗分类：五言绝句，五言律诗，七言绝句，七言律诗，其他诗
保留21868条律诗；保留13655条绝句


第二部分：835条story与古诗对应的数据
爬取古诗文网https://so.gushiwen.cn/上所有分类为唐诗三百，宋词300，春天，高中古诗，写花，离别，励志，思念，写人，咏物，月亮的古诗。
将{诗名，诗人，古诗内容，创作背景+译文}作为一组数据进行爬取。
共爬取到2985条数据，对数据进行诗词分类，只保留五言绝句，五言律诗，七言绝句，七言律诗，得到835条数据。


第三部分：872条story与古诗对应的数据
爬取古诗文网https://so.gushiwen.cn/上所有分类为春天，夏天，秋天，冬天，韩愈，陆游，王维，杜甫，宋代，五代，唐代，隋代的所有古诗。
将{诗名，诗人，古诗内容，译文}作为一组数据进行爬取。
得到1860条数据,对爬取到的数据进行诗歌分类，只保留五言绝句，五言律诗，七言绝句，七言律诗，剩下1100，去重后得到872条数据。

!(https://github.com/yyyy-lab/poem_generated_mengzi_t5/edit/main/train_data/图片1.png)
3部分数据放到一起去重后得到36797条数据，其中0.02作为验证集，0.98作为训练数据

模型：Mengzi-T5 model (Chinese)，https://github.com/Langboat/Mengzi?tab=readme-ov-file

对Pretrained T5 进行“写诗 prompt” fine-tuning：
prompt设定：  “作诗一首” + 诗歌类别 +“：”+ 诗名 +“ </s>” +“根据故事：”+故事 或 “作诗一首” + 诗歌类别 +“：”+ 诗名

两种指令形式：
  {instruction：要求+故事，output：诗句}
和
  {instruction：要求，output：诗句}

标题长度限制12token，诗人4token，诗歌64token.
输入的长度限制为：4+4+1+ 16 +  1 + 4+1 + 300（故事最长为300）.
输出长度限制为：64（最多只能生成七言律诗）.
