import streamlit as st
st.markdown('# 👨‍⚕干员 罗伊.斯米-数字档案')
st.markdown('# ✉基础信息')
st.markdown('🐝代号：'':green[哈基蜂]')
st.markdown('📅出生日期：'':green[2008.2.23]')
st.markdown('📏身高：'':green[176cm]')
st.markdown('体重：'':green[75kg]')


st.title('🛠技能')
# 定义列布局，分成3列
c1, c2, c3,c4 = st.columns(4)
c1.metric(label="被动", value="专业救援", delta="+100%")
c2.metric(label="技能1", value="激素枪", delta="+50%")
c3.metric(label="技能2", value="烟幕")
c4.metric(label="技能3", value="烟雾弹", delta="2")

st.title('📔干员任务')
import streamlit as st  # 导入Streamlit并用st代表它
import pandas as pd

data = {
    '1号任务':["让我再救一个", "完成"],
    '2号任务':["成功撤离", "完成"],
    '3号任务':["击败所有特殊兵种", "完成"],
}
# 定义数据框所用的索引
index = pd.Series(['目标',['状态']], name='任务')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.header('')
st.write(df)
st.subheader('成就')
python_code = '''def hello():
    print("G.T.I最佳干员")
'''
st.code(python_code,line_numbers=True)


st.markdown('***')
st.markdown(':green[>> SYSTEM MESSAGE:]''下个任务目标已解锁')
