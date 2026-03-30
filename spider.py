import pandas as pd
import datetime


def fetch_daily_jobs():
    # 这里是你未来的爬虫逻辑，去抓取开源 API 或网页
    # 现在我们用模拟数据代替，确保你能立刻看到效果
    today = datetime.date.today().strftime("%Y-%m-%d")

    # 假设这是你抓取并清洗后的数据
    mock_data = [
        {"公司": "字节跳动", "岗位": "自动化测试工程师", "薪资": "20k-40k", "工作氛围/标签": "技术驱动, 弹性工作",
         "预估加班程度": "⭐⭐⭐⭐⭐", "更新日期": today},
        {"公司": "大疆创新", "岗位": "机器人算法工程师", "薪资": "25k-50k", "工作氛围/标签": "硬件极客, 扁平管理",
         "预估加班程度": "⭐⭐⭐⭐", "更新日期": today},
        {"公司": "某外企", "岗位": "PLC控制工程师", "薪资": "15k-25k", "工作氛围/标签": "WLB, 拒绝内卷",
         "预估加班程度": "⭐", "更新日期": today},
    ]

    df = pd.DataFrame(mock_data)
    # 保存为 CSV 文件，这就是你的“轻量级数据库”
    df.to_csv("jobs_data.csv", index=False, encoding="utf-8-sig")
    print(f"✅ {today} 的招聘数据已更新并保存到 jobs_data.csv")


if __name__ == "__main__":
    fetch_daily_jobs()