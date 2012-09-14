

$(document).ready(function() {


  $('#no_table_provider_type__row').hide();
  $('#company').hide();

  $('#no_table_role').live('change', function () {
    if ($(this).val() == 3 || $(this).val() == 4) {
      if ($(this).val() == 3) { 
        $('#no_table_provider_type__row').fadeIn();
      } else {
        $('#no_table_provider_type__row').fadeOut();
        $("#no_table_role > option:eq(0)").attr('selected', 'selected');
        $('#company input').val(null);
        $('#company textarea').val(null);
      }
        $('#company').fadeIn();
    } else {
        $('#company').fadeOut();
        $("#no_table_role > option:eq(0)").attr('selected', 'selected');
        $('#company input').val(null);
        $('#company textarea').val(null);
    }
  }); 

}); 
