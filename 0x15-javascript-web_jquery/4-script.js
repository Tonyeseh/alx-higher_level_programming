$('div#toggle_header').click(() => {
  if ($('header.green').length === 1) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
});
