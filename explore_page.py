import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


@st.cache
def load_data():
    df = pd.read_csv('train.csv')
    #since we cant be bothering customer with too much data to fill out..we r going tom reduce features furthur
    df = df[['battery_power', 'blue', 'dual_sim', 'fc', 'four_g',    #including only important aspects 
       'int_memory','pc',
        'ram','three_g',
       'touch_screen', 'wifi', 'price_range']]

    return df

df = load_data()

def show_explore_page():
    st.title('See the visualization of mobile price data')
    
    f1 = plt.figure()
    f2 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1 = sns.boxplot(x=df.price_range,y=df.int_memory).figure
    st.write("""### Boxplot of internal memory vs price""")
    st.pyplot(ax1,clear_fig=True)

    f4 = plt.figure()
    f5 = plt.figure()
    ax2 = f4.add_subplot(111)
    ax2 = sns.heatmap(df.corr()).figure
    st.write("""### coorelation graph of the dataset""")
    st.pyplot(ax2,clear_fig=True)


    f6 = plt.figure()
    f7 = plt.figure()
    ax3 = f4.add_subplot(111)
    ax3 = sns.barplot(x=df.price_range,y=df.ram).figure
    st.write("""### barplot of ram vs price""")
    st.pyplot(ax3,clear_fig=True)

    ram1 = df.ram[(df.ram >= 0) & (df.ram <= 1001)]
    ram2 = df.ram[(df.ram >= 1002) & (df.ram <= 2001)]
    ram3 = df.ram[(df.ram >= 2002) & (df.ram <= 3001)]
    ram4 = df.ram[(df.ram >= 3002) & (df.ram <= 4002)]

    ram_range = [len(ram1),len(ram2),len(ram3),len(ram4)]
    label = ['0<1gb','1<2gb','2<3gb','3<4gb']

    f8 = plt.figure()
    f9 = plt.figure()
    ax4 = f4.add_subplot(111)

    ax4 = sns.barplot(y=ram_range,x=label).figure
  
    st.write("""### pie chart of concentration of ram in market""")
    st.pyplot(ax4)
