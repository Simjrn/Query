import query as qy
import streamlit as st

with st.sidebar:
  st.header("Choose your lesson")
  lesson = st.radio("Section 1:", ["lesson 1", "lesson 2", "lesson 3"])

if lesson == "lesson 1":
  st.markdown("""
  Hello = Allegra

  I want = Jau vi

  How are you? = Co vai?

  Thank you = Grazia

  Very well = Fitg bain""")
  answer = qy.make_sentence("hello, how are you?", ["allegra", "vai", "co"]
  if st.button("submit"):
    if answer == ["allegra", "co", "vai"]:
      st.balloons()
    else:
      st.error("uh oh! Try again")
