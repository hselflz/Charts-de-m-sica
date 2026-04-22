import streamlit as st
import requests
import pandas as pd

st.title("🎧 Music Analytics Dashboard")

API_URL = "http://127.0.0.1:8000"

# -------- Top Songs --------

st.header("Top Songs")

response = requests.get(f"{API_URL}/top-songs")
data = response.json()

df = pd.DataFrame(data)

st.bar_chart(df.set_index("title")["total_plays"])


# -------- Top Artists --------

st.header("Top Artists")

response = requests.get(f"{API_URL}/top-artists")
data = response.json()

df = pd.DataFrame(data)

st.bar_chart(df.set_index("artist")["total_plays"])


# -------- Active Users --------

st.header("Most Active Users")

response = requests.get(f"{API_URL}/active-users")
data = response.json()

df = pd.DataFrame(data)

st.dataframe(df)


# Plays by day 

st.header("Plays by day")

reponse = requests.get(f"{API_URL}/plays-by-day")
data = reponse.json()

df = pd.DataFrame(data)

df["day"] = pd.to_datetime(df["day"])
df = df.sort_values("day")
st.line_chart(df.set_index("day")["total_plays"])
