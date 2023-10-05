const banner = document.querySelector("#bannerblock");
const selectedImage = document.getElementById('selectedImage');
const imageInput = document.getElementById('imageInput');
const imageLink = document.getElementById('imageLink');
let flag = false;

banner.style.display = "none"; // Hide the bannerblock div

imageInput.addEventListener('change', function (event) {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
        const imageURL = URL.createObjectURL(selectedFile);
        selectedImage.src = imageURL;
        imageLink.value = ''; // Clear the image link input
    } else {
        selectedImage.src = '';
    }
});

imageLink.addEventListener('change', function () {
    const link = imageLink.value;
    selectedImage.src = link;
    imageInput.value = ''; // Clear the file input
});

function showthedivforaddingbaner() {
    console.log('Testing@!!!!!!!!!!!!!!!!!!!')
    if (flag == true) {
        console.log('Function@!!!!!!!!!!!!!!!!!!!', banner)
        banner.style.display = "none"; // Hide the bannerblock div
        flag = false;
    } else {
        console.log('Functio222222n@!!!!!!!!!!!!!!!!!!!', banner)
        banner.style.display = "block"; // Show the bannerblock div
        flag = true;
    }
}