let button = document.querySelector('.filter-container2');
    window.onscroll = function() {
     if (window.pageYOffset > 84) {
         button.classList.add("test");
     }  else if (window.pageYOffset <= 84){
      button.classList.remove("test");
     }
 }