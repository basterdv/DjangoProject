// Simple JS for interactive elements
document.addEventListener('DOMContentLoaded', function () {
    // Favorite buttons functionality
    const favoriteButtons = document.querySelectorAll('.fa-heart');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function () {
            if (this.classList.contains('far')) {
                this.classList.remove('far');
                this.classList.add('fas', 'text-red-500');
            } else {
                this.classList.remove('fas', 'text-red-500');
                this.classList.add('far');
            }
        });
    });

    // Mobile menu toggle would go here
    // const mobileMenuButton = document.querySelector('.fa-bars');
    // const mobileMenu = document.querySelector('.mobile-menu');
    // mobileMenuButton.addEventListener('click', function() {
    //     mobileMenu.classList.toggle('hidden');
    // });
});