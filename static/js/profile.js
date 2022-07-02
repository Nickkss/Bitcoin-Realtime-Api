function showHide(target) {
    let auth_token = document.getElementById("auth_token");
    if (auth_token.type == 'password') {
        auth_token.type = 'text';
        target.innerHTML = `<i class="fa-solid fa-eye-slash fa-fw"></i>`;
    } else {
        auth_token.type = 'password';
        target.innerHTML = `<i class="fa-solid fa-eye fa-fw"></i>`;
    }
}


function copyAuthToken() {
    let auth_token = document.getElementById("auth_token");

    auth_token.select();
    auth_token.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(auth_token.value);

    showPopup('primary', "Token copied to clipboard !")

}

const refresh_auth_token_form = document.getElementById("refresh_auth_token_form");

refresh_auth_token_form.addEventListener('submit', (event) => {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure?',
        text: "Do you want to change Auth Token.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, Change it!'
    }).then((result) => {
        if (result.isConfirmed) {
            refresh_auth_token_form.submit()
        }
    })
})