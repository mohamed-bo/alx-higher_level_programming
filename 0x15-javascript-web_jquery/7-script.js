$(function () {
    $.get('https://swapi.dev/api/people/5/?format=json', function (data, status) {
      if (status === 'success') {
        $('#character').text(data.name);
      }
    });
  });
  