$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (c) {
  $('div#character').text(c.name);
});
