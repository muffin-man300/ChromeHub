# Modules for starting chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# GUI
import tkinter as tk


root = tk.Tk()
root.geometry("500x500")
root.title("ChromeHub 1.0.0")
s = Service('C:/Windows/chromedriver.exe')


def open_google():
    driver = webdriver.Chrome(service=s)
    driver.get('https://www.google.com/')


def open_gmail():
    driver = webdriver.Chrome(service=s)
    driver.get('https://mail.google.com/')
    

def ip():
    driver = webdriver.Chrome(service=s)
    ip_in = ip_input.get()
    driver.get("https://" + ip_in)

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
root.mainloop()
