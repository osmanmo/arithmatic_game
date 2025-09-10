import streamlit as st
from visuals import (
    create_number_line_with_jumps,
    fig_to_png_bytes,
)

st.set_page_config(
    page_title="Arithmetic Playground",
    page_icon="🎈",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .big-title { font-size: 2.2rem; font-weight: 800; color: #2D2D2D; }
    .subtitle { font-size: 1.1rem; color: #444; }
    .emoji { font-size: 1.6rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='big-title'>🎈 Arithmetic Playground</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>A friendly place to see math, not just do math. Choose an operation from the sidebar!</div>",
    unsafe_allow_html=True,
)

st.divider()

st.write("Try these pages:")
cols = st.columns(4)
if hasattr(st, "page_link"):
    with cols[0]:
        st.page_link("pages/1_Addition.py", label="➕ Addition", icon="➕")
    with cols[1]:
        st.page_link("pages/2_Subtraction.py", label="➖ Subtraction", icon="➖")
    with cols[2]:
        st.page_link("pages/3_Multiplication.py", label="✖️ Multiplication", icon="✖️")
    with cols[3]:
        st.page_link("pages/4_Division.py", label="➗ Division", icon="➗")
else:
    with cols[0]:
        st.markdown("**➕ Addition** — use the sidebar to open pages")
    with cols[1]:
        st.markdown("**➖ Subtraction** — use the sidebar to open pages")
    with cols[2]:
        st.markdown("**✖️ Multiplication** — use the sidebar to open pages")
    with cols[3]:
        st.markdown("**➗ Division** — use the sidebar to open pages")

st.divider()

st.markdown("### Quick Demo: Number Line Hops")
origin = st.slider("Start at", -20, 20, 0)
steps = st.slider("How many +1 hops?", 0, 10, 3)
fig = create_number_line_with_jumps(origin, [1] * steps)
st.image(fig_to_png_bytes(fig), use_container_width=True)
