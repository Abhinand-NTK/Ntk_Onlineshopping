function Wishlist(id) {

    const button = document.querySelector('button[data-bs-toggle="popover"]');
    const colorchange_Accoding_wishlist = document.getElementById('colorchange');
    console.log(colorchange_Accoding_wishlist);



    $('[data-bs-toggle="popover"]').popover()

    console.log(id)
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const headers = new Headers({
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    });
    // Create the fetch request
    fetch(`/mywishlist/${id}`, {
        method: 'POST',
        headers: headers,
    })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {


            console.log(data.message)

            if (data.message == 'The item is added to the Wishlist') {
                colorchange_Accoding_wishlist.style.color = '#ff0000';

            }
            else {

                colorchange_Accoding_wishlist.style.color = '#000';
            }



            button.setAttribute('data-bs-content', '')
            button.setAttribute('data-bs-content', data.message);

            const popover = new bootstrap.Popover(button);

            // Show the popover
            popover.show();

            // Automatically hide the popover after 10 seconds
            setTimeout(function () {
                popover.hide();
            }, 1000);

            console.log(data); // Now you can access the parsed response data
        })
        .catch(error => {
            console.error(error); // Handle any errors that occur during the fetch
        });

}



let varientId;

var myResult = document.getElementById("myresult");
myResult.style.display = "none";

const hide_review_box = document.getElementById('ratingwindow1112');

hide_review_box.style.display = 'none'


function ready(variant_id, color) {
    console.log(variant_id);
    console.log(color);

    const data = {
        variant_id: variant_id,
        color: color,
    };

    // Get the CSRF token from the form
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Create headers with the CSRF token
    const headers = new Headers({
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    });

    // Create the fetch request
    fetch('/products/filtering_varient/', {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`);
            }
            return response.json();
        })
        .then(responseData => {
            console.log('Response:', responseData);


            var varient_color = responseData.varient_color;
            let varient_price = responseData.varient_price;
            let varient_size = responseData.varient_size;
            let varient_stock = responseData.varient_stock;
            varientId = responseData.varient_id;
            const varientIdInput = document.getElementById('varient_id');
            varientIdInput.value = varientId;
            //hide_review_box.style.display = 'block'



            raritng_box = JSON.parse(document.getElementById('rating_data').value)
            raritng_box1 = JSON.parse(document.getElementById('order_list_id').value)





            // JSON.parse(document.getElementById('monthly_sales').value);


            for (let i = 0; i < raritng_box1.length; i++) {


                if (raritng_box1[i] == variant_id) {

                    hide_review_box.style.display = 'block'

                }

            }

            for (let i = 0; i < raritng_box.length; i++) {


                if (raritng_box[i] == variant_id) {

                    hide_review_box.style.display = 'none'

                }

            }

            const cartForm = document.getElementById('cartForm');
            cartForm.action = `/cart/addtocart/${varientId}`;


            const varientPriceContainer = document.getElementById('price');
            price.textContent = responseData.varient_price;

            const varientPriceContainer_1 = document.getElementById('productname');
            price.textContent = responseData.varient_price;

            

            //tStockContainer.textContent = responseData.varient_stock;

            const imagesData = responseData.image_urls; // Assuming image_urls is an array in the response

            // Check if there are images in the response
            if (imagesData && imagesData.length > 0) {

                const imagesContainer = document.getElementsByClassName('imagetochange');
                console.log(imagesContainer)
                for (let i = imagesData.length; i < imagesContainer.length; i++) {
                    imagesContainer[i].style.display = 'none'; // Clear any previous content
                }

                for (let i = imagesContainer.length; i < imagesContainer.length; i++) {
                    imagesContainer[i].style.display = 'none'; // Clear any previous content
                }




                //const imagesContainer = document.getElementById('left-{{ forloop.counter }}');
                // imagesContainer.innerHTML = ''; // Clear any previous content

                const firstImageContainer = document.getElementById('myimage');
                //firstImageContainer.innerHTML = ''; // Clear any previous content


                const price = document.getElementById('price');
                price.innerHTML = `₹${varient_price}`;
                let i = 0;

                // Loop through the image data and create image elements
                for (const imageUrl of imagesData) { // Assuming imagesData is an array of image URLs
                    // Create an image element
                    const img = document.createElement('img');

                    img.src = imageUrl; // Use imageUrl from the array
                    img.alt = ''; // You can set alt text as needed

                    // Append the image to the container
                    //imagesContainer.appendChild(img);

                    imagesContainer[i].src = imageUrl;


                    console.log(imagesData)

                    // Append the first image to the first-image-container
                    if (imagesData.indexOf(imageUrl) === 0) {
                        const firstImg = img.cloneNode(true);

                        console.log(firstImg)
                        //firstImageContainer.appendChild(firstImg);


                        firstImageContainer.src = firstImg.src;

                    }
                    i = i + 1;
                }
            } else {
                // Handle the case where there are no images in the response
                const noImagesMessage = document.createElement('p');
                noImagesMessage.textContent = 'No images found.';
                //document.getElementById('images-container').appendChild(noImagesMessage);
                document.getElementById('myimage').appendChild(noImagesMessage.cloneNode(true));
            }

            //window.location.href = `/products/filter/${varient_color}`;
        })
        .catch(error => {
            console.error('Error sending data:', error);
        });
}


img = document.getElementById('myimage');

function leftright(id) {
    console.log("Id is :-", id)
    const left = document.getElementById(id);

    let temp = left.src
    left.src = img.src
    img.src = temp

}


const imageContainer = document.querySelector('.image-container');
const imageZoom = document.getElementById('myimage');
const zoomLens = document.getElementById('zoom-lens');

imageContainer.addEventListener('mousemove', moveLens);
imageContainer.addEventListener('mouseenter', showLens);
imageContainer.addEventListener('mouseleave', hideLens);

function showLens(event) {
    zoomLens.style.display = 'block';
}

function hideLens(event) {
    zoomLens.style.display = 'none';
    resetImageZoom();
}

function moveLens(event) {
    const rect = imageContainer.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const lensSize = 100; // Adjust the lens size
    const zoomFactor = 2; // Adjust the zoom level

    // Calculate the background position to achieve the zoom effect
    const bgX = (x / rect.width) * 100;
    const bgY = (y / rect.height) * 100;

    // Set the lens position
    zoomLens.style.left = x - lensSize / 2 + 'px';
    zoomLens.style.top = y - lensSize / 2 + 'px';

    // Update the image transform to achieve the zoom effect
    const zoomedScale = zoomFactor;
    imageZoom.style.transformOrigin = `${bgX}% ${bgY}%`;
    imageZoom.style.transform = `scale(${zoomedScale})`;
}

function resetImageZoom() {
    imageZoom.style.transformOrigin = 'center center';
    imageZoom.style.transform = 'scale(1)';
}






