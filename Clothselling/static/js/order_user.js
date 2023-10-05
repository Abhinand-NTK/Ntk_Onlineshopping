var showModal = '{{ request.session.show_modal|default:"False"|lower }}';

            document.addEventListener('DOMContentLoaded', function () {
                // Check if the JavaScript variable 'showModal' is set to true
                if (showModal === "true") {
                    // Display the modal on page load
                    $('#modalDiscount').modal('show');
        
                    // Remove the 'show_modal' session variable using a fetch request
                    fetch('/order/remove-show-modal/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrftoken,  // Replace with your CSRF token if needed
                        },
                    }).then(function (response) {
                        // Handle the response here if needed
                        if (response.status === 200) {
                            // Session variable removed
                        } else {
                            // Handle error if the removal fails
                        }
                    });
                }
            });