import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
penguin_df = pd.read_csv(r'D:/streamlit_env/（企业识别数据）penguins-chinese.csv', encoding='gbk')
print(penguin_df.head())
