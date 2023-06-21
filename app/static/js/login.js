$(document).ready(function(){
	$("input[type='radio']").on('change', function(){
		if($('#tabs1').is(":checked")){
			$("#login").attr('placeholder', 'Логин');
		}else if($('#tabs2').is(":checked")){
			$("#login").attr('placeholder', 'Email');
		}else{
			$("#login").attr('placeholder', 'Номер телефона');
		}
	})


	$('.input__file input[type=file]').on('change', function(){
		let file = this.files[0];
		$(this).closest('.input__file').find('.input__file__text').html(file.name);
	});

	$("#form__registry").submit(function(e){
		e.preventDefault();
		let data = new Date($("#birthday").val());
	    let now = new Date();
	    let today = new Date(now.getFullYear(), now.getMonth(), now.getDate()); 
	    let datanow = new Date(today.getFullYear(), data.getMonth(), data.getDate());
	    let age = today.getFullYear() - data.getFullYear();
	    if(today < datanow){
        	age -= 1;
   		}

		if ($('#password').val() != $('#re-password').val()){
			e.preventDefault();
			$('#password').attr('class', 'error');
			$('#re-password').attr('class', 'error');
		}

		if(age < 18){
			e.preventDefault();
			$("#birthday").attr('class', 'error');

		}

	})

})