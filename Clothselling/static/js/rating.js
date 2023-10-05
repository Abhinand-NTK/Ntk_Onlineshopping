document.addEventListener('DOMContentLoaded', function () {
    const ratingForm = document.getElementById('ratingForm');
    const ratingInput = document.getElementById('id_rating_user');
    const stars = ratingForm.getElementsByClassName('star');
    const reviewCommentInput = document.getElementById('review_comment');

    const reviewCommentField = document.querySelector('[name="{{ rating_form.review_comment.name }}"]');

    varient_id = document.getElementById('varient_id')


    // Initialize the rating value
    let currentRating = parseInt(ratingInput.value);
    updateStars(currentRating);

    ratingForm.addEventListener('click', function (event) {
        const selectedStar = event.target;

        if (selectedStar.classList.contains('star')) {
            const ratingValue = parseInt(selectedStar.getAttribute('data-value'));
            currentRating = ratingValue;
            ratingInput.value = currentRating;

            // Update star styles based on the selected rating
            updateStars(currentRating);
        }
    });

    ratingForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the rating and review comment values

        const ratingValue = ratingInput.value;
        const reviewComment = reviewCommentInput.value;


        // Prepare the data to send to the backend
        const formData = {};
        formData['rating'] = ratingValue;
        formData['review_comment'] = reviewCommentField.value;

        const jsonData = JSON.stringify(formData);



        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const headers = new Headers({
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        });



        varient_idvalue = varient_id.value




        const url = `/rating/${varient_idvalue}`;

        fetch(url, {
            method: 'POST',
            body: jsonData,
            headers: headers,
        })
            .then(response => {
                if (response.ok) {
                    // Handle success, e.g., show a success message
                    console.log('Rating submitted successfully');
                    // You can redirect the user or display a success message here
                    hide_review_box.style.display = 'none'

                    ratingForm.reset()

                } else {
                    // Handle errors, e.g., show an error message
                    console.error('Error submitting rating');
                    //hide_review_box.style.display = 'none'

                }
            })
            .catch(error => {
                // Handle network or other errors
                console.error('Error:', error);
                //hide_review_box.style.display = 'none'

            });
    });

    // Function to update star styles
    function updateStars(ratingValue) {
        for (let i = 0; i < stars.length; i++) {
            const star = stars[i];
            if (i < ratingValue) {
                star.classList.add('selected');
            } else {
                star.classList.remove('selected');
            }
        }
    }
});
