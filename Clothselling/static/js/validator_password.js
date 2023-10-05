function validateEmailOrNumber(value) {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const phoneRegex = /^\d{10}$/;

  if (emailRegex.test(value)) {
    return 'email';
  } else if (phoneRegex.test(value)) {
    return 'phone';
  } else {
    throw new Error('Invalid email or phone number');
  }
}

function validatePassword(password) {
  if (password.length < 8) {
    throw new Error('Password must be at least 8 characters long');
  }

  if (!/[A-Z]/.test(password)) {
    throw new Error('Password must contain at least one uppercase letter');
  }

  if (!/[a-z]/.test(password)) {
    throw new Error('Password must contain at least one lowercase letter');
  }

  if (!/\d/.test(password)) {
    throw new Error('Password must contain at least one digit');
  }
}

function main(event) {
  event.preventDefault(); // Prevent form submission

  const emailOrPhone = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  const usernameError = document.getElementById('username-error');
  const passwordError = document.getElementById('password-error');

  // Clear previous error messages
  usernameError.textContent = '';
  passwordError.textContent = 'Invalid Password format : it should be contain atleast Lowercase,Uppercase,Special Character,Number & Minimum length will be 8 characters  ';
  try {
    const fieldType = validateEmailOrNumber(emailOrPhone);
    validatePassword(password);
    console.log(`Valid ${fieldType} and password.`);
    // If validation passes, you can submit the form here
    document.querySelector('form').submit();
  } catch (error) {
    console.error(`Validation error: ${error.message}`);
    if (error.message.includes('email')) {
      usernameError.textContent = error.message;
    }
    if (error.message.includes('password')) {
      passwordError.textContent = error.message;
    }
  }
}
