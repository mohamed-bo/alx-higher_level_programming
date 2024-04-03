$('document').ready(function () {
    const lien = 'https://www.fourtonfish.com/hellosalut/?';
    $('INPUT#btn_translate').click(function () {
        $.get(lien + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
            $('DIV#hello').html(data.hello);
        });
    });
});
