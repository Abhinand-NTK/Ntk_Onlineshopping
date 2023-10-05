function toggleField() {
    var field = document.getElementById('field');
    var button = document.getElementById('toggleButton');
    
    if (field.value === 'true') {
        field.value = 'false';
        button.className = 'red-button';
    } else {
        field.value = 'true';
        button.className = 'green-button';
    }
}