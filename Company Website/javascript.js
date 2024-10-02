document.addEventListener('DOMContentLoaded', function() {
    console.log('Page loaded successfully!');

    // Function to handle responsive navigation
    function handleResponsiveNav() {
        const nav = document.querySelector('nav ul');
        const navItems = nav.querySelectorAll('li');

        // Check the viewport width
        if (window.innerWidth <= 768) {
            // Hide navigation items on smaller screens
            navItems.forEach(item => {
                item.style.display = 'none';
            });

            // Add a toggle button for mobile navigation
            const toggleButton = document.createElement('button');
            toggleButton.innerText = 'Menu';
            toggleButton.style.display = 'block';
            toggleButton.style.margin = '10px auto';
            toggleButton.style.padding = '10px';
            toggleButton.style.backgroundColor = '#379';
            toggleButton.style.color = 'white';
            toggleButton.style.border = 'none';
            toggleButton.style.borderRadius = '4px';
            toggleButton.style.cursor = 'pointer';

            toggleButton.addEventListener('click', function() {
                navItems.forEach(item => {
                    item.style.display = item.style.display === 'none' ? 'block' : 'none';
                });
            });

            nav.parentNode.insertBefore(toggleButton, nav);
        } else {
            // Show navigation items on larger screens
            navItems.forEach(item => {
                item.style.display = 'inline';
            });

            // Remove the toggle button if it exists
            const toggleButton = document.querySelector('nav button');
            if (toggleButton) {
                toggleButton.remove();
            }
        }
    }

    // Initial call to handle responsive navigation
    handleResponsiveNav();

    // Add event listener for window resize
    window.addEventListener('resize', handleResponsiveNav);

    // Form validation for Contact Us form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !message) {
                event.preventDefault();
                alert('Please fill out all fields before submitting.');
            }
        });
    }

    // Form validation for Job Application form
    const jobApplicationForm = document.getElementById('jobApplicationForm');
    if (jobApplicationForm) {
        jobApplicationForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const position = document.getElementById('position').value;
            const resume = document.getElementById('resume').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !phone || !position || !resume || !message) {
                event.preventDefault();
                alert('Please fill out all fields before submitting.');
            }
        });
    }
});
