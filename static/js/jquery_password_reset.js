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
                    // Здесь обычно отправка email
                    console.log('Recovery email sent to:', document.getElementById('recovery-email').value);

                    // Имитация перехода на следующий шаг
                    document.querySelectorAll('.step')[0].classList.remove('active');
                    document.querySelectorAll('.step')[0].classList.add('complete');
                    document.querySelectorAll('.step')[1].classList.add('active');
                    document.querySelector('.progress-bar').style.width = '66%';

                    // Изменение содержимого формы
                    document.querySelector('h2').textContent = 'Создание нового пароля';
                    document.querySelector('p.text-muted').textContent = 'Придумайте надежный пароль для вашего аккаунта';

                    // Замена полей формы
                    const formContent = `
                                <div class="mb-3">
                                    <label for="new-password" class="form-label">Новый пароль</label>
                                    <div class="input-group">
                                        <span class="input-group-text">
                                            <i class="fas fa-lock text-muted"></i>
                                        </span>
                                        <input type="password" class="form-control" id="new-password" placeholder="••••••••" required>
                                        <button class="btn btn-outline-secondary" type="button" id="togglePassword">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <div class="invalid-feedback">
                                            Пожалуйста, придумайте пароль
                                        </div>
                                    </div>
                                    <div class="form-text mt-1">Пароль должен содержать минимум 8 символов</div>
                                </div>

                                <div class="mb-4">
                                    <label for="confirm-password" class="form-label">Подтвердите пароль</label>
                                    <div class="input-group">
                                        <span class="input-group-text">
                                            <i class="fas fa-lock text-muted"></i>
                                        </span>
                                        <input type="password" class="form-control" id="confirm-password" placeholder="••••••••" required>
                                        <button class="btn btn-outline-secondary" type="button" id="toggleConfirmPassword">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <div class="invalid-feedback">
                                            Пароли должны совпадать
                                        </div>
                                    </div>
                                </div>

                                <div class="d-grid gap-2">
                                    <button type="submit" class="btn btn-primary btn-reset mb-3">
                                        <i class="fas fa-save me-2"></i> Сохранить пароль
                                    </button>
                                </div>
                            `;

                    const form = document.querySelector('form');
                    form.innerHTML = formContent;

                    // Добавляем обработчики для новых кнопок
                    document.getElementById('togglePassword')?.addEventListener('click', function () {
                        const password = document.getElementById('new-password');
                        togglePasswordVisibility(password, this);
                    });

                    document.getElementById('toggleConfirmPassword')?.addEventListener('click', function () {
                        const password = document.getElementById('confirm-password');
                        togglePasswordVisibility(password, this);
                    });
                }

                form.classList.add('was-validated');
            }, false);
        });
})();

function togglePasswordVisibility(passwordField, button) {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    const icon = button.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
}
