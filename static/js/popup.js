function showPopup(style, text) {
    let popup_container = document.getElementById("popup_container");
    let popup = document.createElement("div");
    popup.className = `alert alert-${style} alert-dismissible fade show`;
    popup.setAttribute('role', 'alert');
    popup.innerHTML = text;
    popup_container.appendChild(popup)
    setTimeout(function () {
        popup_container.removeChild(popup);
        popup.remove();;
    }, 3000);
}