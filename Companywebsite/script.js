
document.getElementById("contactForm").addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let subject = document.getElementById("subject").value.trim();
    let message = document.getElementById("message").value.trim();

    let error = document.getElementById("error");

    let namePattern = /^[A-Za-z ]+$/;
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (name === "") {
        error.innerHTML = "Please enter your name.";
        error.style.color = "red";
    }

    else if (!namePattern.test(name)) {
        error.innerHTML = "Name should contain only letters.";
        error.style.color = "red";
    }

    else if (email === "") {
        error.innerHTML = "Please enter your email.";
        error.style.color = "red";
    }

    else if (!emailPattern.test(email)) {
        error.innerHTML = "Incorrect email! Please enter a valid email.";
        error.style.color = "red";
    }

    else if (subject === "") {
        error.innerHTML = "Please enter the subject.";
        error.style.color = "red";
    }

    else if (message === "") {
        error.innerHTML = "Please enter your message.";
        error.style.color = "red";
    }

    else {
        error.innerHTML = "Form submitted successfully!";
        error.style.color = "green";

        document.getElementById("contactForm").reset();
    }

});
