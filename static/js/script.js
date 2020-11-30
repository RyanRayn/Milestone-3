/* Home Page */

/* Change +,- icons for accordion on click */
$('.icon-toggle').click(function(){ 
    $(this).find('i').toggleClass('fa-plus-circle fa-minus-circle'); 
});

/* Tabs Page */

/* Toggle Create New, Edit and Delete buttons */    
$(".add-edit-delete").click(function(){
  $(".no-show").toggle();
});

$(".sad").click(function(){
    $(".entry-modal, .modal-delete").removeClass("entry-modal modal-delete").addClass("modal-new");
    $(".entry-input, .delete-input").removeClass("entry-input delete-btn").addClass("new-input");
    $(".entry-button, .delete-btn").removeClass("entry-button delete-btn").addClass("new-btn");
});

$(".happy").click(function(){
    $(".modal-new, .modal-delete").removeClass("modal-new modal-delete").addClass("entry-modal");
    $(".new-input, .delete-input").removeClass("new-input delete-input").addClass("entry-input");
    $(".new-btn, .delete-btn").removeClass("new-btn delete-btn").addClass("entry-button");
});

$(".angry").click(function(){
    $(".modal-new, .entry-modal").removeClass("modal-new entry-modal").addClass("modal-delete");
    $(".new-input, .entry-input").removeClass("new-input entry-input").addClass("delete-input");
    $(".new-btn, .entry-button").removeClass("new-btn entry-button").addClass("delete-btn");
});

$(".happy").click(function(){
  $(".insert-text").text("is the best! Give us the details.");
  $(".insert-2").text("");
});

$(".sad").click(function(){
    $(".insert-2").text("Aww, what did ");
    $(".insert-text").text("do this time?");
});

$(".angry").click(function(){
    $(".insert-text").text("makes me so MAD!!!");
    $(".insert-2").text("");
});