const menuButton = document.querySelector('.menu-button');
const sideMenu = document.getElementById('side-menu');
const closeButton = document.querySelector('.close-button');
const overlay = document.getElementById('overlay');

function openMenu() {
    sideMenu.setAttribute('aria-hidden', 'false');
    menuButton.setAttribute('aria-expanded', 'true');
    overlay.classList.add('open');
    document.body.style.overflowY = 'hidden';
}

function closeMenu() {
    sideMenu.setAttribute('aria-hidden', 'true');
    menuButton.setAttribute('aria-expanded', 'false');
    overlay.classList.remove('open');
    document.body.style.overflowY = 'auto';
}

// Event Listeners
menuButton.addEventListener('click', openMenu);
closeButton.addEventListener('click', closeMenu);
overlay.addEventListener('click', closeMenu);

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && sideMenu.getAttribute('aria-hidden') === 'false') {
        closeMenu();
    }
});
