$(function(){
    $("#Analyze").hide();
  $('#PisaLink').click(function(){
     $('#Pisa').show();
     $('#Analyze').hide();
     $('#Search').hide();
  });
  $('#AnalyzeLink').click(function(){
     $('#Pisa').hide();
      $('#Search').hide();
     $('#Analyze').show();
  });
    $('#SearchLink').click(function(){
     $('#Pisa').hide();
      $('#Search').show();
     $('#Analyze').hide();
  });
});
