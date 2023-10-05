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

          // Handle the response data here
          console.log(responseData.varient_color);
          console.log(responseData.varient_price);
          console.log(responseData.varient_size);
          console.log(responseData.varient_stock);
          var varient_color = responseData.varient_color;
          let varient_price = responseData.varient_price;
          let varient_size = responseData.varient_size;
          let varient_stock = responseData.varient_stock;

          
          const varientPriceContainer = document.getElementById('price');
          price.textContent = responseData.varient_price;

         //tStockContainer.textContent = responseData.varient_stock;

          const imagesData = responseData.image_urls; // Assuming image_urls is an array in the response

          // Check if there are images in the response
          if (imagesData && imagesData.length > 0) {
              const imagesContainer = document.getElementById('images-container');
              imagesContainer.innerHTML = ''; // Clear any previous content

              const firstImageContainer = document.getElementById('first-image-container');
              firstImageContainer.innerHTML = ''; // Clear any previous content


              const price = document.getElementById('price');
              price.innerHTML = '';

              // Loop through the image data and create image elements
              for (const imageUrl of imagesData) { // Assuming imagesData is an array of image URLs
                  // Create an image element
                  const img = document.createElement('img');
                  img.src = imageUrl; // Use imageUrl from the array
                  img.alt = ''; // You can set alt text as needed

                  // Append the image to the container
                  imagesContainer.appendChild(img);

                  // Append the first image to the first-image-container
                  if (imagesData.indexOf(imageUrl) === 0) {
                      const firstImg = img.cloneNode(true);
                      firstImageContainer.appendChild(firstImg);
                  }
              }
          } else {
              // Handle the case where there are no images in the response
              const noImagesMessage = document.createElement('p');
              noImagesMessage.textContent = 'No images found.';
              document.getElementById('images-container').appendChild(noImagesMessage);
              document.getElementById('first-image-container').appendChild(noImagesMessage.cloneNode(true));
          }

          //window.location.href = `/products/filter/${varient_color}`;
      })
      .catch(error => {
          console.error('Error sending data:', error);
      });
}