delete_id=document.getElementById('delete_');
console.log(delete_id.value)
function delete_wishlist(){
    fetch(`/deletewish/${delete_id.value}`,{

    })    
}



$(document).ready(function () {
    $(".alert").slideDown(400).delay(3000).slideUp(400);
});