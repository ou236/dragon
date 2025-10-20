import streamlit as st
import pandas as pd
st.title("🦱学生  小崔  数字档案")

st.header('🚩基础信息')

st.text("学生ID：NEO-2026-6-27|精神状态:✔️累")

st.text("当前位置：中国")
st.markdown('保密等级：:red[SSS]')

st.title('拥有技能')

c1, c2, c3 = st.columns(3)
c1.metric(label="烹饪技巧", value="99%", delta="+1%")
c2.metric(label="工作能力", value="66%", delta="6%")
c3.metric(label="经济能力", value="50", delta="0", delta_color="off")

st.title('')
data = {
    '交易数量':[999, 999, 1000, 1000, 2000],
    '成功数量':[999, 884, 768, 524, 709],
    '正在交易数量':[577, 532, 996, 929, 694],
}

index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')

df = pd.DataFrame(data, index=index)

st.subheader('个月的交易量')
st.dataframe(df)

st.subheader('代码模块')
python_code = '''def matrix_breach():
    while True:
        if detect_vulnerablity():
            exploit()
            return "ACCESS GRANTD"
        else:
            stealth_evade()
'''
st.code(python_code, line_numbers=True)

st.markdown('***')
st.markdown(':green[>>SYSTEM MESSAGE:]'"下一个任务目标已解锁...")
st.markdown(':green[>>TARGET:]'"课程管理系统")
st.markdown(':green[>>COUNTDOWN:]'"2025-06-03 15:24:58")
st.text("系统状态：在线 连接状态：已加密")
