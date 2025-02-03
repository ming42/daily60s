import requests
from python.notify import send

def fetch_and_format_news():
    print("🔍 正在获取每日新闻...")

    # 获取新闻内容
    response = requests.get("https://60s.viki.moe/?encoding=text", timeout=10)
    response.raise_for_status()
    raw_content = response.text
    print("✅ 新闻获取成功")

    # 格式化新闻内容
    print("✅ 正在格式化新闻文本...")
    formatted_content = raw_content.replace('\n', '\n')
    formatted_content += "\n\n![图片](https://api.03c3.cn/api/zb)"
    print("✅ 新闻文本格式化完成")

    return formatted_content

def main():
    try:
        content = fetch_and_format_news()
        title = "每天60秒读懂世界"
        send(title, content)
        print("✅ 推送已完成，请检查推送结果")
    except Exception as e:
        print(f"❌ 每日新闻获取失败: {e}")

if __name__ == "__main__":
    main()