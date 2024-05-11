document.addEventListener("DOMContentLoaded", function () {
  if (document.querySelector(".toast-success")) {
    Toastify({
      text: "The new region added successfully. <a href='{% url 'facility_creation' %}' class='alert-link'>View all facilities.</a>",
      duration: 5000,
      gravity: "top",
      position: "right",
      close: true,
    }).showToast();
  }
});
