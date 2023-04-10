import streamlit as st
st.text("hola mundo!")
st.write("hola mundo")
st.caption("esto es un caption")
st.markdown("😜:alien:")

listaopciones=["a","b","c"]
ele=st.radio("elige:",listaopciones,index=1)
if ele==listaopciones[0]:
  st.text("elegiste aaa")
elif ele==listaopciones[1]:
  st.markdown("elegiste :red[bbbb]")
  
