from flask import Flask
import pandas as pd 

app = Flask(__name__) 

def load_data():
	df = pd.read_csv("/home/ubuntu/APGL_projet/docs/data.csv", sep=";", encoding="utf-8")
	df.columns = ["timestamp", "value"]
	df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
  df["value"] = pd.to_numeric(df["value"].astype(str).str.replace(',', '.'), errors='coerce')

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=5000)
