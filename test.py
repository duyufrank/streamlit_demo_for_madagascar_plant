from PIL import Image
from matplotlib import pyplot as plt
import streamlit as st


def read_markdown_file(markdown_file):
    with open(markdown_file, encoding='utf-8') as fp:
        w = fp.read()
    return w

st.markdown('**See more: **')
st.image('images/a1.jpg', 'Lauraceae')
st.markdown(read_markdown_file("a.md"), unsafe_allow_html=True)
st.image('images/a2.jpg', 'Proteaceae')
st.markdown(read_markdown_file("a2.md"), unsafe_allow_html=True)
st.image('images/a3.png', 'Burseraceae')
st.markdown(read_markdown_file("a3.md"), unsafe_allow_html=True)
st.image('images/a4.jpg', 'Calophyllaceae')
st.markdown(read_markdown_file("a4.md"), unsafe_allow_html=True)
st.image('images/a5.jpg', 'Clusiaceae')
st.markdown(read_markdown_file("a5.md"), unsafe_allow_html=True)
st.image('images/a6.jpg', 'Euphorbiaceae')
st.markdown(read_markdown_file("a6.md"), unsafe_allow_html=True)

def latex_tag(tag):
    out = r"$\bf{tag}$"
    return out.replace('tag', str(tag))

st.markdown('**Donors’ tree** \n Pie chart: ')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('We have six types of trees', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b1.md"), unsafe_allow_html=True)

st.markdown('**Map**')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('We keep track of every tree we have planted', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b2.md"), unsafe_allow_html=True)

st.markdown('**Trees planted across years**')
st.markdown(read_markdown_file("b3.md"), unsafe_allow_html=True)

st.markdown('**Status of trees planted in other years**')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('Satisfying tree survival rate', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b4.md"), unsafe_allow_html=True)

st.markdown('**Natural observations in this region**')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('Planting trees are effective to ecosystem', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b5.md"), unsafe_allow_html=True)

st.markdown('**Income**')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('Madagascar is in need for help', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b6.md"), unsafe_allow_html=True)

st.markdown('**Coffee**')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('Residents get the largest profit ratio from growing $\\bf{coffee}$', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b7.md"), unsafe_allow_html=True)

st.markdown('**Environment**')
fig, ax = plt.subplots()
img = Image.open('images/a1.jpg')
ax.imshow(img)
ax.axis('off')
ax.set_title('Protection of biomass', loc='center')
st.pyplot(fig)
st.markdown(read_markdown_file("b8.md"), unsafe_allow_html=True)