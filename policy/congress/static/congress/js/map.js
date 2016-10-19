var map = new Datamap({
	element: document.getElementById('container'),
	scope: 'usa',
	responsive: true,
	done: function(datamap) {
		datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
			window.location.href = "/state/" + geography.id;
		});
	}
});

window.addEventListener('resize', function() {
	map.resize();
});

map.labels();
