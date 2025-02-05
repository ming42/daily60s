import json
import requests
from notify import send

def load_api_config():
    """加载API配置文件"""
    try:
        with open('api.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception("API配置文件未找到")
    except json.JSONDecodeError:
        raise Exception("API配置文件格式错误")

def fetch_news(url):
    """获取每日新闻"""
    print("🔍 正在获取每日新闻...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"获取每日新闻失败: {e}")

    try:
        news_data = response.json()
        if "data" not in news_data or not news_data["data"]:
            raise Exception("新闻数据不存在或为空")
        news_list = news_data["data"].get("news", [])
        weiyu = news_data["data"].get("weiyu", "")
        image = news_data["data"].get("image", "")
        if not news_list:
            raise Exception("新闻列表为空")
        news_content = "\n".join(news_list) + "\n\n微语：" + weiyu + "\n\n" + f"![image]({image})"
        print("✅ 新闻获取成功")
        return news_content
    except (json.JSONDecodeError, KeyError) as e:
        raise Exception(f"解析新闻数据失败: {e}")

def main():
    try:
        config = load_api_config()
        title = "每天60秒读懂世界"
        content = fetch_news(config["news_api"])
        result = f'{content}'
        send(title, result)
        print("✅ 推送已完成，请检查推送结果")
    except Exception as e:
        print(f"❌ 每日新闻获取失败: {e}")

if __name__ == "__main__":
    main()