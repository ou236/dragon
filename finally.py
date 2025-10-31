 
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import joblib
st.set_page_config(page_title="学生成绩预测", page_icon="", layout="wide")

def load_data():
    df = pd.read_csv(r'student_data_adjusted_rounded.csv') 
    return df
df = load_data()

model = joblib.load("score_predictor.pkl") 

page = st.sidebar.radio("导航菜单", ["项目介绍", "专业数据分析", "期末成绩预测"])

if page == "项目介绍":
    st.title("‍🎓学生成绩分析与预测系统")
    st.markdown('***')
    c1,c2 = st.columns([2,1])
    with c1:
        st.header("📖项目概述")
        st.markdown("本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。")  
        st.markdown('### 主要特点：')
        st.markdown('·📊数据可视化：多维度展示学生学业数据')
        st.markdown('·🎯专业分析：按专业分类的详细统计分析')
        st.markdown('·🧠智能预测：基于机器学习模型的成绩预测')
        st.markdown('·💡学习建议：根据预测结果提供个性化反馈')
    with c2:

        images = [{'url':'屏幕截图(1).png','parm':"这是各专业男女比例和每周学习时长期中期末分数对比图"},
          {'url':'屏幕截图(2).png','parm':"这是各专业的出勤率分析和大数据管理专业项分析的分析图"},
          {'url':'屏幕截图(3).png','parm':"这是从5万条数据中，为我们预测在多少的出勤率，期中成绩，每周学习时长下可以做到期末成绩合格的图片"}]

        if 'tp'not in st.session_state:
            st.session_state['tp'] = 0

        def nextImg():
            st.session_state['tp'] = (st.session_state['tp'] + 1) % len(images)
        def nextImg1():
            st.session_state['tp'] = (st.session_state['tp'] - 1) % len(images)
            



        st.image(images[ st.session_state['tp']]['url'],caption=images[st.session_state['tp']]['parm'])

        d1,d2 = st.columns(2)

        with d1:
            st.button('上一张', on_click=nextImg1,use_container_width=True)

        with d2:
            st.button('下一张', on_click=nextImg, use_container_width=True)



    st.markdown('***')
    st.header("🚀项目目标")

    a1,a2,a3 = st.columns(3)
    with a1:
        st.markdown('### 🎯目标一')
        st.markdown('分析影响因素')
        st.markdown('·识别关键学习指标')
        st.markdown('·探索成绩相关因素')
        st.markdown('·提供数据支持决策')
    with a2:
        st.markdown('### 📊目标二')
        st.markdown('可视化展示')
        st.markdown('·专业对比分析')
        st.markdown('·性别差异研究')
        st.markdown('·学习模式识别')
    with a3:
        st.markdown('### 🔮目标三')
        st.markdown('成绩预测')
        st.markdown('·机器学习模型')
        st.markdown('·个性化预测')
        st.markdown('·及时干预预警')



        
    st.markdown('***')
    st.header("🛠技术架构")
    b1,b2,b3 = st.columns(3)
    with b1:
        st.markdown('前端框架')
        st.markdown('Streamlit')

    with b2:
        st.markdown('数据处理')
        st.markdown('Pandas')
        st.markdown('NumPy')

    with b3:
        st.markdown('可视化')
        st.markdown('Plotly')
        st.markdown('Matpotlib')












elif page == "专业数据分析":
    st.title("📊 专业数据分析中心")
    

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">1. 各专业男女性别比例</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        gender_fig = px.histogram(
            df, 
            x="专业", 
            color="性别", 
            barmode="group",
            title="各专业男女性别分布",
            color_discrete_map={"男": "#2563eb", "女": "#f43f5e"},
            labels={"count": "人数", "专业": "专业名称"},
            height=300
        )
        gender_fig.update_layout(
            plot_bgcolor="#1e293b",
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="#f8fafc"
        )
        st.plotly_chart(gender_fig, use_container_width=True)
    
    with col2:
        gender_data = df.groupby(["专业", "性别"])["学号"].count().reset_index()
        gender_pivot = gender_data.pivot(index="专业", columns="性别", values="学号").fillna(0).astype(int)
        st.subheader("性别比例数据")
        st.dataframe(gender_pivot, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">2. 各专业学习指标对比</h2>', unsafe_allow_html=True)
    metrics = ["每周学习时长（小时）", "期中考试分数", "期末考试分数"]
    metric_df = df.groupby("专业")[metrics].mean().reset_index()
    col1, col2 = st.columns([2, 1])

    with col1:

        fig = go.Figure()


        fig.add_trace(
            go.Bar(
                x=metric_df["专业"],
                y=metric_df["每周学习时长（小时）"],
                name="每周学习时长",
                yaxis="y1"
            )
        )


        fig.add_trace(
            go.Line(
                x=metric_df["专业"],
                y=metric_df["期中考试分数"],
                name="期中考试分数",
                yaxis="y2"
            )
        )
        fig.add_trace(
            go.Line(
                x=metric_df["专业"],
                y=metric_df["期末考试分数"],
                name="期末考试分数",
                yaxis="y2"
            )
        )


        fig.update_layout(
            title="各专业学习时间与成绩对比",
            yaxis=dict(
                title="每周学习时长（小时）",
                side="left"
            ),
            yaxis2=dict(
                title="分数",
                side="right",
                overlaying="y"
            ),
            xaxis=dict(title="专业"),
            plot_bgcolor="#1e293b",  
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="#f8fafc",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("详细数据")
        st.dataframe(metric_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


    

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">3. 各专业出勤率分析</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        attendance_fig = px.density_heatmap(
            df, 
            x="专业", 
            y="上课出勤率",
            title="各专业出勤率分布热力图",
            color_continuous_scale="Viridis",
            labels={"专业": "专业名称", "上课出勤率": "出勤率"},
            height=300
        )
        attendance_fig.update_layout(
            plot_bgcolor="#1e293b",
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="#f8fafc"
        )
        st.plotly_chart(attendance_fig, use_container_width=True)
    
    with col2:
        attendance_rank = df.groupby("专业")["上课出勤率"].mean().reset_index()
        attendance_rank = attendance_rank.sort_values("上课出勤率", ascending=False)
        attendance_rank["排名"] = range(1, len(attendance_rank)+1)
        st.subheader("出勤率排名")
        st.dataframe(attendance_rank[["排名", "专业", "上课出勤率"]], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">4. 大数据管理专业专项分析</h2>', unsafe_allow_html=True)
    bd_major = df[df["专业"] == "大数据管理"]
    

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("平均出勤率", f"{bd_major['上课出勤率'].mean():.1%}")
    with col2:
        st.metric("期中平均分", f"{bd_major['期中考试分数'].mean():.1f}分")
    with col3:
        st.metric("期末平均分", f"{bd_major['期末考试分数'].mean():.1f}分")
    with col4:
        st.metric("平均学习时长", f"{bd_major['每周学习时长（小时）'].mean():.1f}小时")
    

    col1, col2 = st.columns(2)
    with col1:
        score_fig = px.histogram(
            bd_major,
            x="期末考试分数",
            title="大数据管理专业期末成绩分布",
            color_discrete_sequence=["#10b981"],
            nbins=10,
            height=300
        )
        score_fig.update_layout(
            plot_bgcolor="#1e293b",
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="#f8fafc"
        )
        st.plotly_chart(score_fig, use_container_width=True)
    
    with col2:
        hours_fig = px.box(
            bd_major,
            y="每周学习时长（小时）",
            title="大数据管理专业学习时长分布",
            color_discrete_sequence=["#f59e0b"],
            height=300
        )
        hours_fig.update_layout(
            plot_bgcolor="#1e293b",
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="#f8fafc"
        )
        st.plotly_chart(hours_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


else:
    st.title("🎯 期末成绩预测系统")
    st.markdown("通过输入学生的学习特征，系统将基于机器学习模型预测期末成绩并提供个性化建议")
    st.markdown("---")


    with st.form("predict_form", clear_on_submit=False):
        st.subheader("📝 学生学习信息录入")
        col1, col2 = st.columns(2)
        
        with col1:
            student_id = st.text_input("学号", placeholder="例如：2023001001")
            gender = st.selectbox("性别", ["男", "女"])
            major = st.selectbox("专业", df["专业"].unique())
            study_hours = st.slider(
                "每周学习时长（小时）", 
                min_value=0.0, max_value=50.0, step=0.5, value=15.0,
                help="学生平均每周投入学习的时长"
            )
        
        with col2:
            attendance = st.slider(
                "上课出勤率", 
                min_value=0.0, max_value=1.0, step=0.01, value=0.8,
                help="实际出勤课时/应出勤课时"
            )
            mid_score = st.slider(
                "期中考试分数", 
                min_value=0.0, max_value=100.0, step=1.0, value=70.0
            )
            homework_rate = st.slider(
                "作业完成率", 
                min_value=0.0, max_value=1.0, step=0.01, value=0.9,
                help="已完成作业数/总作业数"
            )
        
        submit_btn = st.form_submit_button("🔍 预测期末成绩", type="primary")


    if submit_btn and student_id:  

        X = [[study_hours, attendance, mid_score, homework_rate]]
        pred_score = model.predict(X)[0]
        pred_score = max(0, min(100, round(pred_score, 1)))  


        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        st.subheader(f"📊 学号 {student_id} 的预测结果")
        

        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f'<div class="result-highlight">{pred_score} 分</div>', unsafe_allow_html=True)
        with col2:
            st.progress(pred_score / 100)  
        

        if pred_score >= 90:
            st.success("🌟 成绩等级：优秀")
            st.image("https://imgs.699pic.com/images/401/430/829.jpg!list1x.v2", width=200)
        elif pred_score >= 80:
            st.success("👍 成绩等级：良好")
            st.image("https://pic.mksucai.com/00/19/14/988152f4d1b0b2fd.webp",width=200)
        elif pred_score >= 60:
            st.info("✅ 成绩等级：合格")
            st.image("https://img.ixintu.com/download/jpg/20210125/032c3c715edf24264befa485d75bd933_512_512.jpg!ys", width=200)
        else:
            st.warning("⚠️ 成绩等级：待提高")
            st.image("https://pic.616pic.com/ys_bnew_img/00/24/30/fOcjochnUv.jpg", width=200)
        

        st.markdown('<div class="advice-box">', unsafe_allow_html=True)
        st.subheader("💡 学习建议")
        if attendance < 0.7:
            st.markdown("- 建议提高出勤率，课堂互动对成绩影响显著")
        if homework_rate < 0.8:
            st.markdown("- 需加强作业完成质量，作业是巩固知识的关键")
        if study_hours < 10:
            st.markdown("- 建议增加每周学习时长，保证足够的知识消化时间")
        if pred_score < 60:
            st.markdown("- 可针对性复习期中考试薄弱环节，必要时寻求老师帮助")
        else:
            st.markdown("- 保持当前学习状态，建议定期总结知识体系，查漏补缺")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif submit_btn:
        st.error("请输入学号后再进行预测")
