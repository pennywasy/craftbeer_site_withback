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
		if ($('#password').val() != $('#re-password').val()){
			e.preventDefault();
			$('#password').css('background-color', '#ffa9a9');
			$('#re-password').css('background-color', '#ffa9a9');
		}

	})

})