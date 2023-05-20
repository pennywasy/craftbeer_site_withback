$(document).ready(function () {
  $("#button1").click(function () {
    $("#catalog").modal({
      fadeDuration: 500,
      fadeDelay: 0.1,
      escapeClose: false,
      showClose: false,
    });
  });
});