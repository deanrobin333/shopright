
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

// deleting not items
document.querySelectorAll('.delete-item').forEach(button => {
    button.addEventListener('click', async (event) => {
        const cartId = button.getAttribute('data-cart-id');
        const itemId = button.getAttribute('data-item-id');

        // Ensure both IDs are present
        if (cartId && itemId) {
            try {
                const response = await fetch(`/cart/${cartId}/delete`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ item_id: itemId })
                });

                if (response.ok) {
                    // alert('Item deleted from cart.');
                    location.reload(); // Reload the page to reflect changes
                } else {
                    alert('Failed to delete item.');
                }
            } catch (error) {
                console.error('Error deleting item:', error);
                alert('An error occurred.');
            }
        } else {
            console.error('Missing cart or item ID.');
        }
    });
});


// remove flash message after some time
document.addEventListener('DOMContentLoaded', function() {
    // Select the flash message container
    const flashMessage = document.querySelector('#flash-message');
    
    if (flashMessage) {
        // Set a timeout to fade out the alert after 2 seconds
        setTimeout(function() {
            flashMessage.classList.remove('show'); // Removes the "show" class to hide it
            flashMessage.classList.add('fade'); // Adds the "fade" class (Bootstrap behavior)
        }, 3333); // 2000 milliseconds = 2 seconds
    }
});

// set today's date on creating cart
document.addEventListener("DOMContentLoaded", function() {
    const today = new Date().toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
    document.getElementById('date').value = today; // Set the value of the date input
});