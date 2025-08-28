// Получаем глобальный объект VK ID
const VKID = window.VKIDSDK;

// Настройка SDK
VKID.Config.init({
    app: 54015625, // Идентификатор приложения.
    redirectUrl: 'http://localhost/users/vk_auth_callback', // Адрес для перехода после авторизации.
    responseMode: VKID.ConfigResponseMode.Callback,
    state: '1WYhJUS_NETi_eUCLGrGPVv5yVY6fYiXVAxrmdVqXfY', // Произвольная строка состояния приложения.
    codeChallenge: 'tLSph3W3GZ8n4YzjVqkgwCmETptZSNXGULm4FkZ4VQ0', // Параметр в виде случайной строки. Обеспечивает защиту передаваемых данных.
    scope: 'email phone first_name last_name', // Список прав доступа, которые нужны приложению.
    mode: VKID.ConfigAuthMode.InNewWindow,
});

const authButton = document.getElementById('VKAuthButton');


authButton.onclick = () => {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    // Запускаем авторизацию
    VKID.Auth.login();
};

function checkTabClosed() {
    if (localStorage.getItem('tabClosed') === 'true') {
        localStorage.removeItem('tabClosed');
        location.reload();  // Обновляем страницу
    }
}

// Проверяем при загрузке страницы
window.addEventListener('load', checkTabClosed);

// Периодически проверяем каждые 1000 мс (1 секунда)
setInterval(checkTabClosed, 1000);



