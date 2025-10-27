import streamlit as st

st.title("主页")
tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["数字档案", "美食地图", "相册","音乐播放器","视频网站","个人简历生成器"])

with tab1:    
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

with tab2:
    import pandas as pd
    st.subheader('🗺️店铺所在地')
    map_data = {
        'latitude':[22.854160, 22.840392, 22.838409, 22.841667, 22.847446],
        'longitude':[108.222322, 108.245341, 108.217607, 108.245700, 108.220922],
        }
    st.map(pd.DataFrame(map_data))

    st.subheader('🍽1-3到店人数')
    data = {
        '恰好铺子':[200, 150, 180],
        '重庆小面':[120, 160, 123],
        '兰师傅柳州螺蛳粉':[110, 100, 160],
        '蜜雪冰城':[512,625,456],
        '兰州拉面':[545,523,342],
    }

    df = pd.DataFrame(data)
    index = pd.Series(["1月", "2月", "3月",], name='月份')
    df.index = index
    st.dataframe(df)
    st.line_chart(df)
    st.subheader('⭐评分')
    data = {
        '恰好铺子':[8.2,8.6,8.4,8.4],
        '重庆小面':[8.5,8.6,8.7,8.8],
        '兰师傅柳州螺蛳粉':[9.2,9.4,8.5,9.3],
        '蜜雪冰城':[9.5,9.3,8.6,9.4],
        '兰州拉面':[9.5,9.3,9.4,7.4],
    }

    df = pd.DataFrame(data)
    index = pd.Series(["早餐","午餐","晚餐","下午茶"], name='评分')
    df.index = index
    st.bar_chart(df)
    st.subheader('💸1-12月的价格')
    data = {
        '恰好铺子':[30,31,35,14,15,13,31,54,32,34,31,21],
        '重庆小面':[21,12,42,12,12,31,21,41,13,11,12,21],
        '兰师傅柳州螺蛳粉':[12,32,42,53,12,34,46,34,46,67,37,33],
        '蜜雪冰城':[9,16,21,23,15,16,24,20,19,17,18,13],
        '兰州拉面':[12,13,11,12,14,13,14,15,21,13,14,16],
    }

    df = pd.DataFrame(data)
    index = pd.Series(["1月", "2月", "3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"], name='月份')
    df.index = index
    st.line_chart(df)
    data = {
        '恰好铺子':[350,351,385,194,175,163,371,584,382,354,351,261],
        '重庆小面':[251,152,482,172,142,351,231,471,123,181,122,221],
        '兰师傅柳州螺蛳粉':[182,382,462,535,162,342,456,354,456,667,377,373],
        '蜜雪冰城':[92,156,251,293,125,176,244,230,159,127,188,123],
        '兰州拉面':[112,173,131,122,174,133,124,175,231,123,174,316],
    }
    df = pd.DataFrame(data)
    index = pd.Series(["1月", "2月", "3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"], name='月份')
    df.index = index
    st.area_chart(df)
    image_path='https://news.cgtn.com/news/2023-12-16/Luosifen-a-smelly-noodle-dish-popular-across-China-1pA42exhyKc/img/54facee984934eb9a217f800e5e278d5/54facee984934eb9a217f800e5e278d5.jpeg'
    st.image(image_path,caption='https://news.cgtn.com/news/2023-12-16/Luosifen-a-smelly-noodle-dish-popular-across-China-1pA42exhyKc/img/54facee984934eb9a217f800e5e278d5/54facee984934eb9a217f800e5e278d5.jpeg')

with tab3:
    st.set_page_config(page_title='动物园', page_icon='🐒')
    images = [{'url':'https://facts.net/wp-content/uploads/2023/07/pufferfish-cute-.jpg','parm':'🐟鱼🐟'},
              {'url':'https://animalcorner.org/wp-content/uploads/2015/02/british-wild-cat-1.jpg','parm':'🐈猫🐈'},
              {'url':'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg','parm':'🐦鸟🐦'},
              {'url':'https://site-547756.mozfiles.com/files/547756/medium/Dog2.jpg','parm':'🐕狗🐕'}]
    if 'tpl'not in st.session_state:
        st.session_state['tpl'] = 0

    def nextImg():
        st.session_state['tpl'] = (st.session_state['tpl'] + 1) % len(images)
    def prevImg():
        st.session_state['tpl'] = (st.session_state['tpl'] - 1) % len(images)
    
    st.image(images[ st.session_state['tpl']]['url'],caption=images[st.session_state['tpl']]['parm'])

    c1,c2 = st.columns(2)

    with c1:
        st.button('上一张', on_click=prevImg,use_container_width=True)

    with c2:
        st.button('下一张', on_click=nextImg, use_container_width=True)
with tab4:
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
    
with tab5:
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

with tab6:
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






