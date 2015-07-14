var totop     = undefined,
    height    = 100,
    dx        = 0,
    docBody   = document.documentElement || document.body.parentNode || document.body,
    hasOffset = window.pageYOffset !== undefined,
    offset    = height,
    scrollTop = oldScrollTop = hasOffset ? window.pageYOffset : docBody.scrollTop,
    scrollBot = 0,
    max       = 0,
    min       = 0;

window.onload = function(e) {
  totop = document.getElementById("to-top");
  totop.style.bottom = "-"+offset+"px";

  var link = document.getElementById("menu-link");
  var menu = document.getElementById("menu");
  var container = document.getElementById("container");
  menu.id = "js-menu";
  menu.className = "hidden";
  container.className = "js-menu";
  link.onclick = function () {
    if (menu.className == "hidden") {
      link.className = "open";
      menu.className = "visible";
    } else {
      menu.className = "hidden";
      link.className = "";
    }
    return false;
  }
}

window.onscroll = function (e) {
  // cross-browser compatible scrollTop.
  scrollTop = hasOffset ? window.pageYOffset : docBody.scrollTop;
  dx = scrollTop - oldScrollTop;
  var scrollBot = document.body.offsetHeight - scrollTop - window.innerHeight;

  offset = offset + dx
  if (scrollBot < height) { max = scrollBot; } else { max = height; }
  if (scrollTop < height) { min = height - scrollTop; } else { min = 0; }
  if (offset > max) { offset = max; }
  if (offset < min) { offset = min; }

  if (totop) {
    totop.style.bottom = "-"+offset+"px";
  }

  oldScrollTop = scrollTop;
}
