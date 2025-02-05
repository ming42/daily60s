import json
import requests
from bs4 import BeautifulSoup
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

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取年份
    year_tag = soup.find('p', string=lambda t: t.strip() == '2025')
    year = year_tag.get_text(strip=True) if year_tag else "2025"

    # 提取日期
    date_tag = soup.find('h2', string=True)
    date = date_tag.get_text(strip=True) if date_tag else ""

    # 提取星期和农历日期
    md_div = soup.find('div', id='md')
    ymd_div = soup.find('div', id='ymd')
    lunar_date = md_div.get_text(strip=True) if md_div else ""
    ymd_text = ymd_div.get_text(strip=True) if ymd_div else ""

    full_date = f"{year}年{date} {lunar_date}\n{ymd_text}"

    # 提取新闻
    news_list = []
    news_title_tag = soup.find('h1', string='「60秒读懂世界」')
    if news_title_tag:
        news_section = news_title_tag.find_next('ul')
        if news_section:
            news_list = [item.find('a').get_text(strip=True) for item in news_section.find_all('li') if item.find('a')]

    news = ''
    for news_item in news_list:
        news += f'{news_item}\n'
    result = f'{full_date}\n\n{news}'
    print("✅ 新闻获取成功")
    return result

def main():
    try:
        config = load_api_config()
        title = "每天60秒读懂世界"
        result = fetch_news(config["news_api"])
        image_api = config["image_api"]
        content = f"{result}\n\n![image]({image_api})"
        print("🚀 新闻推送中...")
        send(title, content)
        print("✅ 推送已完成，请检查推送结果")
    except Exception as e:
        print(f"❌ 每日新闻获取失败: {e}")

if __name__ == "__main__":
    main()