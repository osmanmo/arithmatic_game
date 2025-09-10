import streamlit as st
from visuals import create_grouping_model, create_number_line_with_jumps, fig_to_png_bytes

st.set_page_config(page_title="Division • Arithmetic Playground", page_icon="➗")

st.title("➗ Division")
st.caption("Division is making equal groups.")

with st.sidebar:
    st.header("Choose Numbers")
    total = st.slider("Total items", 0, 120, 63)
    group_size = st.slider("Group size (how many in each group)", 1, 12, 9)
    step = st.checkbox("Show groups step-by-step", value=True)

quotient = total // group_size
remainder = total % group_size
shown_groups = st.slider("How many groups to show?", 0, quotient, quotient if not step else min(1, quotient)) if step else quotient

st.subheader("Make equal groups")
fig1 = create_grouping_model(total, group_size, step_groups=shown_groups, title=f"{total} ÷ {group_size} = {quotient} R {remainder}")
st.image(fig_to_png_bytes(fig1), use_container_width=True)

st.divider()

st.subheader("Repeated subtraction on a number line")
st.write("Start at the total, hop back by the group size.")
jumps = [-group_size] * quotient
fig2 = create_number_line_with_jumps(total, jumps, title=f"{quotient} jumps of −{group_size}; remainder {remainder}")
st.image(fig_to_png_bytes(fig2), use_container_width=True)
