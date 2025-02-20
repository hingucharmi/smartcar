// Init cleave on show modal (To fix the cc image issue)
    let addNewCCModal = document.getElementById('addNewCCModal');
    addNewCCModal.addEventListener('show.bs.modal', function (event) {
      initCleave();
    });

    // Expiry Date Mask
    if (expiryDateMask) {
      new Cleave(expiryDateMask, {
        date: true,
        delimiter: '/',
        datePattern: ['m', 'y']
      });
    }

    // CVV
    if (cvvMask) {
      new Cleave(cvvMask, {
        numeral: true,
        numeralPositiveOnly: true
      });
    }