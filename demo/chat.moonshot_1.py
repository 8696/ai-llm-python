from openai import OpenAI

import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))

from ai_key import MOONSHOT_API_KEY


# 最近三个月购买的商品
buy_list = [
    {
      "name": "iphone 12", "price": 5000, "category": "手机"
    },
    {
      "name": "索尼（SONY）Alpha 7 IV", "price": 280000, "category": "数码相机"
    },
    {
      "name": "金士顿（Kingston）64GB USB3.2 Gen 1 U盘", "price": 34, "category": "数码配件"
    },
    {
      "name": "清风抽纸 原木2层200抽*20包", "price": 39, "category": "日用品"
    }
  ]

# 最近十条浏览产品记录
view_list = [
    {
      "name": "iphone 16", "price": 5000, "category": "手机", "id": "1"
    },
    {
      "name": "索尼（SONY）Alpha 7 IV", "price": 280000, "category": "数码相机", "id": "2"
    },
    {
      "name": "金士顿（Kingston）64GB USB3.2 Gen 1 U盘", "price": 34, "category": "数码配件", "id": "3"
    },
    {
      "name": "扩展坞", "price": 199, "category": "数码配件", "id": "4"
    },
    {
      "name": "充电器", "price": 69, "category": "数码配件", "id": "5"
    },
    {
      "name": "type-c数据线", "price": 79, "category": "数码配件", "id": "6"
    },
    { 
      "name": "Apple Watch Series 6", "price": 3999, "category": "手表", "id": "7"
    },
    {
      "name": "MacBook Pro 16寸", "price": 14999, "category": "电脑", "id": "8"
    },
    {
      "name": "小米10", "price": 3999, "category": "手机", "id": "9"
    },
    {
      "name": "维达（Vinda）抽纸 超韧3层150抽*24包", "price": 46, "category": "日用品", "id": "10"
    },
    {
      "name": "清扬（CLEAR）男士去屑洗发水活力运动薄荷型", "price": 69, "category": "日用品", "id": "11"
    },
]

question = (
  "根据下面我给出的用户行为数据，你觉得用户大概率会购买浏览过的哪个商品？为什么？"+
  "行为数据如下："+
  "用户一年前购买的商品清单：" +
  # "用户最近三个月购买的商品清单：" +
  json.dumps(buy_list, ensure_ascii=False) + 
  "，最近十天浏览产品记录：" + 
  json.dumps(view_list, ensure_ascii=False) 
)



system_content = (
  "你是商城app智能推荐助手，根据用户购买记录和浏览记录，在商城首页推荐模块推荐用户可能感兴趣的商品给用户。需要额外提几个要求：" +
  "1、需要考虑商品的生命周期、换新周期；" +
  "2、需要考虑用户的消费能力；" +
  "3、需要考虑可能购买商品的真实需求；" +
  "4、你回答问题的格式是只回答浏览商品的ID就行，例如 ['id1', 'id2]，分析原因不用回答；"
)
print(system_content)
print(question)

client = OpenAI(
    api_key = MOONSHOT_API_KEY,
    base_url = "https://api.moonshot.cn/v1",
)

completion = client.chat.completions.create(
    model = "moonshot-v1-32k",
    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": question}
    ],
    temperature = 0.3,
)
 
print('---------------')

print(completion.choices[0].message.content)