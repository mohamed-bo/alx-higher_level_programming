$('document').ready(function () {
    $('INPUT#btn_translate').click(ytra);
    $('INPUT#language_code').focus(function () {
        $(this).keydown(function (e) {
            if (e.keyCode === 13) {
                ytra();
            }
        });
    });
});

function ytra () {
    const lien = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(lien + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
    });
}
