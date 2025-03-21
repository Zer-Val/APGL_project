from flask import Flask, render_template, jsonify, send_from_directory 
import pandas as pd 
import plotly.express as px 
import plotly.io as pio 

app = Flask(__name__) 

def load_data():
	try:
		df = pd.read_csv("/home/ubuntu/APGL_projet/docs/data.csv", sep=";", encoding="utf-8")
		df.columns = ["timestamp", "value"]
		df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
		df["value"] = pd.to_numeric(df["value"].astype(str).str.replace(',', '.'), errors='coerce')
	except FileNotFoundError:
		print("CSV file not found")
		df = pd.DataFrame({"timestamp": [], "value": []})
	return df


@app.route('/')
def index():
	df = load_data()

	fig = px.line(df, x="timestamp", y="value")
	fig.update_traces(line=dict(color='purple'))
	fig.update_layout(
		xaxis_title='',
		yaxis_title='',
		xaxis=dict(
			tickformat="%H:%M:%S",
			tickfont=dict(color='black', family='Arial, sans-serif', size=14, weight='bold'),
            showgrid=True,
            gridcolor="gray"                
		),
		yaxis=dict(
			tickfont=dict(color='black', family='Arial, sans-serif', size=14, weight='bold'),  
			showgrid=True,
			gridcolor="gray"
		),
	)

	graphHTML = pio.to_html(fig, full_html=False)
	return render_template('index.html',graphHTML=graphHTML)

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=5000)
