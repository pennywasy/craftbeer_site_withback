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
})