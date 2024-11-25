import tkinter as tk
import requests

def fetch_properties():
    response = requests.get("http://127.0.0.1:5000/properties")
    properties = response.json()
    output = ""
    for prop in properties:
        output += f"Name: {prop['name']}, Price: {prop['price']}, ROI: {prop['roi']}%\n"
    label.config(text=output)

def analyze_property():
    price = int(entry_price.get())
    response = requests.post("http://127.0.0.1:5000/analyze", json={"price": price})
    result = response.json()
    result_label.config(text=f"Estimated ROI: {result['roi']}%")

root = tk.Tk()
root.title("Real Estate App")

label = tk.Label(root, text="Fetching properties...")
label.pack()

fetch_button = tk.Button(root, text="Fetch Properties", command=fetch_properties)
fetch_button.pack()

tk.Label(root, text="Enter Property Price:").pack()
entry_price = tk.Entry(root)
entry_price.pack()

analyze_button = tk.Button(root, text="Analyze ROI", command=analyze_property)
analyze_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
