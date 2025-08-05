document.addEventListener('DOMContentLoaded', function () {
    // Favorite buttons functionality
    const favoriteButtons = document.querySelectorAll('.fa-heart');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function () {
            if (this.classList.contains('far')) {
                this.classList.remove('far');
                this.classList.add('fas', 'text-danger');
            } else {
                this.classList.remove('fas', 'text-danger');
                this.classList.add('far');
            }
        });
    });

    // Smooth scroll for navbar links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const navbarHeight = document.querySelector('.fixed-navbar').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});