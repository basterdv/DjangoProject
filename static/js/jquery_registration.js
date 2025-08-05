// // Toggle password visibility
// const togglePassword = document.querySelector('#togglePassword');
// const password = document.querySelector('#password');
// const confirmPassword = document.querySelector('#confirm-password');
//
// togglePassword.addEventListener('click', function () {
//     const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
//     password.setAttribute('type', type);
//     this.innerHTML = type === 'password' ? '<i class="fas fa-eye text-gray-400 hover:text-gray-600"></i>' : '<i class="fas fa-eye-slash text-gray-400 hover:text-gray-600"></i>';
// });
//
// // Password strength meter
// password.addEventListener('input', function () {
//     const strengthBar = document.getElementById('passwordStrength');
//     const strength = calculatePasswordStrength(this.value);
//
//     strengthBar.style.width = strength * 25 + '%';
//
//     if (strength < 2) {
//         strengthBar.style.backgroundColor = '#ef4444'; // red
//     } else if (strength < 4) {
//         strengthBar.style.backgroundColor = '#f59e0b'; // yellow
//     } else {
//         strengthBar.style.backgroundColor = '#10b981'; // green
//     }
// });
//
// function calculatePasswordStrength(password) {
//     let strength = 0;
//     if (password.length >= 8) strength++;
//     if (password.match(/[a-z]+/)) strength++;
//     if (password.match(/[A-Z]+/)) strength++;
//     if (password.match(/[0-9]+/)) strength++;
//     if (password.match(/[$@#&!-+]+/)) strength++;
//     return strength;
// }
//
// // Form validation and submission
// document.getElementById('registrationForm').addEventListener('submit', function (e) {
//     e.preventDefault();
//
//     // Check if passwords match
//     if (password.value !== confirmPassword.value) {
//         alert('Пароли не совпадают');
//         return;
//     }
//
//     // Check if terms are accepted
//     if (!document.getElementById('terms').checked) {
//         alert('Пожалуйста, примите условия использования');
//         return;
//     }
//
//     // Here you would normally handle the registration logic
//     console.log('Registration data:', {
//         firstName: document.getElementById('first-name').value,
//         lastName: document.getElementById('last-name').value,
//         email: document.getElementById('email').value,
//         phone: document.getElementById('phone').value,
//         password: document.getElementById('password').value
//     });
//
//     // Redirect after "successful" registration
//     window.location.href = 'profile.html';
// });
//
// // Phone number input mask
// document.getElementById('phone').addEventListener('input', function (e) {
//     let x = this.value.replace(/\D/g, '').match(/(\d{0,1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
//     this.value = !x[2] ? x[1] : x[1] + ' (' + x[2] + (x[3] ? ') ' + x[3] + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '') : '');
// });


// Toggle password visibility
const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
const confirmPassword = document.querySelector('#confirm-password');

togglePassword.addEventListener('click', function () {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
});

// Password strength meter
password.addEventListener('input', function () {
    const strengthBar = document.getElementById('passwordStrength');
    const strength = calculatePasswordStrength(this.value);

    strengthBar.style.width = strength * 25 + '%';

    if (strength < 2) {
        strengthBar.style.backgroundColor = '#dc3545'; // red
    } else if (strength < 4) {
        strengthBar.style.backgroundColor = '#ffc107'; // yellow
    } else {
        strengthBar.style.backgroundColor = '#198754'; // green
    }
});

function calculatePasswordStrength(password) {
    let strength = 0;
    if (password.length >= 8) strength++;
    if (password.match(/[a-z]+/)) strength++;
    if (password.match(/[A-Z]+/)) strength++;
    if (password.match(/[0-9]+/)) strength++;
    if (password.match(/[$@#&!-+]+/)) strength++;
    return strength;
}

// Form validation and submission
document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Check if passwords match
    if (password.value !== confirmPassword.value) {
        alert('Пароли не совпадают');
        return;
    }

    // Check if terms are accepted
    if (!document.getElementById('terms').checked) {
        alert('Пожалуйста, примите условия использования');
        return;
    }

    // Here you would normally handle the registration logic
    console.log('Registration data:', {
        firstName: document.getElementById('first-name').value,
        lastName: document.getElementById('last-name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        password: document.getElementById('password').value
    });

    // Redirect after "successful" registration
    window.location.href = 'profile.html';
});

// Phone number input mask
document.getElementById('phone').addEventListener('input', function (e) {
    let x = this.value.replace(/\D/g, '').match(/(\d{0,1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
    this.value = !x[2] ? x[1] : x[1] + ' (' + x[2] + (x[3] ? ') ' + x[3] + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '') : '');
});
