$(document).ready(function(){
	$("#form__admin").submit(function(e){
		e.preventDefault();
		$.ajax({
			type: "POST",
			url: "/admin/product/",
			data: new FormData($("#form__admin")[0]),
			processData: false,
			contentType: false,
            success: function(data){
                $("#result").html(`<span>${data}</span>`);
            }
		});
	});
});


    // $("#form").submit(function(e){
    //     e.preventDefault();
    //     let myData = $("#form").serialize();
    //     $.ajax({
    //         type: "POST",
    //         url: "file.php",
    //         data: new FormData($("#form")[0]),
    //         processData: false, 
    //         contentType: false, 
    //         success: function(data){
    //             $("#result").html(data);
    //         }
    //     });

    // })