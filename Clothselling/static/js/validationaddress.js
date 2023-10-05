const phoneRegex = /^\d{10}$/;
const pincodeRegex = /^\d{6}$/;

document.getElementById("phonenumber").addEventListener("input", function () {
    const phonenumber = this.value.trim(); // Remove leading and trailing spaces

    if (phoneRegex.test(phonenumber)) {
        document.getElementById("validationMessage").textContent = phonenumber + " is a valid phone number.";
        document.getElementById("validationMessage").style.color = 'green';
    } else {
        document.getElementById("validationMessage").textContent = "Invalid phone number. Please enter 10 digits.";
        document.getElementById("validationMessage").style.color = 'red';
    }
});

document.getElementById("zipcode").addEventListener("input", function () {
    const zipcode = this.value.trim(); // Remove leading and trailing spaces

    if (pincodeRegex.test(zipcode)) {
        document.getElementById("validationMessageforzipcode").textContent = zipcode + " is a valid ZIP code.";
        document.getElementById("validationMessageforzipcode").style.color = 'green';
    } else {
        document.getElementById("validationMessageforzipcode").textContent = "Invalid ZIP code. Please enter 6 digits.";
        document.getElementById("validationMessageforzipcode").style.color = 'red';
    }
});

document.getElementById("addressform").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    const phonenumber = document.getElementById("phonenumber").value.trim(); // Remove leading and trailing spaces
    const zipcode = document.getElementById("zipcode").value.trim(); // Remove leading and trailing spaces

    if (phoneRegex.test(phonenumber) && pincodeRegex.test(zipcode)) {
        document.getElementById("validationMessage").textContent = "Form submitted successfully!";
        document.getElementById("addressform").submit();
    } else {
        document.getElementById("validationMessage").textContent = "Invalid input. Please enter valid phone number and ZIP code.";
    }
});