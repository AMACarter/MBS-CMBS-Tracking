from fredapi import Fred
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

fredapi = Fred(api_key='43014c898148b01637a1c1150e17ff0c')

# Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
mbsbankdata = fredapi.get_series_latest_release('TMBACBW027SBOG')
mbsbankdata.tail()
print(mbsbankdata)

# Latest Mortgage 
mort30yeardata = fredapi.get_series_latest_release('MORTGAGE30US')
mort30yeardata.tail()
print(mort30yeardata)

root = ThemedTk(theme="Equilux")
root.title("Flamingo Trading Bot")
root.geometry("1920x1080")
       
# Generate Plot
plt.style.use('dark_background')
fig, (ax1,ax2) = plt.subplots(2)
fig.suptitle('MBS Tracking', color="blue", fontsize="30")
ax1.plot(mbsbankdata, color="blue")
ax1.set_title('Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks')
ax1.set(ylabel="Billions of U.S Dollars ($)")
ax1.set(xlabel="Year")

ax2.plot(mort30yeardata, color="blue")
ax2.set_title("30-Year Fixed Rate Mortgage Average in the United States")
plt.ylabel("Percentage (%)")
plt.xlabel("Year")
    
# Snap plot to canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.draw()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)
canvas.flush_events()
      
root.mainloop() 
