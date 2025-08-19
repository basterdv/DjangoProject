if ('VKIDSDK' in window) {
    const VKID = window.VKIDSDK;

    const vkidOnSuccess =

    VKID.Config.init({
        app: 54015625,
        redirectUrl: 'http://localhost/users/login',
        responseMode: VKID.ConfigResponseMode.Callback,
        source: VKID.ConfigSource.LOWCODE,
        mode: VKID.ConfigAuthMode.InNewWindow,
        scope: 'email', // Заполните нужными доступами по необходимости
    });

    const oneTap = new VKID.OneTap();

    oneTap.render({
        container: document.currentScript.parentElement,
        showAlternativeLogin: true,
        oauthList: [
            'ok_ru',
            'mail_ru'
        ]
    })
        .on(VKID.WidgetEvents.ERROR, vkidOnError)
        .on(VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload) {
            const code = payload.code;
            const deviceId = payload.device_id;

            VKID.Auth.exchangeCode(code, deviceId)
                .then(vkidOnSuccess)
                .catch(vkidOnError);
        });
}


///////////////////////////////////

// function printDiv(divId) {
//     let divContents = document.getElementById(divId).innerHTML;
//     let printWindow = window.open('', '', 'height=500,width=800');
//     printWindow.document.write('<html><head><title>Print Div Content</title>');
//     // Optional: Add specific styles for printing
//     printWindow.document.write('<style>body { font-family: Arial, sans-serif; }</style>');
//     printWindow.document.write('</head><body>');
//     printWindow.document.write(divContents);
//     printWindow.document.write('</body></html>');
//     printWindow.document.close();
//     printWindow.focus(); // Necessary for some browsers like IE >= 10
//     // printWindow.print();
//     // printWindow.close();
// }


// Создание экземпляра кнопки.
// const oneTap = new VKID.OneTap();

// Получение контейнера из разметки.
// const container = document.getElementById('VkIdSdkOneTap');
// const container = document.getElementById('VKIDSDKAuthButton');
//
// // handleError — какой-либо обработчик ошибки.
// function handleError() {
//     document.addEventListener("DOMContentLoaded", function () {
//         var myModal = new bootstrap.Modal(document.getElementById("errorModal"));
//         myModal.show();
//     });
// }
//
// // Проверка наличия кнопки в разметке.
// // if (container) {
// //     // Отрисовка кнопки в контейнере с именем приложения APP_NAME, светлой темой и на русском языке.
// //     oneTap.render({container: container, scheme: VKID.Scheme.LIGHT, lang: VKID.Languages.RUS})
// //         .on(VKID.WidgetEvents.ERROR, handleError)
// //         .on(VKID.OneTapInternalEvents.LOGIN_SUCCESS); // handleError — какой-либо обработчик ошибки.
// // }
//
// function onErrorHandler() {
//     alert('Вы нажали кнопку ОШИБКА')
// }
//
//
// //настройки обработчика успешной авторизации
// // oneTap.on(VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload) {
// //     const code = payload.code;
// //     const deviceId = payload.device_id;
// //
// //     VKID.Auth.exchangeCode(code, deviceId)
// //         .then(onSuccessHandler)
// //         .catch(onErrorHandler);
// // });
//
// // VKID.config.set({
// // //     В метод передать данные
// //     app: 54015625, // ID Приложения
// //     redirectUrl: 'http://localhost/users/login',
// //     responseMode: VKID.ConfigResponseMode.Callback,
// //     source: VKID.ConfigSource.LOWCODE,
// //     scope: '', // Заполните нужными доступами по необходимости
// // });
// //
// //
// // Создание экземпляра кнопки.
// // const oneTap = new VKID.OneTap();
// //
// // // Получение контейнера из разметки.
// // const container = document.getElementById('VKIDSDKAuthButton');
//
// // Проверка наличия кнопки в разметке.
// // if (container) {
// //     // Отрисовка кнопки в контейнере с именем приложения APP_NAME, светлой темой и на русском языке.
// //     oneTap.render({container: container, scheme: VKID.Scheme.LIGHT, lang: VKID.Languages.RUS})
// //         .on(VKID.WidgetEvents.ERROR, handleError); // handleError — какой-либо обработчик ошибки.
// // }
//
// // const VKID = window.VKIDSDK;
//
//
// // Обработчик клика.
// const handleClick = () => {
//
//     // alert('Вы нажали кнопку РАЗРЕШИТЬ')
//     document.getElementById('printable_area').innerHTML = 'kkkkkkkkkkkkkkk'
//
// //     function handleCallbackAuth() {
// //         // Пользователь нажал на кнопку РАЗРЕШИТЬ
// //         alert('Вы нажали кнопку РАЗРЕШИТЬ')
// //         window.location.close()
// //         VKID.Auth.login().close()
// //     }
// //
//     // Открытие авторизации.
//     // VKID.Auth.login().then(VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload) {
//     //     const code = payload.code;
//     //     const deviceId = payload.device_id;
//     //
//     //     VKID.Auth.exchangeCode(code, deviceId)
//     //         .then(onSuccessHandler)
//     //         .catch(onErrorHandler);
//     // });
//     // window.close()
//     // VKID.close()
//     //
//     // function onSuccessHandler() {
//     //     alert('Вы нажали кнопку РАЗРЕШИТЬ')
//     //     document.getElementById('printable_area').innerHTML = 'ffffffffffffffffff'
//     //
//     // }
//
//     VKID.Auth.login(function (response) {
//         __authInfo(response);
//     });
// }
//
// function __authInfo(response) {
//     if (response.session) {
//         // Пользователь нажал на кнопку РАЗРЕШИТЬ
//         document.getElementById('printable_area').innerHTML = 'ffffffffffffffffff'
//         alert('Вы нажали кнопку РАЗРЕШИТЬ')
//         closeLoginWindow()
//     } else {
//         // Пользователь нажал кнопку Отмена в окне авторизации
//         alert('вы нажали кнопку ОТМЕНА');
//     }
// }
//
// // Получение кнопки из разметки.
// const button = document.getElementById('VKIDSDKAuthButton');
//
// // Проверка наличия кнопки в разметке.
// if (button) {
//     // Добавление обработчика клика по кнопке.
//     button.onclick = handleClick;
// }
//
// function printDiv() {
//     document.getElementById('printable_area').innerHTML = 'ffffffffffffffffff'
// }
//
// function closeLoginWindow() {
//     window.close();
// }
//
//
// // Получаем глобальный объект VK ID
// const VKID = window.VKIDSDK;
//
// // Настройка SDK
// VKID.Config.init({
//     app: 54015625, // Идентификатор приложения.
//     redirectUrl: 'http://localhost/users/login', // Адрес для перехода после авторизации.
//     responseMode: VKID.ConfigResponseMode.Callback,
//     // state: '<случайно сгенерированный state>', // Произвольная строка состояния приложения.
//     // codeVerifier: '<ваш сгенерированный code_verifier>', // Параметр в виде случайной строки. Обеспечивает защиту передаваемых данных.
//     scope: 'email phone', // Список прав доступа, которые нужны приложению.
//     mode: VKID.ConfigAuthMode.InNewWindow,
// });
//
// const renderUserInfo = (user) => {
//     const userInfoBlock = document.getElementById('userInfo');
//     userInfoBlock.innerText = `
//         Email: ${user.email}
//         Телефон: ${user.phone.substring(0, 5)}*****
//            `
// }
//
// // Имя: ${user.first_name}
// // Фамилия: ${user.last_name}
//
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
// const renderLogoutButton = (token) => {
//     const logoutButton = document.getElementById('logoutButton');
//     logoutButton.innerText = 'Выйти';
//     logoutButton.style.display = 'block';
//     logoutButton.onclick = () => {
//         VKID.Auth.logout(token);
//         window.location.reload();
//     }
// }
//
// const renderLoginButton = () => {
//     const buttonConteiner = document.getElementById('VkAuthButton');
//     const oneTap = new VKID.oneTap();
// }
