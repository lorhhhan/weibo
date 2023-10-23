from transformers import BertTokenizer

#加载字典和分词工具，即tokenizer
token = BertTokenizer.from_pretrained('H:/huggingface/bert-base-chinese')  # 要跟预训练模型相匹配
token
tokenizer = BertTokenizer.from_pretrained('H:/bert-base-uncased')
tokenizer
from transformers import BertModel

#加载预训练模型
pretrained = BertModel.from_pretrained('H:/huggingface/bert-base-chinese')
print(pretrained)