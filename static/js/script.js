/* Flash Message Timeout */
setTimeout(function() {
    $('#flash_message').fadeOut('fast');
}, 2500);



/* TABS PAGE */



/* Toggle Create New, Edit and Delete buttons */    
$(".add-edit-delete").click(function(){
  $(".no-show").toggle();
});



/* PROFILE PAGE */



/* Change entry modal colors based on emotion chosen */
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

/* Toggle text for entry modal and enter hidden input for "emotion" */
$(".happy").click(function(){
  $(".insert-1").text("");
  $(".insert-2").text("is the best! Give us the details.");
  $("#entry_emotion").val("happy");
});

$(".sad").click(function(){
    $(".insert-1").text("Aww, what did ");
    $(".insert-2").text("do this time?");
    $("#entry_emotion").val("sad");
});

$(".angry").click(function(){
    $(".insert-1").text("");
    $(".insert-2").text("makes me so MAD!!!");
    $("#entry_emotion").val("angry");
});

/* Enter date values in hidden input fields on the Entry Modal */
function setValues(){

let monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"]

let d = new Date();
let monthNumber = d.getMonth();
let monthName = monthNames[monthNumber];
let currentYear = d.getFullYear();
let currentDate = d.getDate();
let today = monthName + " " + currentDate + "," + " " + currentYear;

$('#entry_month').val(monthName);
$('#entry_year').val(currentYear);
$('#entry_date').val(today);
}

/* Send Email Function */
function sendMail(emailSend) {
    emailjs.send("KeepingTABS", "template_s61f969", {
       "toEmail": emailSend.toEmail.value,
       "subject": emailSend.subject.value,
       "message": emailSend.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        });
    return false;
}

/* Hide email form on submission */
$(document).ready(function(){
    $( "#emailSend" ).click(function() {
        $( "#emailForm" ).hide( "slow", function() {
    });
});
}); 

/* Change header message when email sends */
$("#emailSend").click(function(){
    $("#email-h3").addClass("no-show");
    $("#email-h1").removeClass("no-show");
});