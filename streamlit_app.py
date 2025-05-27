import streamlit as st


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_3080.png", width=300")
st.image("")

st.tittle("dayan(dadiyanto)")
st.header("contoh orang orang ganteng")
angka = st.number_input("ganteng ga?:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} dadi ganteng")
else: 
    st.write(f"{angka} yanto ganteng")
