$(document).ready(function(){
	$('.input__file input[type=file]').on('change', function(){
		let file = this.files[0];
		$(this).closest('.input__file').find('.input__file__text').html(file.name);
	});

	$("#personal__password__update").submit(function(e){
		if ($('#password').val() != $('#re-password').val()){
			e.preventDefault();
			$('#password').css('background-color', '#ffa9a9');
			$('#re-password').css('background-color', '#ffa9a9');
		}

	})

})