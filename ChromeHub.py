# Modules for starting chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# GUI
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
# Other
import os

root = tk.Tk()
root.geometry("500x500")
root.title("ChromeHub 1.1.0")
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
        save_tab = open("ChromeHubStartupTabs.txt", "w")
        save_tab.write(open_start_tabs_entry.get() + " ")
        start_tabs.append(open_start_tabs_entry.get())
        save_tab.close()
        start_tab_list_label.config(text="Tabs: " + str(start_tabs))
        os.system("ChromeHubStartupTabs.txt")
    except:
        tkinter.messagebox.showerror("Error", "An error occurred while saving and opening the file or the entry is not filled in properly.")

open_website_head = tk.Label(root, text="Open Website")
open_website_head.grid(row=0, column=0)
open_web_btn_1 = tk.Button(root, text="Google", command=lambda: [open_google()])
open_web_btn_1.grid(row=1, column=0)
open_web_btn_2 = tk.Button(root, text="Gmail", command=lambda: [open_gmail()])
open_web_btn_2.grid(row=1, column=1)
connect_ip_head = tk.Label(root, text="Connect IP Address")
connect_ip_head.grid(row=2, column=0)
ip_input = tk.Entry(root, width=30)
ip_input.grid(row=3, column=0)
ip_connect = tk.Button(root, text="Connect", command=lambda: [ip()])
ip_connect.grid(row=3, column=1)
sec2_lab = tk.Label(root, text="Open Tabs on Startup")
sec2_lab.grid(row=4, column=0)
sep = ttk.Separator(root, orient='horizontal')
sep.grid(row=5, column=0, sticky='ew')
open_start_tabs_entry = tk.Entry(root, width=30)
open_start_tabs_entry.grid(row=6, column=0)
add_start_tab = tk.Button(root, text='Add Tab', command=lambda: [add_tab()])
add_start_tab.grid(row=6, column=1)
start_tab_list_label = tk.Label(root, text="Tabs: " + str(start_tabs))
start_tab_list_label.grid(row=6, column=2)
root.mainloop()
