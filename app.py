import streamlit as st
import ollama
import time
import psutil
import pandas as pd

# Load YOUR real results
@st.cache_data
def load_benchmarks():
    return pd.read_csv('benchmark_results.csv')

st.title("🛡️Local SLM Benchmark Dashboard")

# Show your table
df = load_benchmarks()
st.subheader("Your Hardware Benchmarks")
st.dataframe(df.style.highlight_min(axis=0, color='lightgreen'))

# Live inference 
model = st.selectbox("Choose model:", df['model'].tolist())
prompt = st.chat_input("Test live inference...")

if prompt:
    with st.spinner(f'🤖 {model} thinking...'):
        start = time.time()
        resp = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        latency = (time.time() - start)*1000
        
        st.write("**Response:**")
        st.write(resp['message']['content'])
        st.metric("Live Latency", f"{latency:.0f}ms")