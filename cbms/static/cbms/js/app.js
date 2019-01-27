$(function(){
  $("#id_choice").change(function(){
    var selected = $("option").val();
    $("#submit_form").submit();
    });
});
