import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Stock Strategy Dashboard", layout="wide")

st.title("📈 Stock Strategy Backtesting Dashboard")

# Load data
wf = pd.read_csv("walk_forward_results.csv", parse_dates=["Train_Start", "Train_End", "Test_End"])
equity = pd.read_csv("equity_curve.csv", index_col=0, parse_dates=True)

# Sidebar
st.sidebar.header("Controls")
show_equity = st.sidebar.checkbox("Show Equity Curve", True)
show_wf = st.sidebar.checkbox("Show Walk-Forward Results", True)

# Equity Curve
if show_equity:
    st.subheader("📊 Equity Curve (Full Period)")
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(equity)
    ax.set_xlabel("Date")
    ax.set_ylabel("Equity")
    ax.grid()
    st.pyplot(fig)

# Walk-forward Results
if show_wf:
    st.subheader("🔁 Walk-Forward Test Returns")
    st.dataframe(wf)

    fig2, ax2 = plt.subplots(figsize=(10,4))
    ax2.plot(wf["Test_End"], wf["Test_Return"], marker="o")
    ax2.axhline(0, color="red", linestyle="--")
    ax2.set_xlabel("Test Period End")
    ax2.set_ylabel("Return")
    ax2.grid()
    st.pyplot(fig2)

# Summary
st.subheader("📌 Summary")
st.metric("Average Walk-Forward Return", round(wf["Test_Return"].mean(), 3))
st.metric("Best Period Return", round(wf["Test_Return"].max(), 3))
st.metric("Worst Period Return", round(wf["Test_Return"].min(), 3))
