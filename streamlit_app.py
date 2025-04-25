import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Hedge Fund Dashboard", layout="wide", initial_sidebar_state="expanded")

# ----------------------------
# Sidebar Strategy Summary
# ----------------------------
st.sidebar.title("📌 Strategy Summary")

# ----------------------------
# Pool of large-cap US tickers
# ----------------------------
ticker_pool = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "BRK-B", "UNH", "JPM",
    "JNJ", "V", "MA", "AVGO", "PG", "XOM", "HD", "PFE", "LLY", "PEP"
]

# ----------------------------
# Fetch Data
# ----------------------------
@st.cache_data(ttl=86400)
def fetch_company_data(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="ytd")["Close"]
            data.append({
                "Ticker": ticker,
                "Name": info.get("shortName", ticker),
                "Market Cap": info.get("marketCap", 0),
                "PE Ratio": info.get("trailingPE", 0),
                "EPS": info.get("trailingEps", 0),
                "Dividend Yield": info.get("dividendYield", 0),
                "EPS Growth": info.get("earningsQuarterlyGrowth", 0),
                "ROE": info.get("returnOnEquity", 0),
                "Debt/Equity": info.get("debtToEquity", 0),
                "Revenue Growth": info.get("revenueGrowth", 0),
                "History": hist
            })
        except Exception as e:
            st.warning(f"Error loading {ticker}: {e}")
    return pd.DataFrame(data)

df_all = fetch_company_data(ticker_pool)

# ----------------------------
# Select Top 5 by Market Cap
# ----------------------------
df = df_all.sort_values(by="Market Cap", ascending=False).head(5).reset_index(drop=True)

# ----------------------------
# Strategy Categorization
# ----------------------------
def categorize(row):
    if row["PE Ratio"] < 20 and row["EPS Growth"] > 0.1 and row["ROE"] > 0.15 and row["Debt/Equity"] < 100:
        return "Buy"
    elif row["PE Ratio"] < 25 and row["Revenue Growth"] >= 0:
        return "Hold"
    else:
        return "Sell"

df["Decision"] = df.apply(categorize, axis=1)

# ----------------------------
# Sidebar Action Summary
# ----------------------------
st.sidebar.success("🟢 **Buy**: " + ", ".join(df[df["Decision"] == "Buy"]["Name"].tolist() or ["None"]))
st.sidebar.warning("🟡 **Hold**: " + ", ".join(df[df["Decision"] == "Hold"]["Name"].tolist() or ["None"]))
st.sidebar.error("🔴 **Sell**: " + ", ".join(df[df["Decision"] == "Sell"]["Name"].tolist() or ["None"]))

# ----------------------------
# Dashboard Title
# ----------------------------
st.markdown("### 📊 Hedge Fund Dashboard: Top 5 US Companies by Market Cap")

# ----------------------------
# Colors
# ----------------------------
color_map = {"Buy": "green", "Hold": "yellow", "Sell": "red"}

# ----------------------------
# Layout: Main Dashboard
# ----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(px.bar(df, x="Name", y="PE Ratio", color="Decision", color_discrete_map=color_map,
                           title="PE Ratio", height=200).update_layout(font=dict(size=10), margin=dict(t=30)), use_container_width=True)
    
    st.plotly_chart(px.bar(df, x="Name", y="Dividend Yield", color="Decision", color_discrete_map=color_map,
                           title="Dividend Yield", height=200).update_layout(font=dict(size=10), margin=dict(t=30)), use_container_width=True)

    st.plotly_chart(px.bar(df, x="Name", y="ROE", color="Decision", color_discrete_map=color_map,
                           title="Return on Equity", height=200).update_layout(font=dict(size=10), margin=dict(t=30)), use_container_width=True)

with col2:
    st.plotly_chart(px.bar(df, x="Name", y="EPS Growth", color="Decision", color_discrete_map=color_map,
                           title="EPS Growth", height=200).update_layout(font=dict(size=10), margin=dict(t=30)), use_container_width=True)

    st.plotly_chart(px.bar(df, x="Name", y=df["Market Cap"] / 1e9, color="Name",
                           title="Market Cap (in $B)", height=200).update_layout(font=dict(size=10), margin=dict(t=30), showlegend=False), use_container_width=True)

    st.plotly_chart(px.bar(df, x="Name", y="Revenue Growth", color="Decision", color_discrete_map=color_map,
                           title="Revenue Growth", height=200).update_layout(font=dict(size=10), margin=dict(t=30)), use_container_width=True)

with col3:
    fig_pe = px.line()
    for _, row in df.iterrows():
        if row["EPS"] > 0:
            pe_series = row["History"] / row["EPS"]
            fig_pe.add_scatter(x=pe_series.index, y=pe_series.values, mode='lines', name=row["Name"])
    fig_pe.update_layout(
        title="PE Ratio Over Time (YTD)",
        height=420,
        font=dict(size=10),
        margin=dict(t=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.80,
            xanchor="center",
            x=0.7,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=8)
        )
    )

    st.plotly_chart(fig_pe, use_container_width=True)

    st.plotly_chart(px.bar(df, x="Name", y="Debt/Equity", color="Decision", color_discrete_map=color_map,
                           title="Debt-to-Equity Ratio", height=200).update_layout(font=dict(size=10), margin=dict(t=30)), use_container_width=True)

# ----------------------------
# Footer
# ----------------------------
footer_left, footer_right = st.columns([1, 1])
with footer_left:
    st.markdown("**Data Source**: Yahoo Finance", unsafe_allow_html=True)
with footer_right:
    st.markdown(
        '<div style="text-align:right">Maintained by: <a href="https://www.linkedin.com/in/kaushalnagrecha" target="_blank">Kaushal Nagrecha</a></div>',
        unsafe_allow_html=True
    )
