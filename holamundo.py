import streamlit as st
st.text("hola mundo!")
st.write("hola mundo")
st.caption("esto es un caption")
st.markdown("😜:alien:")
ele=st.radio("elige:",["a","b","c"],index=1)
if ele=="a":
  st.text("elegiste aaa")
elif ele=="b":
  st.markdown("elegiste :red[bbbb]")
  
