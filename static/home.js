/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}
const showpop = (n) => {
  document.getElementById(n).style.display="flex";
  var ele=document.getElementById("inputContainer");
  ele.scrollIntoView();
}
const hidepop = (n) => {
  document.getElementById(n).style.display="none";
}
const shownav = () => {
  document.getElementById("rightnav").classList.toggle('active');
  document.getElementById("mobilenav").classList.toggle('active');
}