import pandas as pd
from cemotion import Cemotion
from transformers import BertTokenizer
from transformers import BertModel
c = Cemotion()
import time
token = BertTokenizer.from_pretrained('H:/huggingface/bert-base-chinese')  # 要跟预训练模型相匹配
tokenizer = BertTokenizer.from_pretrained('H:/huggingface/bert-base-chinese')

start = time.perf_counter()  # 程序运行前的当前时刻

df = pd.read_excel(r'H:\content.xlsx',engine='openpyxl')
#定义函数，批量处理所有的评论信息
def get_sentiment_cn(text):
    return c.predict(text)
#根据df里的“comments”列，将读取文本后的情感分析结果添加到新的一列，命名为“sentiment”
df["话题情感"] = df['话题内容'].apply(get_sentiment_cn)
print(df)
#储存为表格。
data1=df.to_excel(r'H:\Cemotioncontent.xlsx')
#输出程序运行时间
elapsed = (time.perf_counter() - start)#结束后计时-开始前计时
print("Time used:%s 秒"%elapsed)
