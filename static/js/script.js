/* ================================ Index Page =====================================  */
document.addEventListener("DOMContentLoaded", function () {
  const loginIcon = document.getElementById("loginIcon");
  const referralIcon = document.getElementById("referralIcon");

  if (loginIcon) {
    loginIcon.addEventListener("click", function (){
      alert("Login modal will open here");
    });
  }

  if (referralIcon) {
    referralIcon.addEventListener("click", function (){
      alert("XXXX XXXX (login required)");
    });
  }
})

/* ================================ Course Modal =====================================  */
var courseModal = document.getElementById('courseModal')
courseModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget
    var title = button.getAttribute('data-title')
    var content = button.getAttribute('data-content')

    courseModal.querySelector('.modal-title').textContent = title
    courseModal.querySelector('.modal-body').innerHTML = `<p>${content}</p>`
})


/* ================================ Text Rotator =====================================  */
const texts = [
  "Whatever your demand,<br>you get on <span>Begin2Code</span>."
];

let i = 0;
const el = document.getElementById("mainText");

setInterval(() => {
    el.style.opacity = 0;
    setTimeout(() => {
        i = (i + 1) % texts.length;
        el.innerHTML = texts[i];
        el.style.opacity = 1;
    }, 500);
}, 4000);




