import streamlit as st
from visuals import create_array_model, create_number_line_with_jumps, fig_to_png_bytes

st.set_page_config(page_title="Multiplication • Arithmetic Playground", page_icon="✖️")

st.title("✖️ Multiplication")
st.caption("Rows and columns make an array.")

with st.sidebar:
    st.header("Choose Numbers")
    rows = st.slider("Rows", 1, 12, 3)
    cols = st.slider("Columns", 1, 12, 4)
    step_fill = st.checkbox("Fill step by step", value=False)
    how_many = st.slider("How many cells filled?", 0, rows*cols, rows*cols) if step_fill else rows*cols

st.subheader("Array model (rows × columns)")
fig1 = create_array_model(rows, cols, fill_until=how_many, title=f"{rows} × {cols} = {rows*cols}")
st.image(fig_to_png_bytes(fig1), use_container_width=True)

st.divider()

st.subheader("Skip counting on the number line")
st.write("Jump by 'columns' size, 'rows' times (or vice-versa).")
fig2 = create_number_line_with_jumps(0, [cols] * rows, title=f"{rows} jumps of +{cols}")
st.image(fig_to_png_bytes(fig2), use_container_width=True)
