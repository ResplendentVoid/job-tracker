import requests
import pandas as pd
import datetime


def fetch_v2ex_jobs():
    print("🚀 开始抓取 V2EX 酷工作节点最新真实岗位...")

    # V2EX 官方提供的免费 API 接口
    url = "https://www.v2ex.com/api/topics/show.json?node_name=jobs"

    # 伪装成浏览器，防止被服务器拒绝 (反爬虫基础操作)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # 发送网络请求获取数据
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果网络报错，抛出异常

        # 将返回的 JSON 数据转换为 Python 字典列表
        topics = response.json()

        job_list = []
        today = datetime.date.today().strftime("%Y-%m-%d")

        # 遍历抓取到的每一条帖子
        for topic in topics:
            title = topic.get("title", "")
            url = topic.get("url", "")

            # 组装成我们需要的格式
            job_list.append({
                "公司/城市": "详见标题 (社区直招)",  # V2EX 的标题通常自带城市和公司名
                "岗位": title,
                "薪资": "面议/详见链接",
                "工作氛围/标签": "V2EX 社区直招",
                "预估加班程度": "⭐⭐⭐",  # 目前默认给3星，这是我们下一步要用 AI 去分析的重点！
                "直达链接": url,
                "更新日期": today
            })

        # 将列表转换为 Pandas 的数据表格
        df = pd.DataFrame(job_list)

        # 保存为 CSV 文件覆盖旧的模拟数据
        df.to_csv("jobs_data.csv", index=False, encoding="utf-8-sig")
        print(f"✅ 成功抓取 {len(job_list)} 条真实岗位数据，已更新 jobs_data.csv！")

    except Exception as e:
        print(f"❌ 抓取失败，错误信息: {e}")


if __name__ == "__main__":
    fetch_v2ex_jobs()