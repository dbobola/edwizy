// Sidebar toggle function
const sidebarToggle = () => {
	document.body.classList.toggle('sidebar-open')
}

// Sidebar trigger
const sidebarTrigger = document.getElementById('main-header__sidebar-toggle')

// Add the event listener for the sidebar toggle
sidebarTrigger.addEventListener('click', sidebarToggle)



// Sidebar collapse function
const sidebarCollapse = () => {
	document.body.classList.toggle('sidebar-collapsed')
}

// Sidebar trigger
const sidebarCollapseTrigger = document.getElementById('sidebar__collapse')

// Add the event listener for the sidebar toggle
sidebarCollapseTrigger.addEventListener('click', sidebarCollapse)



// Theme switcher function
const switchTheme = () => {
	// Get root element and data-theme value
	const rootElem = document.documentElement
	let dataTheme = rootElem.getAttribute('data-theme'),
		newTheme

	newTheme = (dataTheme === 'light') ? 'dark' : 'light'

	// Set the new HTML attribute
	rootElem.setAttribute('data-theme', newTheme)
	

	// Set the new local storage item
	localStorage.setItem("theme", newTheme)
	location.reload()
}

// Add the event listener for the theme switcher
document.querySelector('#sidebar__theme-switcher').addEventListener('click', switchTheme)



// // Convert the Django context variable to JavaScript
// var data = JSON.parse('{{ data }}');

// // Extract relevant data for the chart
// var dates = data.map(row => row.time);
// var opens = data.map(row => row.ask);
// var highs = data.map(row => row.bid);
// var lows = data.map(row => row.ask_volume);
// var closes = data.map(row => row.bid_volume);

// // Create the candlestick chart using Plotly
// var trace = {
// 	x: dates,
// 	open: opens,
// 	high: highs,
// 	low: lows,
// 	close: closes,
// 	type: 'candlestick',
// 	increasing: { line: { color: 'green' } },
// 	decreasing: { line: { color: 'red' } },
// };

// var layout = {
// 	title: 'Forex Chart',
// 	xaxis: { title: 'Time' },
// 	yaxis: { title: 'Price' }
// };

// Plotly.newPlot('chart', [trace], layout);

