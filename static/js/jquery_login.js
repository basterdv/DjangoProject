// // Simple JS for interactive elements
//     document.addEventListener('DOMContentLoaded', function () {
//         // Favorite buttons functionality
//         const favoriteButtons = document.querySelectorAll('.fa-heart');
//         favoriteButtons.forEach(button => {
//             button.addEventListener('click', function () {
//                 if (this.classList.contains('far')) {
//                     this.classList.remove('far');
//                     this.classList.add('fas', 'text-red-500');
//                 } else {
//                     this.classList.remove('fas', 'text-red-500');
//                     this.classList.add('far');
//                 }
//             });
//         });
//
//         // Mobile menu toggle would go here
//         // const mobileMenuButton = document.querySelector('.fa-bars');
//         // const mobileMenu = document.querySelector('.mobile-menu');
//         // mobileMenuButton.addEventListener('click', function() {
//         //     mobileMenu.classList.toggle('hidden');
//         // });
//     });


// Форма валидации
(function () {
    'use strict'

    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                } else {
                    event.preventDefault();
                    // Здесь обычно обработка входа
                    console.log('Login attempt with:', {
                        email: document.getElementById('email').value,
                        password: document.getElementById('password').value,
                        remember: document.getElementById('remember-me').checked
                    });
                    // Перенаправление после "успешного" входа
                    window.location.href = 'profile.html';
                }

                form.classList.add('was-validated')
            }, false)
        })
})();

// Переключение видимости пароля
document.getElementById('togglePassword').addEventListener('click', function () {
    const password = document.getElementById('password');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);

    const icon = this.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});
