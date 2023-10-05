
function approve(id) {

    console.log(id)
    console.log(id)
    console.log(id)
    fetch(`/order/returnindivudalproducts/${id}`)
        .then(response => {

            return response.json();
        })
        .then(data => {

            const requestStatusDiv = document.querySelector('.text-warning');
            const buttonstatus = document.querySelector('.approved');
            console.log(data.refunded)

            if (data.refunded == true) {
                // Request is pending
                console.log("i am working bro!!!!!!!!")
                requestStatusDiv.innerHTML = '<p class="text-success font-weight-bold">Request Accepted & Refunded</p>';
                buttonstatus.style.display = 'none';
            }
        })
        .catch(error => {

            console.error('Fetch error:', error);
        });

}