function resetNavState() {
    document.querySelectorAll('.nav-menu, .dropdown-menu, .dropdown-backdrop, .mobile-menu-toggle').forEach(el => {
        el.classList.remove('active', 'mobile-active', 'expanded');
    });
    document.body.style.overflow = '';
    document.body.style.overflowX = '';
    document.documentElement.style.overflowX = '';
}

// Reset on initial load
document.addEventListener('DOMContentLoaded', resetNavState);

// Also reset when page is restored from bfcache (browser back/forward)
window.addEventListener('pageshow', (e) => {
    if (e.persisted) resetNavState();
});

document.addEventListener('DOMContentLoaded', () => {
    // Dropdown menu functionality
    const programsDropdown = document.querySelector('.programs-dropdown');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const dropdownBackdrop = document.querySelector('.dropdown-backdrop');
    let dropdownTimeout;

    // Show dropdown on hover
    if (programsDropdown && dropdownMenu && dropdownBackdrop) {
        programsDropdown.addEventListener('mouseenter', () => {
            clearTimeout(dropdownTimeout);
            dropdownMenu.classList.add('active');
            dropdownBackdrop.classList.add('active');
        });

        // Keep dropdown open when hovering over the menu
        dropdownMenu.addEventListener('mouseenter', () => {
            clearTimeout(dropdownTimeout);
            dropdownMenu.classList.add('active');
            dropdownBackdrop.classList.add('active');
        });

        // Hide dropdown when leaving the trigger
        programsDropdown.addEventListener('mouseleave', () => {
            dropdownTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('active');
                dropdownBackdrop.classList.remove('active');
            }, 100);
        });

        // Hide dropdown when leaving the menu
        dropdownMenu.addEventListener('mouseleave', () => {
            dropdownTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('active');
                dropdownBackdrop.classList.remove('active');
            }, 100);
        });

        // Hide dropdown when clicking on backdrop
        dropdownBackdrop.addEventListener('click', () => {
            dropdownMenu.classList.remove('active');
            dropdownBackdrop.classList.remove('active');
        });
    }

    // Mobile menu toggle functionality
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');

            // Toggle backdrop for mobile drawer
            if (dropdownBackdrop) {
                dropdownBackdrop.classList.toggle('active');
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !mobileMenuToggle.contains(e.target) && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');

                // Remove backdrop
                if (dropdownBackdrop) {
                    dropdownBackdrop.classList.remove('active');
                }
            }
        });

        // Close menu when clicking backdrop
        if (dropdownBackdrop) {
            dropdownBackdrop.addEventListener('click', () => {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                dropdownBackdrop.classList.remove('active');
            });
        }
    }

    // Mobile Programs Dropdown (inside drawer)
    if (programsDropdown) {
        programsDropdown.addEventListener('click', (e) => {
            // Only handle click on mobile (when drawer is visible)
            if (window.innerWidth <= 800) {
                e.preventDefault();
                e.stopPropagation();

                // Toggle dropdown menu visibility
                if (dropdownMenu) {
                    dropdownMenu.classList.toggle('mobile-active');
                    programsDropdown.classList.toggle('expanded');
                }
            }
        });
    }

    // Header Scroll Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Animated Number Counter for Stats
    function animateValue(obj) {
        const rawValue = obj.getAttribute('data-target') || obj.innerText;
        // Parse value: "10,000+" -> 10000, suffix "+"
        const valueStr = rawValue.replace(/,/g, '');
        const end = parseInt(valueStr);
        const suffix = valueStr.replace(/[0-9]/g, '');

        if (isNaN(end)) return;

        let startTimestamp = null;
        const duration = 2000;

        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            obj.innerHTML = Math.floor(progress * end).toLocaleString() + suffix;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerHTML = rawValue; // Ensure original string formatting
            }
        };
        window.requestAnimationFrame(step);
    }

    // Intersection Observer for Scroll Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px', // Trigger slightly before element enters view
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;

                // Handle Stat Numbers Animation
                const numberEl = target.querySelector('.stat-number');
                if (numberEl && !target.classList.contains('counted')) {
                    animateValue(numberEl);
                    target.classList.add('counted');
                }

                // Handle General Reveal Animations
                target.classList.add('reveal-active');
                target.classList.add('visible');

                // Stop observing once revealed
                observer.unobserve(target);
            }
        });
    }, observerOptions);

    // Observe Elements
    // Select all elements designed to animate
    const animateElements = document.querySelectorAll('.stat-item, .program-card, .role-card, .comparison-card-with-support, .comparison-card-without-support, .reveal-up, .reveal-left, .reveal-right, .reveal-fade');
    animateElements.forEach(el => observer.observe(el));

    // Smooth Scroll for Anchor Links
    // Handle all anchor links that point to page sections (start with #)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');

            // Skip if it's just "#" without a target
            if (targetId === '#' || !targetId) return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                e.preventDefault();

                // Smooth scroll to the target element
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});