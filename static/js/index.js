document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const linkItems = document.querySelectorAll('.nav-links li');

    // Toggle side navigation
    toggleButton.addEventListener('click', () => {
        navLinks.classList.toggle('active');

        // Animate links when menu opens
        if (navLinks.classList.contains('active')) {
            linkItems.forEach((link, index) => {
                link.style.transitionDelay = `${index * 0.05}s`;
                link.style.opacity = '1';
                link.style.transform = 'translateX(0)';
            });
        } else {
            linkItems.forEach((link) => {
                link.style.transitionDelay = '0s';
                link.style.opacity = '0';
                link.style.transform = 'translateX(-20px)';
            });
        }
    });

    // Close nav when a link is clicked
    linkItems.forEach(link => {
        const anchor = link.querySelector('a');
        anchor.addEventListener('click', () => {
            navLinks.classList.remove('active');
            linkItems.forEach((item) => {
                item.style.transitionDelay = '0s';
                item.style.opacity = '0';
                item.style.transform = 'translateX(-20px)';
            });
        });
    });
});