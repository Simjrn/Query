import query as qy

with st.sidebar:
  st.header("Choose your lesson")
  lesson = st.radio("Section 1:", ["lesson 1", "lesson 2", "lesson 3"])

if lesson == "lesson 1":
  
