
//For sending the details to the back end and collect the address data for initiziate the online payement//

// Global Variables for shariing the details of the project to diffrent post and access them it in separeatly in the sucess functions

var addressDetailsFromFirstAjax;

var selectedAddressId;

var payement_method_for_Shopping;

$(document).ready(function () {
    $('input[type=radio][name=address]').change(function () {
        selectedAddressId = $(this).val();
        console.log('Selected Address ID:', selectedAddressId);
        var selectedAddressId1 = $(this).attr('id'); // Retrieve the ID of the selected radio button
        address_id = selectedAddressId

        payement_method_for_Shopping =

            console.log('Selected Address ID:', selectedAddressId1);
        //var selectn =  document.getElementById("addressDetails").textContent
        //console.log(se)
        // Make an AJAX request to retrieve address details
        $.ajax({
            url: '/order/get-address-details/',
            method: 'GET',
            dataType: 'json', // Specify that the response is JSON
            data: { id: selectedAddressId },
            success: function (addressDetails) {


                // Store the data in the variable
                addressDetailsFromFirstAjax = addressDetails;

                // Now, you can access the JSON data directly
                var first_name = addressDetails.first_name
                console.log(first_name)
                console.log('First Name:', addressDetails.first_name);
                console.log('Last Name:', addressDetails.last_name);
                console.log('Phone Number:', addressDetails.phonenumber);
                console.log('Address:', addressDetails.address);
                console.log('Town:', addressDetails.town);
                console.log('Zip Code:', addressDetails.zip_code);
                console.log('Nearby Location:', addressDetails.nearbylocation);
                console.log('District:', addressDetails.district);
                console.log('Created:', addressDetails.created);
                console.log('Id:', selectedAddressId);
                console.log('payement_method_for_Shopping:', addressDetails.payement_method);

                // You can also update other parts of your UI with these variables
                $('#streetInput').val(addressDetails.address);
                $('#cityInput').val(addressDetails.town);
                $('#stateInput').val(addressDetails.district);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }

        });
    });
});

function walletpayment() {
    var formData1 = document.getElementById('addressForm');

    let address_id = formData1.address.value;
    var total_price = formData1.total_price_input.value;
    var GrandTotal = formData1.GrandTotal_input.value;
    var radio_button = formData1.querySelectorAll('input[name="payment-method"]');
    for (var i = 0; i < radio_button.length; i++) {
        if (radio_button[i].checked) {
            selectedPaymentMethod = radio_button[i].value;
            break; // Stop looping once a checked radio button is found
        }
    }

    var payment_method = selectedPaymentMethod


    // Now you have the selected payment method in the selectedPaymentMethod variable
    console.log('Selected payment method:', selectedPaymentMethod);

    var discount = formData1.discount_price.value;
    var tax = formData1.tax_input.value;

    console.log("The isuse is here", selectedAddressId)


    if (!selectedAddressId) {
        Swal.fire({
            icon: 'error',
            title: 'Oopss...',
            text: 'Select an  address form the address box!',



        })
    }
    else {
        var data = {
            'address': selectedAddressId,
            'total': total_price,
            'order_total': GrandTotal,
            'payment_method': payment_method,
            'discount_price': discount,
            'tax': tax,
        };


        // Get the CSRF token from the form
        var csrfToken = formData1.csrfmiddlewaretoken.value;

        // Include the CSRF token in the headers
        var headers = new Headers({
            'X-CSRFToken': csrfToken
        });

        // Create the request object
        var request = new Request('/order/placeorder/', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data)
        });

        // Send the fetch request
        fetch(request)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                Swal.fire({
                    icon: 'success',
                    title: 'Success...',
                    title: '<span style="font-weight: bold; font-size: 18px;">Thank You for Shopping With Us</span>',
                    html: '<p style="font-size: 16px;">Your Order Number is: <strong>' + data.order_id + '</strong></p>',
                    footer: '<a href="/myorder/" style="font-size: 14px;">Go to My Orders</a>',
                }) // Handle the response data
                setTimeout(() => {
                    window.location.href = '/myorder/'
                }, 2000);
            })
            .catch(error => {
                console.error('Fetch error:', error);
            });

    }


}


$(document).ready(function () {

    $('.payonline').click(function (e) {
        e.preventDefault();




        if (!selectedAddressId) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'All fields are madaratory!',
                footer: '<a href="">Why do I have this issue?</a>'
            })
        }
        else {
            var formData = new FormData(document.getElementById('addressForm'));
            var first_name = addressDetailsFromFirstAjax.first_name;
            var last_name = addressDetailsFromFirstAjax.last_name;
            var phonenumber = addressDetailsFromFirstAjax.phonenumber;
            var town = addressDetailsFromFirstAjax.town;
            var address = addressDetailsFromFirstAjax.address;
            var district = addressDetailsFromFirstAjax.district;
            var zip_code = addressDetailsFromFirstAjax.zip_code;
            var nearbylocation = addressDetailsFromFirstAjax.nearbylocation;
            $.ajax({
                url: '/order/proceed-to-pay/', // Replace with your backend endpoint
                method: 'POST',
                data: formData,
                processData: false, // Prevent jQuery from processing the data
                contentType: false,
                success: function (response) {

                    console.log(response)

                    // Data for setting the order

                    var total_price = response.total_price
                    var GrandTotal = response.GrandTotal
                    var discount_price = response.discount_price
                    var tax = response.tax
                    var payement_method = response.payment_method
                    var token = $("[name='csrfmiddlewaretoken']").val()
                    console.log(payement_method)


                    var options = {
                        "key": "rzp_test_RyZUgsGPNnwtiQ", // Enter the Key ID generated from the Dashboard
                        "amount": response.GrandTotal * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Ntk Online Shopping ", //your business name
                        "description": "Thanku for Choosing us , Have a Great Day",
                        "image": "https://t3.ftcdn.net/jpg/05/29/41/96/360_F_529419639_eFk62uXuzFexGwZR5Xi6zYwiAQvaxSjM.jpg",
                        //"order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response) {
                            //alert(response.razorpay_payment_id);
                            data = {
                                "address": selectedAddressId,
                                "total_price": total_price,
                                "GrandTotal": GrandTotal,
                                "discount_price": discount_price,
                                "tax": tax,
                                "payment-method": payement_method,
                                csrfmiddlewaretoken: token
                            }
                            $.ajax({
                                method: 'POST',  // Corrected method definition
                                url: "/order/placeorder_online/",
                                data: data,
                                success: function (responseB) {

                                    Swal.fire({
                                        position: 'center',
                                        icon: 'success',
                                        title: '<span style="font-weight: bold; font-size: 18px;">Thank You for Shopping With Us</span>',
                                        html: '<p style="font-size: 16px;">Your Order Number is: <strong>' + responseB.order_id + '</strong></p>',
                                        footer: '<a href="/myorder/" style="font-size: 14px;">Go to My Orders</a>',
                                        showConfirmButton: false,
                                        width: '50%',
                                    });
                                    console.log(formData)
                                    var form = document.getElementById('addressForm')
                                    form.reset()
                                    setTimeout(() => {
                                        window.location.href = '/myorder/'
                                    }, 2000);
                                    window.reload()

                                    // Handle the success of the AJAX request here
                                },
                                // You can also handle error and other events as needed
                            });

                        },
                        "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                            "name": first_name + " " + last_name, //your customer's name
                            "email": "None",
                            "contact": phonenumber  //Provide the customer's phone number for better conversion rates 
                        },
                        "notes": {
                            "address": "Ntk Online Shopping Co.Ltd"
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.on('payment.failed', function (response) {
                        alert(response.error.code);
                        alert(response.error.description);
                        alert(response.error.source);
                        alert(response.error.step);
                        alert(response.error.reason);
                        alert(response.error.metadata.order_id);
                        alert(response.error.metadata.payment_id);
                    });

                    rzp1.open();


                },
                error: function (xhr, status, error) {
                    console.error(error);
                }

            });


        }




    });
});