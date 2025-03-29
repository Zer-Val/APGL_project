// JAVASCRIPT CODE TO UPDATE THE GRAPH EVERY 5 MINUTES

function updateDashboard() {
	fetch('http://13.53.122.97:5000/get-server-time')
		.then(response => response.json())
		.then(serverTimeData => {
			let serverTime = new Date(serverTimeData.server_time);
			let currentHour = serverTime.getHours();
			let currentMinute = serverTime.getMinutes();
			let isMarketOpen = (currentHour > 9 || (currentHour === 9 && currentMinute >= 30)) && currentHour < 16;
			let isTimeReport = currentHour >= 20 || (currentHour < 9 || (currentHour === 9 && currentMinute <= 29));

			fetch('http://13.53.122.97:5000/data')
				.then(response => response.json())
				.then(data => {
					if (isMarketOpen) {
						let formattedTime = data.timestamp.map(timestamp => {
							let date = new Date(timestamp);
							return date.getHours()*60 + date.getMinutes();
						});

						let timeLabels = data.timestamp.map(timestamp => {
							let date = new Date(timestamp);
							let hours = date.getHours();
							let minutes = date.getMinutes();
							return `${hours}:${minutes < 10 ? '0' + minutes : minutes}`; 
						});

						let trace = {
							x: formattedTime,
							y: data.values,
							type: 'scatter',
							line: { color: 'purple'},
							hovertemplate: '%{text}<br>Value: $%{y}<extra></extra>',
							text: timeLabels
						};

						let layout = {
							xaxis: {
								title: '', 
								tickformat: '%H:%M', 
								tickfont: { 
									color: "black", 
									family: "Arial, sans-serif", 
									size: 14, 
									weight: "bold" 
								}, 
								color: 'black', 
								showgrid: true, 
								range: [570, 960], 
								tickvals : [570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960], 
								ticktext: ['9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00'] 
							},

							yaxis : {
								title: '', 
								tickfont: { 
									color: "black", 
									family: "Arial, sans-serif", 
									size: 14, 
									weight: "bold"  
								}, 
								color: 'black', 
								showgrid: true, 
								gridcolor: "black" 
							},
							plot_bgcolor: "rgba(255, 255, 255, 0)", 
							font: {family: "Arial, sans-serif", size: 14},
						}; 
						Plotly.react('graph-container', [trace], layout);
					}
					let teslaStockValue = data.values[data.values.length - 1]; 
					document.getElementById('tesla-stock-value').textContent = `Tesla Stock current price: $${teslaStockValue}`;					
				})
				.catch(error => console.error('Error fetching data', error));

			fetch('http://13.53.122.97:5000/rapport_tesla')
				.then(response => response.json())
				.then(data => {
					let tableWrapper = document.getElementById('table-wrapper');
					let rapportTable = document.getElementById('rapport-table');
					let tableWrapperH2 = document.querySelector("#table-wrapper h2");

					let allValuesEmpty = [data.opening_value, data.min_value, data.max_value, data.closing_value, data.volatility]
						.every(value => value === null || value === undefined || value ==="");

					if (allValuesEmpty) {
						console.log("No valid data available (CSV contains only headers).");
						tableWrapper.style.display = 'none';
						rapportTable.style.display = 'none';
						if (tableWrapperH2) {
							tableWrapperH2.style.display = 'none';
						}
						return;
					}

					document.getElementById('opening-value').textContent = data.opening_value;
					document.getElementById('min-value').textContent = data.min_value;
					document.getElementById('max-value').textContent = data.max_value;
					document.getElementById('closing-value').textContent = data.closing_value;
					document.getElementById('volatility').textContent = data.volatility;

					tableWrapper.style.display = 'block';                                     
					rapportTable.style.display = 'block';
					tableWrapperH2.style.display = 'block';
				})
		})
		.catch(error => console.error('Error fetching server time 2', error));
}

setInterval(updateDashboard, 10000);	
window.onload = updateDashboard;
