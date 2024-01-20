import streamlit as st
import pandas as pd
import numpy as np

st.title(":cat: Book Gang Events Calendar :dog: :duck: :penguin: :frog: :goat: :rat: :chicken: :elephant: :baby_chick: :mouse: :bird:")
csv_table = open("Events.csv")
dataframe = pd.read_csv(csv_table)
#remove last column
dataframe = dataframe.iloc[: , :-1]
print(dataframe)
st.dataframe(data=dataframe, use_container_width = True, hide_index = True)
st.image("bottom_img.png")