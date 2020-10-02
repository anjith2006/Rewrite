import streamlit as st

from translate_utils import forward_backward, LANGUAGES, LANGCODES, HTML_WRAPPER

language= st.sidebar.selectbox(
	'Select the language to forward-backward',['german','french']+list(LANGCODES.keys()))



times= st.sidebar.selectbox(
    'Number of times',[1,2,3,4,5])

st.title('reWrite:')

text = st.text_area('The sentence to rewrite.')

agree = st.button('Rewrite!')

if agree:
	trans=forward_backward(text,lang=LANGCODES[language],times=int(times)) 
	st.write(HTML_WRAPPER.format(trans),unsafe_allow_html=True)


	