document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if(menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Cookie consent
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesBtn = document.getElementById('accept-cookies');
    
    if(cookieBanner && acceptCookiesBtn) {
        if(!localStorage.getItem('cookies_accepted')) {
            cookieBanner.classList.add('show');
        }
        
        acceptCookiesBtn.addEventListener('click', () => {
            localStorage.setItem('cookies_accepted', 'true');
            cookieBanner.classList.remove('show');
        });
    }
});
