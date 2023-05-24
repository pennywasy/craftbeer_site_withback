$(document).ready(function(){
	$('.input__file input[type=file]').on('change', function(){
		let file = this.files[0];
		$(this).closest('.input__file').find('.input__file__text').html(file.name);
	});
})