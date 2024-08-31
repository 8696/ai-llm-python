from openai import OpenAI

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))

from ai_key import MOONSHOT_API_KEY

print(MOONSHOT_API_KEY)

client = OpenAI(
    api_key = MOONSHOT_API_KEY,
    base_url = "https://api.moonshot.cn/v1",
)

# 示例用户和新商品
user = {
    "name": "张三",
    "phone_number": "1234567890",
    "browsing_history": ["运动鞋", "跑步机"],
    "purchase_history": ["健身器材"],
    "inquiry_history": ["需要更多运动装备"]
}

# new_product = "耐克S1000 运动鞋"
new_product = "macbook pro"

question = (
    f"用户的兴趣数据如下：\n"
    f"浏览记录：{user['browsing_history']}\n"
    f"购买记录：{user['purchase_history']}\n"
    f"咨询记录：{user['inquiry_history']}\n"
    f"新商品信息：{new_product}\n\n"
    f"请判断这个用户是否可能喜欢这款新商品。如果可能，请用'喜欢'回复；如果不可能，请用'不喜欢'回复"
)
 
completion = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        {"role": "system", "content": "你是电商app的助手，我问你问题时你只需要回复喜欢或不喜欢就行了，不需要给出具体的原因。"},
        {"role": "user", "content": question}
    ],
    temperature = 0.3,
)
 
print(completion.choices[0].message.content)