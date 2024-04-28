document.addEventListener('DOMContentLoaded', function() {
    var consoleElement = document.getElementById('console');
    var text = "\nVerifying your identity...\nYou are not my master Naup!\nYou are just User...\n> Success!!\n[User@FFAM-000000]Start...\n[User@FFAM-000001]Installing package...\n[User@FFAM-000002]Connect to FFAM system...\n[User@FFAM-000003]All requirement already satisfied \n[User@FFAM-000004]Try to find Flag...\n[User@FFAM-000005]Try to get shell...\n";
    var additionalText = "Error: Insufficient System Memory\nThis operation requires a minimum of 8GB of RAM.\n\nIf you want to use small shell, you can go to /webshell .";
    var index = 0;
    
    function typeWriter(callback) {
      if (index < text.length) {
        consoleElement.innerHTML += text.charAt(index);
        index++;
        setTimeout(function() { typeWriter(callback); }, 50); // 調整數字可以改變打字速度
      } else if (callback) {
        callback();
      }
    }
    
    function displayAdditionalText() {
      var span = document.createElement('span');
      span.className = 'red-text';
      span.textContent = additionalText;
      consoleElement.appendChild(span);
    }
    
    typeWriter(displayAdditionalText);
    
  });