from ctypes import alignment
import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article
import io
import nltk
import pandas as pd
import plotly.express as px
nltk.download('punkt')

st.set_page_config(page_title='NewsIn: A News📰 Summarizer and Analyzer', page_icon='./Meta/newspaper.ico')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

excel_file='analyzer1.xlsx'
excel_files='analyzer.xlsx'

#sheet_name='DATA'



def fetch_news_search_topic(topic):
    site = 'https://news.google.com/rss/search?q={}'.format(topic)
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    return news_list


def fetch_top_news():
    site = 'https://feeds.feedburner.com/ndtvnews-trending-news'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    return news_list

def world_news():
    site = 'https://feeds.feedburner.com/ndtvnews-world-news'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    df=pd.read_excel(excel_file,
                     usecols='U:W',
                     header=0)
    pie_chart=px.pie(df,
                     title='World',
                     values='world_count',
                     names='world_date')
    st.plotly_chart(pie_chart)
    df=pd.read_excel(excel_file,
                     usecols='BH:BM',
                     skiprows=33,
                     nrows=1,
                     header=0)
    pie_chart=px.pie(df,
                     title='World',
                     #values=['Russia','USA','UK','Asia'],
                     values= [152, 62, 47, 60],
                     names=['Russia','USA','UK','Asia'],
                     color=['Russia','USA','UK','Asia'],
                     color_discrete_map={'Russia':'#8d42f5','USA':'#42f563','UK':'#fc1414','Asia':'#f7e72f'})

    st.plotly_chart(pie_chart)
    return news_list

def nation_news():
    site = 'https://feeds.feedburner.com/ndtvnews-india-news'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    df=pd.read_excel(excel_file,
                     usecols='I:K',
                     header=0)
    pie_chart=px.pie(df,
                     title='Nation',
                     values='nation_count',
                     names='nation_date')
    st.plotly_chart(pie_chart)
    df=pd.read_excel(excel_file,
                     usecols='AO:AR',
                     skiprows=33,
                     nrows=1,
                     header=0)
    pie_chart=px.pie(df,
                     title='Nation',
                     values=[55,133,57,64],
                     names=['covid','government','crime','court'],
                     color=['covid','government','crime','court'],
                     color_discrete_map={'covid':'#8d42f5','government':'#42f563','crime':'#fc1414','court':'#f7e72f'})
    st.plotly_chart(pie_chart)
    return news_list

def business_news():
    site = 'https://feeds.feedburner.com/ndtvprofit-latest'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    df=pd.read_excel(excel_file,
                     usecols='A:C',
                     header=0)
    pie_chart=px.pie(df,
                     title='Business',
                     values='business_count',
                     names='business_date')
    st.plotly_chart(pie_chart)
    df=pd.read_excel(excel_file,
                     usecols='Z:AD',
                     skiprows=33,
                     nrows=1,
                     header=0)
    pie_chart=px.pie(df,
                     title='Business',
                     values=[62,61,39,63,61],
                     names=['Crypto','Market','Money','Economy','Industry'],
                     color=['Crypto','Market','Money','Economy','Industry'],
                     color_discrete_map={'Crypto':'#8d42f5','Market':'#42f563','Money':'#fc1414','Economy':'#f7e72f','Industry':'#2fe6f7'})
    st.plotly_chart(pie_chart)
    return news_list

def technology_news():
    site = 'https://feeds.feedburner.com/gadgets360-latest'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    df=pd.read_excel(excel_file,
                     usecols='Q:S',
                     header=0)
    pie_chart=px.pie(df,
                     title='Technology',
                     values='technology_count',
                     names='technology_date')
    st.plotly_chart(pie_chart)
    df=pd.read_excel(excel_file,
                     usecols='BB:BE',
                     skiprows=33,
                     nrows=1,
                     header=0)
    pie_chart=px.pie(df,
                     title='Technology',
                     values=[76,132,126,72],
                     names=['5G','Mobile','New_gadgets','Crypto'],
                     color=['5G','Mobile','New_gadgets','Crypto'],
                     color_discrete_map={'5G':'#8d42f5','Mobile':'#42f563','New_gadgets':'#fc1414','Crypto':'#f7e72f'})
    st.plotly_chart(pie_chart)
    return news_list

def entertainment_news():
    site = 'https://feeds.feedburner.com/ndtvmovies-latest'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    df=pd.read_excel(excel_file,
                     usecols='E:G',
                     header=0)
    pie_chart=px.pie(df,
                     title='Entertainment',
                     values='entertainment_count',
                     names='entertainment_date')
    st.plotly_chart(pie_chart)
    df=pd.read_excel(excel_file,
                     usecols='AG:AL',
                     skiprows=33,
                     nrows=1,
                     header=0)
    pie_chart=px.pie(df,
                     title='Entertainment',
                     values=[137,61,50,60],
                     names=['bollywood','hollywood','tv','web_series'],
                     color=['bollywood','hollywood','tv','web_series'],
                     color_discrete_map={'bollywood':'#8d42f5','hollywood':'#42f563','tv':'#fc1414','web_series':'#f7e72f'})
    st.plotly_chart(pie_chart)
    return news_list

def sports_news():
    site = 'https://feeds.feedburner.com/ndtvsports-latest'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    df=pd.read_excel(excel_file,
                     usecols='M:O',
                     header=0)
    pie_chart=px.pie(df,
                     title='Sports',
                     values='sports_count',
                     names='sports_date')
    st.plotly_chart(pie_chart)
    df=pd.read_excel(excel_file,
                     usecols='AV:AX',
                     skiprows=33,
                     nrows=1,
                     header=0)
    pie_chart=px.pie(df,
                     title='Sports',
                     values=[209,59,34],
                     names=['cricket','football','tennis'],
                     color=['cricket','football','tennis'],
                     color_discrete_map={'cricket':'#8d42f5','football':'#42f563','tennis':'#fc1414'})
    st.plotly_chart(pie_chart)
    return news_list

def fetch_category_news(topic):
    site = 'https://news.google.com/news/rss/headlines/section/topic/{}'.format(topic)
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    return news_list


def fetch_news_poster(poster_link):
    try:
        u = urlopen(poster_link)
        raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        st.image(image, use_column_width=True)
    except:
        image = Image.open('./Meta/no_image.jpg')
        st.image(image, use_column_width=True)

def display_news(list_of_news, news_quantity):
    c = 0
    for news in list_of_news:
        c += 1
        st.write('**({}) {}**'.format(c, news.title.text))
        news_data = Article(news.link.text)
        try:
            news_data.download()
            news_data.parse()
            news_data.nlp()
        except Exception as e:
            st.error(e)
        if news_data.top_image is not None:
            fetch_news_poster(news_data.top_image)
        with st.expander(news.title.text):
                st.markdown(
                    '''<h6 style='text-align: justify;'>{}"</h6>'''.format(news_data.summary),
                    unsafe_allow_html=True)
                st.markdown("[Read more]({})".format(news.link.text))
        st.success("Published Date: " + news.pubDate.text)
        if c >= news_quantity:
                break




def run():
    st.title("NewsIn: A News📰 Summarizer and Analyzer")
    image = Image.open('./Meta/newspaper.png')

    col1, col2, col3 = st.columns([3, 5, 3])

    with col1:
        st.write("")

    with col2:
        st.image(image, use_column_width=False)

    with col3:
        st.write("")
    category = ['--Select--', 'Trending🔥 News', 'Favourite💙 Topics', 'Search🔍 Topic']
    cat_op = st.selectbox('Select your Category', category)
    if cat_op == category[0]:
        st.warning('Please select Type!!')
        
    elif cat_op == category[1]:
        st.subheader("✅ Here is the Trending🔥 news for you")
        no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
        news_list = fetch_top_news()
        display_news(news_list, no_of_news)


    elif cat_op == category[2]:
        av_topics = ['Choose Topic', 'WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS']
        st.subheader("Choose your favourite Topic")
        chosen_topic = st.selectbox("Choose your favourite Topic", av_topics)
        if chosen_topic == av_topics[0]:
            st.warning("Please Choose the Topic")

        elif chosen_topic == av_topics[1]:            
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = world_news()
            display_news(news_list, no_of_news)

        elif chosen_topic == av_topics[2]:            
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = nation_news()
            display_news(news_list, no_of_news)

        elif chosen_topic == av_topics[3]:            
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = business_news()
            display_news(news_list, no_of_news)

        elif chosen_topic == av_topics[4]:            
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = technology_news()
            display_news(news_list, no_of_news)
        
        
        elif chosen_topic == av_topics[5]:
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = entertainment_news()
            display_news(news_list, no_of_news)

        elif chosen_topic == av_topics[6]:
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = sports_news()
            display_news(news_list, no_of_news)

        
        else:
            no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)
            news_list = fetch_category_news(chosen_topic)
            if news_list:
                st.subheader("✅ Here are the some {} News for you".format(chosen_topic))
                display_news(news_list, no_of_news)
            else:
                st.error("No News found for {}".format(chosen_topic))

    elif cat_op == category[3]:
        user_topic = st.text_input("Enter your Topic🔍")
        no_of_news = st.slider('Number of News:', min_value=5, max_value=15, step=1)

        if st.button("Search") and user_topic != '':
            user_topic_pr = user_topic.replace(' ', '')
            news_list = fetch_news_search_topic(topic=user_topic_pr)
            if news_list:
                st.subheader("✅ Here are the some {} News for you".format(user_topic.capitalize()))
                display_news(news_list, no_of_news)
            else:
                st.error("No News found for {}".format(user_topic))
        else:
            st.warning("Please write Topic Name to Search🔍")

    df=pd.read_excel(excel_files,
                usecols = 'C,B,E,H,K,N,Q'
                )
    fig=px.line(df,
            x='Date',
            y=['business_count','entertainment_count','nation_count','sports_count','technology_count','world_count'],
            title='Line Graph')
    st.plotly_chart(fig)

run()
