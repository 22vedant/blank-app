import streamlit as st
import numpy as np
import pandas as pd

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

y = st.slider('Select a number from 0 to 100');
st.write("You selected ", y)
# You can access the value at any point with:
st.session_state.name

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# add_name = st.sidebar.text_input("Hello, name = ", key = "slider_name")
# st.sidebar.write(add_name)
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

with st.form("my_form"):
    # st.write("Inside the form")
    st.title("GST CALCULATOR")
    # inside_text = st.text_input("")
    a = st.slider('Select amount', 0, 100000);
    # b = st.slider('Select interest rate');
    option = st.selectbox(
        "Tax Slab",
        (0.25, 3, 5, 12, 18, 28)
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        gst = (a * option) / 100
        st.write("GST Amount is", gst )
        st.write("Final Price", a + gst)

