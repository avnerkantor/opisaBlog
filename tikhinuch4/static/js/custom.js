
$(function(){
    $("#achievements").hide();
    $("#students").hide();
    $("#analyze").hide();
     $('#dictionary').hide();
  $('#PisaLink').click(function(){
       $("#carousel").hide();
     $('#achievements').show();
      $("#students").hide();
     $('#analyze').hide();
     $('#dictionary').hide();
  });
    $('#Pisa2Link').click(function(){
         $("#carousel").hide();
     $('#achievements').hide();
      $("#students").show();
     $('#analyze').hide();
     $('#dictionary').hide();
  });
  $('#AnalyzeLink').click(function(){
       $("#carousel").hide();
     $('#achievements').hide();
      $("#students").hide();
      $('#dictionary').hide();
     $('#analyze').show();
  });
    $('#SearchLink').click(function(){
         $("#carousel").hide();
     $('#achievements').hide();
        $("#students").hide();
      $('#dictionary').show();
     $('#analyze').hide();
  });
});

//$(function () {
//    $('#aa').click(function () {
//        alert("df");
//        $('#myiframe').contents().find('#7448-3').click();
//    });
//});

