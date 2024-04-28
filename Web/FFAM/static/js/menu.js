function validateForm() {
    var USB = document.querySelector('input[name="USB"]').value;
    var Keyboard = document.querySelector('input[name="Keyboard"]').value;
    var RAM = document.querySelector('input[name="RAM"]').value;

    if (USB === "" && Keyboard === "" && RAM === "") {
      alert("請至少選擇一樣商品");
      return false;
    }


    if (USB === "") {
      document.querySelector('input[name="USB"]').value = 0;
    }
    if (Keyboard === "") {
      document.querySelector('input[name="Keyboard"]').value = 0;
    }
    if (RAM === "") {
      document.querySelector('input[name="RAM"]').value = 0;
    }
  }