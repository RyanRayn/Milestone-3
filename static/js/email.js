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
    $("#sendEmail").addClass("no-show");
    $("#plane").removeClass("no-show");
});

/* Disable Email Submit Button Until Inputs Are Filled */
$(document).ready(function (){
    validate();
    $('#toEmail, #subject').change(validate);
});

function validate(){
    if ($('#toEmail').val().length   >   0   &&
        $('#subject').val().length  >   0) {
        $("#emailSend").prop("disabled", false);
    }
    else {
        $("#emailSend").prop("disabled", true);
    }
}
