import sys
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import keyboard
from matplotlib.animation import FuncAnimation


ticker = yf.Ticker("MRF.NS")

def animate(i):
    data = ticker.history(period="1d", interval="1m")
    x = data.tail(30).index
    y1 = data.tail(30)['Close']
    y2 = data.tail(30)['High']
    y3 = data.tail(30)['Low']
    y4 = data.tail(30)['Open']
    plt.cla()
    plt.plot(x, y1, label='Close')
    plt.plot(x, y2, label='High')
    plt.plot(x, y3, label='Low')
    plt.plot(x, y4, label='Open')
    plt.legend()
    plt.tight_layout()

try:
    f = True
    while f:
        ani = FuncAnimation(plt.gcf(), animate, interval=60000)
        plt.tight_layout()
        plt.show()
        if keyboard.is_pressed('q'):
            print("Exiting...")
            sys.exit()
except Exception as e:
    print(f"Error fetching data: {e}")