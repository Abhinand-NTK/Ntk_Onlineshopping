
      $(document).ready(function() {
        // Show the "Add Color" modal when the corresponding button is clicked
        $('#showColorModalBtn').click(function() {
            $('#colorModal').modal('show');
        });
    
        // Show the "Add Size" modal when the corresponding button is clicked
        $('#showSizeModalBtn').click(function() {
            $('#sizeModal').modal('show');
        });
        
        $('#showBrandModalBtn').click(function() {
          $('#brandModal').modal('show');
         });

        //  $('#editProductModal').click(function() {
        //   $('#brandModal').modal('show');
        //  });



     


        $(document).ready(function() {
            $('.edit-button').click(function() {
              var modalId = $(this).data('bs-target'); // Get the modal ID from data-bs-target
              $(modalId).modal('show');
            });
          });
    });