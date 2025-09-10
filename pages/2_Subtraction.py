import streamlit as st
from visuals import create_number_line_with_jumps, create_combine_takeaway_dots, fig_to_png_bytes

st.set_page_config(page_title="Subtraction • Arithmetic Playground", page_icon="➖")

st.title("➖ Subtraction")
st.caption("Take away to see what is left.")

with st.sidebar:
    st.header("Choose Numbers")
    input_mode = st.radio("Input method", ["Slider", "Type"], horizontal=True)
    if input_mode == "Slider":
        a = st.slider("Start with (A)", 0, 50, 12)
        b = st.slider("Take away (B)", 0, 50, 4)
    else:
        a = st.number_input("Start with (A)", min_value=0, max_value=1000, value=12, step=1)
        b = st.number_input("Take away (B)", min_value=0, max_value=1000, value=4, step=1)
    b = min(b, a)

st.subheader("See what is left")
fig1 = create_combine_takeaway_dots(a, b, mode="subtract", title=f"{a} − {b} = {a-b}")
st.image(fig_to_png_bytes(fig1), use_container_width=True)

st.divider()

st.subheader("Hop back on the number line")
st.write("Start at A, and hop backward B steps.")
fig2 = create_number_line_with_jumps(a, [-1] * b, title=f"Start {a} and hop −1, {b} times")
st.image(fig_to_png_bytes(fig2), use_container_width=True)
