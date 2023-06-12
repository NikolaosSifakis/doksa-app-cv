import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon="🧘‍♀️", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_python = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_t9h3vpwn.json")
img1 = Image.open("MY_PLATE.png")
img2 = Image.open("Halloween_yoga_dance.png")
img3 = Image.open("CASTLE_WARS.png")
img_doxa = Image.open("doxa.png")
img_doxa = img_doxa.resize((150, 150), Image. LANCZOS)


# ---- HEADER SECTION ----

with st.container():


    left_column,right_column = st.columns([1,2])
    with left_column:
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")

        st.subheader("Hi, I am Doxa 👋 ")

        st.title("I am a  P.E. Teacher  ⛹️‍♀️")
        st.write(
        "I am passionate about finding ways to keep kids active and motivated."
            )
        st.write(
        "I love 3D modeling and animation and i use it for creating  p.e. content for kids and p.e. teachers."
            )
        st.write("[My Instagram Profile >](https://www.instagram.com/doxadakanalipe/?hl=el)")
    with right_column:
        st.image(img_doxa)
        st.title("Welcome to my website")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating videos for  kids, Families, P.E. Teachers:
            - Fun informative videos about balanced diet for kids.
            - Interactive P.E. games .
            - P.E. games for the schoolyard or gym.
            - Yoga for kids.
            - Dance for kids.
            "
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@doxadakanalipe772)")
    with right_column:
        st_lottie(lottie_python, height=450, key="python")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("MY PLATE")
        st.write(
            """
            Learn learn all about 'My plate" and the food groups in this video.
            You will learn how to built healthy meals and snacks to help you grow,
            play, learn and stay healthy.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=xQRylT2ndyw)")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
with st.container():
    with image_column:
        st.image(img2)
    with text_column:
        st.subheader("Halloween Yoga Freeze Dance")
        st.write(
            """
            This is a Yoga and dance game! When the music is on  dance and move with
            all of your favorite spooky characters , when the music stops hold a yoga pose ! 
            This GoNoodle inspired activity is perfect for kids of all ages.  
            DANCE with us in this super fun workout for the class and the whole family.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=zzhkdbkbpLM)")
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=xQRylT2ndyw)")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")


with st.container():

    with image_column:
        st.image(img3)
    with text_column:
        st.subheader("CASTLE WARS")
        st.write(
            """
            Castle wars is a very popular pe game for the gym or the school yard.
            With this game the kids will develop skills like throwing, catching, defending space 
            and team building and they will have a lots of fun
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=WAs18iZtYFU)")

# https://blog.streamlit.io/introducing-theming/



st.code('''
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon="🧘‍♀️", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_python = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_t9h3vpwn.json")
img1 = Image.open("MY_PLATE.png")
img2 = Image.open("Halloween_yoga_dance.png")
img3 = Image.open("CASTLE_WARS.png")
img_doxa= Image.open("doxa.png")
img_doxa = img_doxa.resize((150, 150), Image.ANTIALIAS)


# ---- HEADER SECTION ----

with st.container():

   # st.markdown("# Welcome to my website")
    left_column, right_column = st.columns([1,2])
    with left_column:
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")

        st.subheader("Hi, I am Doxa 👋 ")

        st.title("I am a  P.E. Teacher  ⛹️‍♀️")
        st.write(
        "I am passionate about finding ways to keep kids active and motivated."
            )
        st.write(
        "I love 3D modeling and animation and i use it for creating  p.e. content for kids and p.e. teachers."
            )
        st.write("[My Instagram Profile >](https://www.instagram.com/doxadakanalipe/?hl=el)")
    with right_column:
        st.image(img_doxa)
        st.title("Welcome to my website")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating videos for  kids, Families, P.E. Teachers:
            - Fun informative videos about balanced diet for kids.
            - Interactive P.E. games .
            - P.E. games for the schoolyard or gym.
            - Yoga for kids.
            - Dance for kids.
            "
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@doxadakanalipe772)")
    with right_column:
        st_lottie(lottie_python, height=400, key="python")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("MY PLATE")
        st.write(
            """
            Learn learn all about 'My plate" and the food groups in this video.
            You will learn how to built healthy meals and snacks to help you grow,
            play, learn and stay healthy.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=xQRylT2ndyw)")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
with st.container():
    with image_column:
        st.image(img2)
    with text_column:
        st.subheader("Halloween Yoga Freeze Dance")
        st.write(
            """
            This is a Yoga and dance game! When the music is on  dance and move with
            all of your favorite spooky characters , when the music stops hold a yoga pose ! 
            This GoNoodle inspired activity is perfect for kids of all ages.  
            DANCE with us in this super fun workout for the class and the whole family.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=zzhkdbkbpLM)")
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=xQRylT2ndyw)")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")
        st.write("######")


with st.container():
    
    with image_column:
        st.image(img3)
    with text_column:
        st.subheader("CASTLE WARS")
        st.write(
            """
            Castle wars is a very popular pe game for the gym or the school yard.
            With this game the kids will develop skills like throwing, catching, defending space 
            and team building and they will have a lots of fun
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=WAs18iZtYFU)")

# https://blog.streamlit.io/introducing-theming/
 ''')