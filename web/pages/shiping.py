import streamlit as st


video_file = [{'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/82f434005145403703273697144/v.f100830.mp4',
               'title':'人民网',
               'episode':'一缕阳光|暖意长留',
               'time':'2025年10月24日',
               'author':'责编：候自聪'
               },
              {'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/2d0eb44f5145403703160061228/v.f100830.mp4',
               'title':'人民网',
               'episode':'这一刻，没有竞争，只有致敬',
               'time':'2025年10月23日',
               'author':'责编：候自聪'
               },
              {'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/7e3905485145403703273489963/v.f100830.mp4',
               'title':'人民日报',
               'episode':'这些建筑、古村落、很潮范儿',
               'time':'2025年10月25日',
               'author':'责编：候自聪'
               }]


if 'tp' not in st.session_state:
    st.session_state['tp'] = 0
st.text(video_file[st.session_state['tp']]['title'])
st.text(video_file[st.session_state['tp']]['episode'])
st.text(video_file[st.session_state['tp']]['time'])

st.video(video_file[st.session_state['tp']]['url'])

c1,c2,c3,c4,c5,c6 = st.columns(6)
with c6:
    st.text(video_file[st.session_state['tp']]['author'])
def play(arg):
   
    st.session_state['tp'] = int(arg)

    
df = st.columns(4)
di=min(4,len(video_file))
for i in range(len(video_file)):
    col_index=i%di
    with df[col_index]:
        st.button(f'第{i + 1}集',use_container_width=True,on_click=play,args=(i,))
