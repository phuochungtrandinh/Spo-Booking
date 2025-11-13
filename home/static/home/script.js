document.addEventListener("DOMContentLoaded", function() {
  const avatar = document.getElementById("avatarIcon");
  const dropdown = document.getElementById("userDropdown");

  if (avatar && dropdown) {
    avatar.addEventListener("click", function() {
      dropdown.classList.toggle("show");
    });
  }
});
