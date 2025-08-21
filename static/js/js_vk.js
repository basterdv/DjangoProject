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
    // После авторизации будет редирект на адрес, указанный в параметре redirectUrl
    VKID.Auth.login();
    window.location.reload();
};



// fetch('http://localhost/users/login', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({}),
// })
//     .catch(console.error)
//     .then((response) => response.json())
//     .then((data) => {
//         localStorage.setItem('access_token', data.access_token);
//         localStorage.setItem('username', data.refresh_token);
//         document.getElementById('printable_area').innerHTML = 'code';
//         window.location.reload();
//
//
//         // //настройки обработчика успешной авторизации
//         // VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload) {
//         //     const code = payload.code;
//         //     const deviceId = payload.device_id;
//         //     document.getElementById('printable_area').innerHTML = code;
//         //`
//         //     VKID.Auth.exchangeCode(code, deviceId)
//         //         .then(onSuccessHandler)
//         //         .catch(onErrorHandler);
//         // };
//
//     });

// };

// const tryAuth = () => {
//     const urlParams = new URLSearchParams(window.location.search);
//     const code = urlParams.get('code');
//     const deviceId = urlParams.get('device_Id');
//     const responseType = urlParams.get('type');
//
//     if (deviceId && responseType === 'code_v2') {
//         VKID.Auth.exchangeCode(code, deviceId)
//             .then((result) => VKID.userInfo(result.access_token))
//     }
// }
//
// // Получение кнопки из разметки.
// const button = document.getElementById('VKAuthButton');
//
// function __authInfo(response) {
//     if (response.session) {
//         // Пользователь нажал на кнопку РАЗРЕШИТЬ
//         document.getElementById('printable_area').innerHTML = 'ffffffffffffffffff'
//         // alert('Вы нажали кнопку РАЗРЕШИТЬ')
//         // closeLoginWindow()
//     } else {
//         // Пользователь нажал кнопку Отмена в окне авторизации
//         alert('вы нажали кнопку ОТМЕНА');
//     }
// }
//
// // Обработчик клика.
// const handleClick = () => {
//
//     VKID.Auth.login(function (response) {
//          tryAuth();
//     });
// }
//
//
// // Проверка наличия кнопки в разметке.
// if (button) {
//     // Добавление обработчика клика по кнопке.
//     button.onclick = handleClick;
// }

