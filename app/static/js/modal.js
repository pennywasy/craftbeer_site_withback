$(document).ready(function () {
  $("#button1").click(function () {
    $("#catalog").modal({
      fadeDuration: 500,
      fadeDelay: 0.1,
      escapeClose: false,
      showClose: false,
    });
  });


  $("#button__login").click(function () {
    $("#login__wrapper").modal({
      fadeDuration: 500,
      fadeDelay: 0.1,
      escapeClose: false,
      showClose: false,
    });
  });

  $("#button__registry").click(function() {
    $("#registry__wrapper").modal({
      fadeDuration: 500,
      fadeDelay: 0.1,
      escapeClose: false,
      showClose: false,
    });
  });
});