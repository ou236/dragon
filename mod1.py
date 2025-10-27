import streamlit as st

page = st.sidebar.selectbox("选择页面", ["数字档案","美食地图","相册","音乐播放器","视频","个人简历生成器"])

if page == "数字档案":
    st.title("数字档案")
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
elif page == "美食地图":
    st.title("美食地图")
    import streamlit as st
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
    image_path=r'D:\\streamlit_env\111.jpeg'
    st.image(image_path,caption='111')
elif page == "相册":
    st.title("相册")
    import streamlit as st

    st.set_page_config(page_title='动物园', page_icon='🐒')





    images = [{'url':'https://facts.net/wp-content/uploads/2023/07/pufferfish-cute-.jpg','parm':'🐟鱼🐟'},
          {'url':'https://animalcorner.org/wp-content/uploads/2015/02/british-wild-cat-1.jpg','parm':'🐈猫🐈'},
          {'url':'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg','parm':'🐦鸟🐦'},
          {'url':'https://site-547756.mozfiles.com/files/547756/medium/Dog2.jpg','parm':'🐕狗🐕'}]

    if 'tp1'not in st.session_state:
        st.session_state['tp1'] = 0

    def nextImg():
        st.session_state['tp1'] = (st.session_state['tp1'] + 1) % len(images)
    def nextImg1():
        st.session_state['tp1'] = (st.session_state['tp1'] - 1) % len(images)
    



    st.image(images[ st.session_state['tp1']]['url'],caption=images[st.session_state['tp1']]['parm'])

    c1,c2 = st.columns(2)

    with c1:
        st.button('上一张', on_click=nextImg1,use_container_width=True)

    with c2:
        st.button('下一张', on_click=nextImg, use_container_width=True)

elif page == "音乐播放器":
    st.title("音乐播放器")
    import streamlit as st

    st.set_page_config(page_title='音乐',page_icon='🎶')
# 读取音频URL
    music = [{'url':'https://music.163.com/song/media/outer/url?id=5260311.mp3',
                   'photo':'https://p1.music.126.net/Oix4KKx3qsuL8UGiLKcDiA==/43980465127856.jpg?param=180y180',
                   'name':'葡萄成熟时',
                   'author':'陈奕迅'},
             {'url':'https://music.163.com/song/media/outer/url?id=2613686702.mp3',
              'photo':'https://p2.music.126.net/p6uM4LOzKh-b3r1eTmvU4g==/109951169838608004.jpg?param=180y180',
              'name':'孤单心事(DJ阿智Remix)',
              'author':'DJ阿智'},
             {'url':'https://music.163.com/song/media/outer/url?id=1834268297.mp3',
              'photo':'https://p2.music.126.net/gJpeTMYWBBXFXq7vpxmLxg==/109951165854197528.jpg?param=180y180',
              'name':'心墙',
              'author':'DJ.Mr.李'}]
         

    if 'tp' not in st.session_state:
        st.session_state['tp'] = 0


 


    a1,a2 = st.columns([1,2])
    with a1:
        st.image(music[st.session_state['tp']]['photo'])
        st.text('封面专辑')
    with a2:
        st.title(music[st.session_state['tp']]['name'])
        st.text(music[st.session_state['tp']]['author'])
    def nextImg():
        st.session_state['tp'] = (st.session_state['tp'] + 1) % len(music)
    def prevImg():
        st.session_state['tp'] = (st.session_state['tp'] - 1) % len(music)

    st.audio(music[st.session_state['tp']]['url'])
    b1,b2 = st.columns(2)
    with b1:
        st.button('上一首', on_click=prevImg,use_container_width=True)
    with b2:
        st.button('下一首', on_click=prevImg,use_container_width=True)

elif page == "视频":
    st.title("视频")
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
elif page == "个人简历生成器":
    st.title("个人简历生成器")
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
