$(() => {
  $('input#btn_translate').click(() => {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + $('input#language_code').val();
    $.get(url, (data) => {
      $('div#hello').text(data.hello);
    });
  });
});
