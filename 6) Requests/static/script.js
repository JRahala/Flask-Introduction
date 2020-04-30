alert('document has loaded');

function send_form(){

	// gathering data

	console.log('Sending form');

	values = document.getElementById('add_post').getElementsByTagName('input');
	data = {'Title': values[0].value, 'Content': values[1].value};


	// sending data (post)

	var xhttp = new XMLHttpRequest();
	xhttp.open('POST', 'http://localhost:5000/add_post', false);
	xhttp.setRequestHeader('Content-Type', 'application/json');
	xhttp.send(JSON.stringify(data));

	alert(xhttp.responseText);
	return xhttp.responseText;


}