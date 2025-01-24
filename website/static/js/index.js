
$(".dark").click(function () {
    const currentTheme = $("html").attr("data-bs-theme");
    if (currentTheme === "dark") {
        $("html").attr("data-bs-theme", "light"); // Switch to light mode
      } else {
        $("html").attr("data-bs-theme", "dark"); // Switch to dark mode
      }
    $(".dark").text(`Activate ${currentTheme} Mode`);

})