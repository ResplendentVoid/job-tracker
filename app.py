import streamlit as st
import pandas as pd

# 设置网页标题和布局
st.set_page_config(page_title="大学生招聘信息聚合器", layout="wide")

st.title("🚀 每日最新招聘与公司打工人真实评价聚合")
st.markdown("自动更新全网最新招聘信息，结合开源黑白名单，帮你避坑！")


# 读取刚才爬虫生成的 CSV 数据
@st.cache_data  # 缓存数据，提升网页加载速度
def load_data():
    try:
        return pd.DataFrame(pd.read_csv("jobs_data.csv"))
    except:
        return pd.DataFrame()


df = load_data()

if not df.empty:
    # 侧边栏：添加过滤功能
    st.sidebar.header("条件筛选")
    job_title = st.sidebar.text_input("搜索岗位名称")
    max_overtime = st.sidebar.selectbox("可接受最大加班程度", ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"])

    # 简单的数据过滤逻辑
    filtered_df = df.copy()
    if job_title:
        filtered_df = filtered_df[filtered_df["岗位"].str.contains(job_title)]

    # 展示数据表格
    st.dataframe(filtered_df, use_container_width=True)

    # 画个简单的图表分析一下当前薪资或岗位分布（扩展功能）
    st.subheader("📊 快速数据预览")
    st.bar_chart(filtered_df["预估加班程度"].value_counts())
else:
    st.warning("暂无数据，请等待爬虫更新。")