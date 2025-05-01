const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const navItems = document.querySelectorAll('.nav-links li');

hamburger.addEventListener('click', () => {
    // Toggle nav
    navLinks.classList.toggle('nav-active');
    
    // Animate links
    navItems.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = '';
        } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
        }
    });
    
    // Hamburger animation
    hamburger.classList.toggle('toggle');
});

// Close mobile menu when clicking on a link
navItems.forEach(item => {
    item.addEventListener('click', () => {
        if (window.innerWidth <= 1024) {
            navLinks.classList.remove('nav-active');
            hamburger.classList.remove('toggle');
            navItems.forEach(link => {
                link.style.animation = '';
            });
        }
    });
});

// Button click handlers
document.querySelector('.login-btn').addEventListener('click', () => {
    alert('Login button clicked!');
    // Add your login functionality here
});

document.querySelector('.signup-btn').addEventListener('click', () => {
    alert('Sign Up button clicked!');
    // Add your signup functionality here
});

document.querySelector('.donate-btn').addEventListener('click', () => {
    alert('Donate button clicked!');
    // Add your donation functionality here
});