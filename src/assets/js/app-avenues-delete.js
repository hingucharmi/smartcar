'use strict';

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    const deleteButtons = document.querySelectorAll('.delete-transaction');
    if (deleteButtons.length === 0) {
        console.error('No delete buttons found.');
        return;
      }
    deleteButtons.forEach(deleteButton => {
      deleteButton.addEventListener('click', function (e) {
        e.preventDefault();
        const userName = this.getAttribute('data-transaction-username');
        const deleteUrl = this.getAttribute('href');

        if (!deleteUrl) {
          console.error('Delete URL not found.');
          return;
        }

        Swal.fire({
          title: 'Delete Avenues?',
          html: `<p class="text-danger">Are you sure you want to delete avenues of ?<br> <span class="fw-medium text-body">${userName}</span></p>`,
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Delete',
          cancelButtonText: 'Cancel',
          customClass: {
            confirmButton: 'btn btn-primary waves-effect waves-light',
            cancelButton: 'btn btn-secondary waves-effect waves-light'
          }
        }).then(result => {
          if (result.isConfirmed) {
            window.location.href = this.getAttribute('href'); //redirect to herf
          } else {
            Swal.fire({
              title: 'Cancelled',
              html: `<p>Did not delete <span class="fw-medium text-primary">${userName}</span> Avenues!</p>`,
              icon: 'error',
              confirmButtonText: 'Ok',
              customClass: {
                confirmButton: 'btn btn-success waves-effect waves-light'
              }
            });
          }
        });
      });
    });
  })();
});
