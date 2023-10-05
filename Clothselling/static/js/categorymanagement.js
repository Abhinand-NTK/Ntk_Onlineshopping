document.addEventListener("DOMContentLoaded", function () {
    const submitButton = document.getElementById("submitButton");
    const form = document.getElementById("myForm");
    const rangeMin = document.getElementById("myRangeMin");
    const rangeMax = document.getElementById("myRangeMax");
    const demoMin = document.getElementById("demoMin");
    const demoMax = document.getElementById("demoMax");
    const enableFilterCheckbox = document.getElementById("enableFilterCheckbox");

    function toggleSliderState() {
      var isEnabled = enableFilterCheckbox.checked;
      console.log(isEnabled)
      rangeMin.disabled = !isEnabled;
      rangeMax.disabled = !isEnabled;
    }

    rangeMin.addEventListener("input", function () {
      demoMin.innerText = rangeMin.value; // Update the displayed value
    });

    rangeMax.addEventListener("input", function () {
      demoMax.innerText = rangeMax.value; // Update the displayed value
    });

    enableFilterCheckbox.addEventListener("change", toggleSliderState);

    toggleSliderState();

    form.addEventListener("submit", function (event) {
      // event.preventDefault(); // Comment this line to allow the form to submit
      // You can add your custom logic here for handling the form submission
    });
  });




  const searchInput = document.getElementById('searchInput');
  const suggestionsContainer = document.getElementById('suggestionsContainer');

  var names=[];

  searchInput.addEventListener('input', function () {
      const query = this.value;

      console.log("Testing is under !!!!!!!!!!!!!! :- " ,query)

      // Clear previous suggestions
      suggestionsContainer.innerHTML = '';

      if (query.trim() === '') {
          return; // No need to make an empty search
      }

      fetch(`/products/search_products/${encodeURIComponent(query)}`)
          .then(response => response.json())
          .then(data => {
              // Process and display the product suggestions
              data.forEach(product => {
                  //console.log(names)

                //console.log(product.name)
                names.push(product.name)
                  const suggestion = document.createElement('div');
                  suggestion.innerText = product.name;
                  suggestion.addEventListener('click', function () {
                      // Handle suggestion click (e.g., fill the search box with the suggestion)
                      searchInput.value = product.name;
                      suggestionsContainer.innerHTML = ''; // Clear suggestions
                  });
                  suggestionsContainer.appendChild(suggestion);
              });
          })
          .catch(error => {
              console.error('Error fetching product suggestions:', error);
          });
        
  });

  

