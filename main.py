import streamlit as st

def count_lines(text):
    count = len(text.split('\n'))
    return count

st.title('Підрахунок рядків')
text = st.text_area('Введіть ваш текст:')
count = count_lines(text)
st.write(f'Кількість рядків: {count}')

