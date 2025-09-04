function mostrarMenu() {
  let menuMobile = document.querySelector(".mobile-menu");
  if (menuMobile.classList.contains("abrir")) {
    menuMobile.classList.remove("abrir");
    document.querySelector(".icone").src = "assets/images/menu_white_36dp.svg";
  } else {
    menuMobile.classList.add("abrir");
    document.querySelector(".icone").src = "assets/images/close_white_36dp.svg";
  }
}
