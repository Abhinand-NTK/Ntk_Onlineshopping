// JavaScript to show/hide max discount field based on the selected discount type
const discountTypeSelect = document.getElementById('discount_type');
const discountAmountField = document.getElementById('discount_amount_field');
const discountPercentageField = document.getElementById('discount_percentage_field');
const maxDiscountAmountField = document.getElementById('max_discount_amount_field');

discountTypeSelect.addEventListener('change', function () {
    if (this.value === 'amount') {
        discountAmountField.style.display = 'block';
        discountPercentageField.style.display = 'none';
        maxDiscountAmountField.style.display = 'none';
    } else if (this.value === 'percentage') {
        discountAmountField.style.display = 'none';
        discountPercentageField.style.display = 'block';
        maxDiscountAmountField.style.display = 'block';
    } else {
        discountAmountField.style.display = 'none';
        discountPercentageField.style.display = 'none';
        maxDiscountAmountField.style.display = 'none';
    }
});