import streamlit as st


st.title("jangan lupa sabskreb dadiyanto😈😛")
st.write(
    "2 contoh tipikal laki laki ganteng tamax(tampanmaximal)😎🥰😍🤪😜😝. "
)
st.image("IMG_3080.png", width=300)
st.image("IMG_5880.png", width=500)

st.tittle("dayan(dadiyanto)")
st.header("contoh orang orang ganteng")
angka = st.number_input("ganteng ga?:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} dadi ganteng")
else: 
    st.write(f"{angka} yanto ganteng")
