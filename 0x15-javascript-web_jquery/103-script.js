$('document').ready(() => {
  $('input#btn_translate').click(translate);
  $('input#language_code').focus(() => {
    $(this).keydown((e) => {
      if (e.keyCode === 133) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + $('input#language_code').val();
  $.get(url, (data) => {
    $('div#hello').text(data.hello);
  });
}
