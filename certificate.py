import cv2
import os
import base64
import streamlit as st
import numpy
import sys
from PIL import Image, ImageDraw

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

font = cv2.FONT_HERSHEY_TRIPLEX

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"> Download {file_label}</a>'
    return href

def annotate(name):
    path = "./images/KAI-MEETUP-ATTEND-SHARE.jpg"
    
    certi = cv2.imread(path)
    if len(name) < 10:
        x = 1310 - (len(name) * 10)
        fontScale = 1.5
    else:
        x = 1310 - (len(name) * 11)
        fontScale = 1.3
    original = cv2.putText(certi, name, (x, 490),font, fontScale, (0, 0, 0), thickness=2)
    
    cv2.imwrite("Certificate.jpg",original)

    if st.button("View certificate"):
        st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',output_format='PNG')
        st.markdown(get_binary_file_downloader_html('Certificate.jpg', 'Certificate'), unsafe_allow_html=True)

st.title("Get Your Certificate")
name=st.text_input('Enter your name').title()
if len(name)>0 and len(name)<=17:
    annotate(name)
elif len(name)>17:
    st.write("Please try with short name")
else:
    st.write("Please enter Your name in the Above Field To download the Certificate")    


