
$(document).ready(function () {
  // On page load, check local storage for the theme
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme) {
      $("html").attr("data-bs-theme", savedTheme); // Apply saved theme
      $(".dark").text(`Activate ${savedTheme === "dark" ? "light" : "dark"} Mode`);
  }

  // Toggle theme on button click
  $(".dark").click(function () {
      const currentTheme = $("html").attr("data-bs-theme");
      if (currentTheme === "dark") {
          $("html").attr("data-bs-theme", "light"); // Switch to light mode
          localStorage.setItem("theme", "light"); // Save to local storage
      } else {
          $("html").attr("data-bs-theme", "dark"); // Switch to dark mode
          localStorage.setItem("theme", "dark"); // Save to local storage
      }
      $(".dark").text(`Activate ${currentTheme} Mode`);
  });
});
