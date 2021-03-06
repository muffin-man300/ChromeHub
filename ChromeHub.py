# Modules for starting chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import webbrowser
# GUI
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
# Other
import os

root = tk.Tk()
root.geometry("500x500")
root.title("ChromeHub 1.2.0")
s = Service('C:/Windows/chromedriver.exe')
start_tabs = []

def open_google():
    driver = webdriver.Chrome(service=s)
    driver.get('https://www.google.com/')


def open_gmail():
    driver = webdriver.Chrome(service=s)
    driver.get('https://mail.google.com/')
    

def ip():
    driver = webdriver.Chrome(service=s)
    ip_in = ip_input.get()
    driver.get("https://" + ip_in + "/")
    
    
def add_tab():
    try:
        start_tabs.append(open_start_tabs_entry.get())
        start_tab_list_label.config(text="Tabs: " + str(start_tabs))
    except:
        tkinter.messagebox.showerror("Error", "An error occurred while saving and opening the file or the entry is not filled in properly.")
        
        
def open_in_chrome():
    if len(start_tabs) > 0:
        for i in start_tabs:
            webbrowser.open(i)
    else:
        tkinter.messagebox.showerror('Error', 'Please add a tab to continue.')

                
# Heading
open_website_head = tk.Label(root, text="Open Website")
open_website_head.grid(row=0, column=0)
#

# Open Websites
open_web_btn_1 = tk.Button(root, text="Google", command=lambda: [open_google()])
open_web_btn_1.grid(row=1, column=0)
open_web_btn_2 = tk.Button(root, text="Gmail", command=lambda: [open_gmail()])
open_web_btn_2.grid(row=1, column=1)
#

# Heading
connect_ip_head = tk.Label(root, text="Connect IP Address")
connect_ip_head.grid(row=2, column=0)
#

# Input
ip_input = tk.Entry(root, width=30)
ip_input.grid(row=3, column=0)
#

# Connect IP Button
ip_connect = tk.Button(root, text="Connect", command=lambda: [ip()])
ip_connect.grid(row=3, column=1)
#

# Heading
open_tabs_lab = tk.Label(root, text="Open Tabs in Chrome")
open_tabs_lab.grid(row=4, column=0)
#

# Seperator
sep = ttk.Separator(root, orient='horizontal')
sep.grid(row=5, column=0, sticky='ew')
#

# Open in Chrome Entry
open_start_tabs_entry = tk.Entry(root, width=30)
open_start_tabs_entry.grid(row=6, column=0)
#

# Add Tab
add_start_tab = tk.Button(root, text='Add Tab', command=lambda: [add_tab()])
add_start_tab.grid(row=6, column=1)
#

# Tab List
start_tab_list_label = tk.Label(root, text="Tabs: " + str(start_tabs))
start_tab_list_label.grid(row=7, column=0)
#

# Open in Chrome
open_startup_btn = tk.Button(root, text='Open tabs in Chrome', command=lambda: [open_in_chrome()])
open_startup_btn.grid(row=8, column=0)
#

root.mainloop()
