$('document').ready(function () {   
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (c) {
    $('div#hello').text(c.hello);
  });
});
