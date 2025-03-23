from flask import Flask, render_template, jsonify, send_from_directory # We use it to create the web application
import pandas as pd # We use it to load and process the data
import plotly.express as px # We use it to create the plot
import plotly.io as pio # We use it to convert the plot to HTML
from datetime import datetime

app = Flask(__name__) # Create the Flask application

# This function is used to load the data from the CSV file
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

def load_report_data():
    try:
	    df = pd.read_csv("/home/ubuntu/APGL_projet/docs/rapport.csv", sep=";", encoding="utf-8")
	    df.columns = ["opening_value", "min_value", "max_value", "closing_value", "volatility"]
    except FileNotFoundError:
        print("CSV file not found")
        df = pd.DataFrame({"opening_value": [0], "min_value": [0], "max_value": [0], "closing_value": [0], "volatility": [0]})
    return df

def load_history():
    try:
        df = pd.read_csv("/home/ubuntu/APGL_projet/docs/data_history.csv", sep=";", encoding="utf-8")
        df.columns=["date", "opening_value", "min_value", "max_value",  "closing_value", "volatility"]
        columns_to_convert = ["opening_value", "min_value", "max_value", "closing_value", "volatility"]

        for col in columns_to_convert:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')

    except FileNotFoundError:
        print("CSV file not found")
        df = pd.DataFrame({"date": [], "opening_value": [], "min_value": [], "max_value": [], "closing_value": [], "volatility": [] })

    return df

@app.route('/')
def index():
	current_time = datetime.now()
	start_time = current_time.replace(hour=20, minute=0, second=0, microsecond=0)
	end_time = current_time.replace(hour=9, minute=30, second=0, microsecond=0)
	df = load_data()

	if df.empty or df["value"].isna().all():
		fig = px.line(title="No data available")
	else:
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
			plot_bgcolor="rgba(255, 255, 255, 1)",
			paper_bgcolor="rgba(255, 255, 255, 1)", 
			font=dict(family="Arial, sans-serif", size=14, color="black"), 
			hovermode="closest",
		)
		
	# Generate the plotly graph in HTML format
	graphHTML = pio.to_html(fig, full_html=False)
	# Return the HTML template with the graph
	return render_template('index.html',graphHTML=graphHTML)

@app.route('/data')
def get_data():

	try:
		df = load_data()
		data = {
			"timestamp": df["timestamp"].astype(str).tolist(),
			"values": df["value"].tolist()
		}
		return jsonify(data)
	except Exception as e:
		print("Erreur:", e)
		return jsonify({"error": "Unable to load data"}), 500

@app.route('/rapport_tesla')
def get_rapport():
    try:
        df = load_report_data()
        if (df.empty or len(df)==0):
            rapport_python={"opening_value": 0, "min_value": 0, "max_value": 0, "closing_value": 0, "volatility": 0 }
            return  jsonify(rapport_python)
        last_row = df.iloc[-1]
        rapport_python={ "opening_value": last_row["opening_value"], "min_value": last_row["min_value"], "max_value": last_row["max_value"], "closing_value": last_row["closing_value"], "volatility": last_row["volatility"]  }
        return jsonify(rapport_python)

    except Exception as e:
        rapport_python={ "opening_value": 0, "min_value": 0, "max_value": 0, "closing_value": 0, "volatility": 0 }
        return  jsonify(rapport_python)

@app.route('/get-server-time')
def get_server_time():
    server_time = datetime.now().isoformat()
    return jsonify({"server_time": server_time})

@app.route('/history')
def history():
    df = load_history()
    graphs = {}
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce").dt.date
    columns=["opening_value", "min_value", "max_value", "closing_value", "volatility"]
    for col in columns:
        fig = px.line(df, x="date", y=col, title=f"Evolution de {col.replace('_',' ').capitalize()}")
        fig.update_layout(template="plotly_dark")
        fig.update_xaxes(type='category')
        fig.update_traces(line=dict(color='red'))  
        graphs[col] = pio.to_html(fig, full_html=False)

    return render_template('history.html', graphs=graphs)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
