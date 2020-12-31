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
            $("#sendEmail").addClass("no-show");
            $("#emailForm").addClass("no-show");
            $("#plane").removeClass("no-show");
        },
        function(error) {
            console.log("FAILED", error);
        },
        );
    return false;
}



