
function validateForm() {
    const inputElement = document.getElementById('imagesselect');
    const price = document.getElementById('price').value; // Get the value of the price input
    const stock = document.getElementById('stock').value; // Get the value of the stock input
    const selectedFiles = inputElement.files;
  
    console.log(selectedFiles);
  
    // Check if the number of selected files is not exactly 4
    if (selectedFiles.length !== 4) {
      Swal.fire('Please select exactly 4 images.');
      return false; // Prevent form submission
    }
  
    // Check if the price field is empty
    if (!price) {
      Swal.fire('Please Enter the Price Field.');
      return false; // Prevent form submission
    }
  
    // Check if the stock field is empty
    if (!stock) {
      Swal.fire('Please Enter the Stock Field.');
      return false; // Prevent form submission
    }
  
    // If validation passes, allow form submission
    return true;
  }