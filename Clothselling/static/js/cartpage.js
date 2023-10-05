
function updateqty(id, action, var_id) {
    var quantityElement = document.getElementById('qty' + id);
    var totalPriceInput = document.getElementById('totalPriceInput' + id);


    $.ajax({
        url: 'update_quantity/',
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        data: {
            id: id,
            action: action,
            var_id: var_id,
        },
        success: function (response) {
            // Set the input box value to the new quantity

            console.log(response)
            console.log(response)
            console.log(response)
            console.log(response)
            if (response.new_quantity == 0) {
                window.alert("The minimum quantity is 1")
            }

            else if (response.new_quantity <= response.cart_Stock) {
                quantityElement.value = response.new_quantity;

                if (totalPriceInput) {
                    totalPriceInput.value = '₹ ' + response.new_total_price; // Update the total price input
                }

                // Update the total price span if needed
                var totalPriceSpan = document.querySelector('.total-price[data-item-id="' + id + '"]');
                if (totalPriceSpan) {
                    totalPriceSpan.textContent = '₹ ' + response.new_total_price;
                }
            }
            else {
                window.alert('The item is out of stock Please choose the last quantitiy or less for purchase!!')
            }

            console.log(response.message)
            console.log(response.message)
            console.log(response.message)
            console.log(response.new_quantity)
            console.log(response.new_quantity)


        },
        error: function () {
            // Handle AJAX request error, and potentially revert the changes
        }
    });
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {
    $('.pro-qty input[type="number"]').on('change', function () {
        const newQuantity = $(this).val();
        console.log(newQuantity)
        const itemId = $(this).data('item-id');

        $.ajax({
            type: 'POST',
            url: '/cart/update_quantity/', // Your server-side URL for updating quantity
            data: {
                item_id: itemId,
                quantity: newQuantity
            },
            success: function (response) {
                // Update the DOM elements with the new data
                $(`.total-price[data-item-id="${itemId}"]`).text(response.total_price);
            }
        });
    });
});
