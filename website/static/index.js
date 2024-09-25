function deleteItem(itemId) {
    fetch("/delete-item", {
      method: "POST",
      body: JSON.stringify({ itemId: itemId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }