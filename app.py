import re
import streamlit as st

POSITIVE={"good","great","useful","excellent","love","happy","success"}
NEGATIVE={"bad","poor","hate","sad","failure","slow","problem"}

def words(text): return re.findall(r"[a-z0-9]+", text.lower())
def similarity(a,b):
    x,y=set(words(a)),set(words(b))
    return round(100*len(x&y)/max(1,len(x|y)),2)
def sentiment(text):
    ws=words(text); score=sum(w in POSITIVE for w in ws)-sum(w in NEGATIVE for w in ws)
    return "positive" if score>0 else "negative" if score<0 else "neutral"

st.set_page_config(page_title="SentiraAI", page_icon="✦")
st.title("✦ SentiraAI")
st.caption("Explainable NLP starter for semantic comparison")
a=st.text_area("Text A", "AI helps people build useful systems.")
b=st.text_area("Text B", "Artificial intelligence helps teams create useful products.")
if st.button("Analyze"):
    st.metric("Token similarity", f"{similarity(a,b)}%")
    st.write({"Text A sentiment":sentiment(a),"Text B sentiment":sentiment(b)})
