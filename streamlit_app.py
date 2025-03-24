import streamlit as st
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
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

with st.form("gst_form"):
    st.title("GST CALCULATOR")
    amount = st.slider('Select amount (₹)', 0, 100000, step=500);
    tax_slab = st.selectbox(
        "Tax Slab",
        (0.25, 3, 5, 12, 18, 28)
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        gst = (amount * tax_slab) / 100
        final = gst + amount
        with st.spinner("Calculating...", show_time=True):
            time.sleep(3)
        st.success("Calculation Complete!")
        
        
        st.write(f"**GST Amount:** ₹{gst:,.2f}")
        st.write(f"**Final Price:** ₹{final :,.2f}")
        

if st.button("Click Me"):
    st.toast("You have clicked the button!", icon="😈")
    time.sleep(1)
    st.toast("After one second", icon="😈")

plt.style.use("dark_background")

st.title("Plot example")

x_values = [1,2,3,4,5]
y_values = [2,3,5,7,11]

fig,ax = plt.subplots()

ax.scatter(x_values,y_values, color="blue")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

ax.set_title("Simple Plot example")

st.pyplot(fig)