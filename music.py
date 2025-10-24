import streamlit as st

#修改标题
st.set_page_config(page_title='音乐', page_icon='🎵')
#这个是对象组
music = [
           {'url':'https://music.163.com/song/media/outer/url?id=2756303345.mp3',
           'photo':'https://p1.music.126.net/IDAl-BxdZpWpNb-_3r_Shg==/109951172160870872.jpg?param=180y180',
           'author':'歌手：陈奕迅',
           'name':'K歌之王',
           'time':'时间：3:41'
            },
          
          {'url':'https://music.163.com/song/media/outer/url?id=2707033683.mp3',
           'photo':'https://p1.music.126.net/p4U0-Y5rtkKfDmQegHXpVQ==/109951172068954764.jpg?param=180y180',
           'name':'吻你吻上天空',
           'author':'歌手：曾舜晞',
           'time':'时间：3:07'},
          
          {'url':'https://music.163.com/song/media/outer/url?id=5257138.mp3',
           'photo':'https://p2.music.126.net/81BsxxhomJ4aJZYvEbyPkw==/109951165671182684.jpg?param=180y180',
           'name':'屋顶',
           'author':'歌手：周杰伦',
           'time':'时间：5:19'}
              ]

if 'tp'not in st.session_state:
    st.session_state['tp'] = 0
#按钮
def nextImg():
    st.session_state['tp'] = (st.session_state['tp'] + 1) % len(music)
def prevImg():
    st.session_state['tp'] = (st.session_state['tp'] - 1) % len(music)
    

a1,a2 = st.columns([1,2])
with a1:
    st.image(music[st.session_state['tp']]['photo'])

with a2:
    st.title(music[st.session_state['tp']]['name'])
    st.text(music[st.session_state['tp']]['author'])
    st.text(music[st.session_state['tp']]['time'])


    
st.audio(music[st.session_state['tp']]['url'])




#分裂
c1,c2 = st.columns(2)

with c1:
    st.button('上一首', on_click=prevImg,use_container_width=True)

with c2:
    st.button('下一首', on_click=nextImg,use_container_width=True)
