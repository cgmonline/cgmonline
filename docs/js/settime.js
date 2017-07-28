var nextYear = moment.tz("2018-01-01 00:00", "America/Sao_Paulo");

$('#clock').countdown(nextYear.toDate(), function(event) {
  $(this).html(event.strftime('%D days %H:%M:%S'));
});
