function grab_location() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(got_location);
	}
	else {
		alert("Couldn't get your location");
	}
}

function got_location(pos) {
	var lat = pos.coords.latitude;
	var lon = pos.coords.longitude;
	var url = "/locate?lat=" + lat + "&lon=" + lon;
	$.ajax({
		url: url,
		type: "GET",
		async: true,
		
		success: function(data) {
			var redirect_url = "/my_district/" + data.state + "/" + data.district;
			window.location.href = redirect_url;
		},
		error: function() {
			alert("didnt work");
		}
	});
}
