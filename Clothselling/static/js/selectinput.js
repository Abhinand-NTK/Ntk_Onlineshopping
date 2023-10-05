
    const categoryDropdown = document.getElementById('categoryDropdown');
    const newSubCategoryInput = document.getElementById('newSubCategory');

    categoryDropdown.addEventListener('change', function() {
        const selectedOption = categoryDropdown.options[categoryDropdown.selectedIndex];
        newSubCategoryInput.value = selectedOption.text;
    });
    // const categoryDropdown1 = document.getElementById('categoryDropdown1');
    // const newSubCategoryInput1 = document.getElementById('newSubCategory1');

    // categoryDropdown.addEventListener('change', function() {
    //     const selectedOption = categoryDropdown.options[categoryDropdown.selectedIndex];
    //     newSubCategoryInput.value = selectedOption.text;
    // });
    const categoryDropdown1 = document.getElementById('categoryDropdown1');
    const newSubCategoryInput1 = document.getElementById('newSubCategory1');

    categoryDropdown1.addEventListener('change', function() {
        const selectedOption = categoryDropdown1.options[categoryDropdown1.selectedIndex];
        newSubCategoryInput1.value = selectedOption.text;
});
