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
		
	graphHTML = pio.to_html(fig, full_html=False)
	return render_template('index.html',graphHTML=graphHTML)

@app.route('/rapport_tesla')
def get_repport():
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

if __name__ == "__main__": # If the script is executed directly
	app.run(debug=True, host="0.0.0.0", port=5000) # Start the web server at port 5000
