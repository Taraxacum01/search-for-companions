(function () {
  function sticky(selector) {
    var $elem = document.querySelector(selector);
    var $clone = $elem.cloneNode(true);
    var added = false;
    var pos = topDistance($elem);

    $clone.classList.add("sticky");

    window.addEventListener("scroll", function (e) {
      if (window.scrollY > pos) {
        document.body.appendChild($clone);
        added = true;
      } else if (added) {
        document.body.removeChild($clone);
        added = false;
      }
    });

    function topDistance(element, distance) {
      distance = distance || 0;
      if (!element) return distance;

      distance += element.offsetTop;

      return topDistance(element.offsetParent, distance);
    }
  }

  sticky(".filter");
})();
