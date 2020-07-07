import yfinance as yf
import streamlit as st
import pandas as pd

##creates text in the web app in HTML
st.write("""
# Simple Stock Price App


Shown are the stock closing price and volume of Tesla.

""")

##looks for the given ticker symbol on Yahoo Finance
tickerSymbol = 'TSLA'

##gets the required data from the given ticker symbol
tickerData = yf.Ticker(tickerSymbol)

##sets the parameters for date and period for the chart
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-7-6')

##shows the chart for the stocks closing value and the volume sold in the given period over the two dates
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)