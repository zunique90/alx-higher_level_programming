$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (c) {
  $('UL#list_movies').append(...c.results.map(movie => `<li>${movie.title}</li>`));
});
