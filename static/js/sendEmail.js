function sendMail(bookingForm) {
    emailjs.send("service_iqkqrva", "mamaskitchen", {
        "from_name": bookingForm.name.value, 
        "from_email": bookingForm.email.value,
        "phone": bookingForm.phone.value,
        "party_size": bookingForm.party_size.value,
        "date": bookingForm.date.value,
        "time": bookingForm.time.value,
        "special_occasion": bookingForm.special_occasion.value,
        "special_requirements": bookingForm.special_requirements.value,
        "booking_ref": bookingForm.booking_ref.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
}

function sendForm(contactForm) {
    emailjs.send("service_iqkqrva", "contactme", {
        "from_name": contactForm.name.value, 
        "from_email": contactForm.email.value, 
        "phone": contactForm.phone.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS!", response); 
        },
        function(error) {
            console.log("FAIL!", error);
        }); 
}