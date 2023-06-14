$("#remove__all_from__cart").click(function(e){
	e.preventDefault();
	$.post('/cart/deleteAllFromCart/', {}, function(data){
		$("#cart").html(data);
	})
})