$("#cart").submit(function(e){
	e.preventDefault();
	sendData = $("#cart").serialize();
	$.post('/addCart/', sendData, function(data) {
		$("#result").html(data);
	})

})

