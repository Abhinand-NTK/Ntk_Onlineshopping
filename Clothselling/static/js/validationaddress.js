const phoneRegex = /^\d{10}$/;
const pincodeRegex = /^\d{6}$/;
const nameregex = /^(?=.*[A-Za-z])[A-Za-z\s]+$/;


document.getElementById("firstname").addEventListener("input", function () {
    const firstname = this.value.trim(); // Remove leading and trailing spaces

    if (nameregex.test(firstname)) {
        document.getElementById("validationMessageforfirstname").textContent = " ";
        document.getElementById("validationMessageforfirstname").style.color = 'green';
    } else {
        document.getElementById("validationMessageforfirstname").textContent = "Please Enter a  valid Name";
        document.getElementById("validationMessageforfirstname").style.color = 'red';
    }
});


document.getElementById("lastname").addEventListener("input", function () {
    const lastname = this.value.trim(); // Remove leading and trailing spaces

    if (nameregex.test(lastname)) {
        document.getElementById("validationMessageforlastname").textContent = " ";
        document.getElementById("validationMessageforlastname").style.color = 'green';
    } else {
        document.getElementById("validationMessageforlastname").textContent = "Please Enter a  valid LastName";
        document.getElementById("validationMessageforlastname").style.color = 'red';
    }
});


document.getElementById("address").addEventListener("input", function () {
    const address = this.value.trim(); // Remove leading and trailing spaces

    if (nameregex.test(address)) {
        document.getElementById("validationMessageforaddress").textContent = " ";
        document.getElementById("validationMessageforaddress").style.color = 'green';
    } else {
        document.getElementById("validationMessageforaddress").textContent = "Please Enter a  valid Address";
        document.getElementById("validationMessageforaddress").style.color = 'red';
    }
});

document.getElementById("town").addEventListener("input", function () {
    const town = this.value.trim(); // Remove leading and trailing spaces

    if (nameregex.test(town)) {
        document.getElementById("validationMessagefortown").textContent = " ";
        document.getElementById("validationMessagefortown").style.color = 'green';
    } else {
        document.getElementById("validationMessagefortown").textContent = "Please Enter a  valid Town";
        document.getElementById("validationMessagefortown").style.color = 'red';
    }
});

document.getElementById("nearbylocation").addEventListener("input", function () {
    const nearbylocation = this.value.trim(); // Remove leading and trailing spaces

    if (nameregex.test(nearbylocation)) {
        document.getElementById("validationMessagefornearbylocation").textContent = " ";
        document.getElementById("validationMessagefornearbylocation").style.color = 'green';
    } else {
        document.getElementById("validationMessagefornearbylocation").textContent = "Please Enter a  valid nearbylocation";
        document.getElementById("validationMessagefornearbylocation").style.color = 'red';
    }
});


document.getElementById("district").addEventListener("input", function () {
    const district = this.value.trim(); // Remove leading and trailing spaces

    if (nameregex.test(district)) {
        document.getElementById("validationMessagefordistrict").textContent = " ";
        document.getElementById("validationMessagefordistrict").style.color = 'green';
    } else {
        document.getElementById("validationMessagefordistrict").textContent = "Please Enter a  valid District";
        document.getElementById("validationMessagefordistrict").style.color = 'red';
    }
});






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
    const firstname = document.getElementById("firstname").value.trim(); // Remove leading and trailing spaces

    if (phoneRegex.test(phonenumber) && pincodeRegex.test(zipcode) && nameregex.test(firstname))   {
        document.getElementById("validationMessage").textContent = "Form submitted successfully!";
        document.getElementById("addressform").submit();
    } else {
        document.getElementById("validationMessage").textContent = "Invalid input. Please enter valid phone number and ZIP code.";
    }
});