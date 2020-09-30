import streamlit as st

from translate_utils import forward_backward

language= st.sidebar.selectbox(
    'Select the language to Forward back ward',['French:fr','German:de','Hindi:hi'])


times= st.sidebar.selectbox(
    'Number of times',[1,2,3,4,5])

# print("language: {}, times: {}".format(language,times))

st.title('Rewrite:')
#text = st.text_input('The sentence to rewrite.')

text = st.text_area('The sentence to rewrite.')

agree = st.button('Rewrite!')

if agree:
	trans=forward_backward(text,lang=language.split(":")[-1],times=int(times))
	st.write(trans)