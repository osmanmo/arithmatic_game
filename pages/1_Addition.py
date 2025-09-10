import streamlit as st
from visuals import create_number_line_with_jumps, create_combine_takeaway_dots, fig_to_png_bytes

st.set_page_config(page_title="Addition • Arithmetic Playground", page_icon="➕")

st.title("➕ Addition")
st.caption("Combine two groups to make a bigger group.")

with st.sidebar:
    st.header("Choose Numbers")
    input_mode = st.radio("Input method", ["Slider", "Type"], horizontal=True)
    if input_mode == "Slider":
        a = st.slider("First number (A)", 0, 50, 7)
        b = st.slider("Second number (B)", 0, 50, 5)
    else:
        a = st.number_input("First number (A)", min_value=0, max_value=1000, value=7, step=1)
        b = st.number_input("Second number (B)", min_value=0, max_value=1000, value=5, step=1)

st.subheader("See the groups")
st.write("We put A and B together to see the total.")
fig1 = create_combine_takeaway_dots(a, b, mode="add", title=f"{a} + {b} = {a+b}")
st.image(fig_to_png_bytes(fig1), use_container_width=True)

st.divider()

st.subheader("Hop on the number line")
st.write("Start at A, and hop forward B steps.")
fig2 = create_number_line_with_jumps(a, [1] * b, title=f"Start {a} and hop +1, {b} times")
st.image(fig_to_png_bytes(fig2), use_container_width=True)
