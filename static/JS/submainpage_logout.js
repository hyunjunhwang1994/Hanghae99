function logout() {


    $.removeCookie('mytoken')

    window.location.href = '/';
}