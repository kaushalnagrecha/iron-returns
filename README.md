
# **Iron-Returns**  
*A Data-Driven Hedge Fund Decision Dashboard*

Welcome to **Iron-Returns** — a real-time, dynamic decision-making dashboard for hedge fund managers, investors, and financial analysts. Built with **Streamlit** and **Yahoo Finance API**, Iron-Returns automatically selects the top 5 U.S. companies by market capitalization, analyzes key metrics like P/E, ROE, Debt/Equity, and more, and helps you make informed decisions on whether to **Buy**, **Hold**, or **Sell** stocks.

[**View my Dashboard**](https://kn-top-5-companies-decision-board.streamlit.app/)

### 📈 Key Features
- **Dynamic Stock Selection**:  
  Automatically selects the top 5 companies by market capitalization based on the latest available data.

- **Metric-Specific Buy/Hold/Sell Signals**:  
  For each company, the dashboard provides **Buy**, **Hold**, or **Sell** signals based on metrics like **P/E Ratio**, **ROE**, **Debt/Equity**, **EPS Growth**, and **Revenue Growth**. The bars are color-coded (green, yellow, red) to make decision-making quick and easy.

- **PE Ratio Trend (YTD)**:  
  A year-to-date trend chart of the P/E ratio of each company to help track valuation movements over time.

- **Compact Layout**:  
  All key metrics and graphs are displayed in a compact layout that fits within a single screen for ease of use. No scrolling necessary, with **click-to-zoom** functionality for deeper analysis.

- **Collapsible Sidebar**:  
  The sidebar provides a quick overview of the Buy/Hold/Sell status for each company, allowing users to focus on the actionable insights.

- **Footer Attribution**:  
  Clear attribution to data sources and the maintainer (you!) for transparency and trust.

---

### 🔨 Built With
- **Streamlit**: A fast, powerful framework for building data dashboards in Python.
- **Yahoo Finance API**: For fetching up-to-date financial data of companies.
- **Plotly**: For building interactive visualizations and graphs.
- **Pandas**: For handling and manipulating financial data efficiently.

---

### 🚀 Getting Started

#### Prerequisites
- Python 3.x
- An IDE or text editor of your choice (VSCode, PyCharm, etc.)
- Internet connection (for data fetching via Yahoo Finance)

#### Steps to Get Started

1. **Clone the repository**:  
   Clone the repository to your local machine to begin working with the dashboard.
   ```bash
   git clone https://github.com/your-org/iron-returns.git
   cd iron-returns
   ```

2. **Install dependencies**:  
   Install all necessary Python dependencies. We recommend using `pip` or `conda`.
   ```bash
   pip install streamlit yfinance pandas plotly
   ```

3. **Run the dashboard**:  
   Once the dependencies are installed, you can launch the dashboard locally.
   ```bash
   streamlit run hedge_dashboard.py
   ```

4. **Explore the Dashboard**:  
   You’ll now see the dashboard in your browser, where you can interact with the data and see real-time decision insights based on the financial data of the top 5 U.S. companies by market cap.

---

### 🛠 Customization & Contributing

If you’d like to add new features, adjust the metrics or logic, or contribute to improving the dashboard, feel free to fork this repo and make a pull request. Some potential improvements could include:
- Adding more financial metrics (e.g., RSI, Moving Averages, etc.)
- Supporting multiple regions or countries beyond the U.S.
- Providing deeper analysis (e.g., risk-adjusted returns, sector comparison)
- Implementing a recommendation system using ML/AI to predict stock movements

If you’re interested in collaborating, don’t hesitate to reach out!

---

### 🏆 Why This Project?

**Iron-Returns** is a great example of:
- Building **data-driven decision tools** for hedge funds or investment firms.
- Creating **interactive dashboards** that make complex financial data digestible.
- Using **Python** and **Streamlit** to rapidly prototype tools that assist in real-time market analysis.

This project demonstrates the ability to combine **financial acumen** with **software engineering**, and I am excited to share it as part of my portfolio.

---

### ✍️ Maintained by:

[**Kaushal Nagrecha**](https://www.linkedin.com/in/kaushal-nagrecha)  

Feel free to connect with me via LinkedIn, and let’s talk about building impactful financial tools!

---

**Iron-Returns** is your companion for **data-driven investment decision-making**. Whether you’re managing a portfolio or just interested in financial data visualization, this tool empowers you to make smarter, faster decisions.
