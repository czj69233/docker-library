import os
import json
import requests
from pathlib import Path

# 设置 Contentful API 访问参数
CONTENTFUL_MANAGEMENT_API = "https://api.contentful.com"
ACCESS_TOKEN = os.environ['CONTENTFUL_ACCESS_TOKEN']
SPACE_ID = "ffrhttfighww"

# 设置请求头
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/vnd.contentful.management.v1+json"
}

def update_contentful(product_name, editions):
    # 获取 Contentful 中的 Product entry
    response = requests.get(
        f"{CONTENTFUL_MANAGEMENT_API}/spaces/{SPACE_ID}/environments/master/entries?content_type=product&fields.key={product_name}",
        headers=headers
    )
    response.raise_for_status()
    entries = response.json()
    # 打印返回的数据
    print(json.dumps(entries, indent=2))
