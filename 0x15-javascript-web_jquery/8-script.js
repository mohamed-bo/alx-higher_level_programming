$(function () {
    $.get('https://swapi.dev/api/arrayfilm/?format=json', function (data, status) {
      if (status === 'success') {
        let arrayfilm = data.results;
        for (let i in arrayfilm) {
          $('#list_movies').append('<li>' + arrayfilm[i].title + '</li>');
        }
      }
    });
  });
