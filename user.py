import streamlit as st
from PIL import Image
import io
st.set_page_config(layout="wide")
st.title("个人简历生成器")
# 拆分左右栏：左栏表单，右栏预览
c1, c2 = st.columns([1, 2])
with c1:
    st.subheader("个人信息表单")
    st.markdown("***")
    name = st.text_input("姓名")
    position = st.text_input("职位")
    gender = st.radio("性别", ["男", "女", "其他"], horizontal=True)
    phone = st.text_input("电话")
    email = st.text_input("邮箱")
    birth_date = st.date_input("出生日期")
    education = st.selectbox("学历", ["高中","本科", "硕士", "博士"])
    communication = st.selectbox("沟通能力",["Choose an option","优秀","良好","一般"])
    skills = st.multiselect("技能", ["Python", "SQL", "Excel", "沟通能力"])
    intro = st.text_area("个人简介",height=100)
    work_exp = st.slider("工作经验（年）",0,30,0)
    salary_range = st.slider("期望薪资范围（元）",8000,5000,(10000,20000))
    contact_time = st.time_input("每日最佳联系时间段")
    avatar = st.file_uploader("上传头像", type=["jpg", "png"])
with c2:
    st.subheader("简历实时预览")
    st.markdown("***")
# 模拟简历布局：姓名 + 基本信息 + 个人简介 + 技能
# 显示上传的头像
    a1,a2 = st.columns(2)
    with a1:
        if avatar:
            img = Image.open(avatar)
            st.image(img, width=100, caption="个人头像")
        st.markdown(f"# {name}")
        st.write(f"性别：{gender} | 学历：{education} | 出生日期：{birth_date}")
        st.write(f"电话：{phone} | 邮箱：{email}")
    with a2:
        st.write(f"沟通能力：{communication} | 工作经验：{work_exp}年 | 期望薪资：{salary_range[1]}元")
        st.write(f"最佳联系时间：{contact_time}")

        st.subheader("专业技能")
        st.write(", ".join(skills))
    st.subheader("个人简介")
    st.write(intro)
