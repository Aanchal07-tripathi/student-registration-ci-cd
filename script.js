const form = document.getElementById("registrationForm");
const message = document.getElementById("message");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const roll = document.getElementById("roll").value;
    const course = document.getElementById("course").value;
    const phone = document.getElementById("phone").value;

    if (!name || !email || !roll || !course || !phone) {
        message.textContent = "Please fill all the fields.";
        return;
    }

    message.textContent =
        "Registration successful! Welcome, " + name + ".";

    form.reset();
});