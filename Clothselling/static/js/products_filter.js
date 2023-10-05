document.addEventListener('DOMContentLoaded', function () {
    const bigImages = document.querySelectorAll('.product__big__img');

    bigImages.forEach(function (bigImage) {
        bigImage.addEventListener('click', function () {
            const imageUrl = bigImage.getAttribute('src');

            const zoomedContainer = document.createElement('div');
            zoomedContainer.className = 'zoomed-image-container';

            const zoomedImage = document.createElement('img');
            zoomedImage.className = 'zoomed-image';
            zoomedImage.setAttribute('src', imageUrl);

            zoomedContainer.appendChild(zoomedImage);
            document.body.appendChild(zoomedContainer);

            zoomedContainer.addEventListener('click', function () {
                document.body.removeChild(zoomedContainer);
            });

            bigImage.classList.toggle('zoomed');
        });
    });
});