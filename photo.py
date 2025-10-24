import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')





images = [{'url':'https://facts.net/wp-content/uploads/2023/07/pufferfish-cute-.jpg','parm':'🐟鱼🐟'},
          {'url':'https://animalcorner.org/wp-content/uploads/2015/02/british-wild-cat-1.jpg','parm':'🐈猫🐈'},
          {'url':'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg','parm':'🐦鸟🐦'},
          {'url':'https://site-547756.mozfiles.com/files/547756/medium/Dog2.jpg','parm':'🐕狗🐕'}]

if 'tp'not in st.session_state:
    st.session_state['tp'] = 0

def nextImg():
    st.session_state['tp'] = (st.session_state['tp'] + 1) % len(images)
def nextImg1():
    st.session_state['tp'] = (st.session_state['tp'] - 1) % len(images)
    



st.image(images[ st.session_state['tp']]['url'],caption=images[st.session_state['tp']]['parm'])

c1,c2 = st.columns(2)

with c1:
    st.button('上一张', on_click=nextImg1,use_container_width=True)

with c2:
    st.button('下一张', on_click=nextImg, use_container_width=True)
