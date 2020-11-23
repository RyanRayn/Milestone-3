/* Home Page */

/* Change +,- icons for accordion on click */
$('.icon-toggle').click(function() { 
    $(this).find('i').toggleClass('fa-plus-circle fa-minus-circle'); 
});

/* Tabs Page */

/* Toggle Create New, Edit and Delete buttons */    
$(".add-edit-delete").click(function(){
  $(".no-show").toggle();
});    