// if ('VKIDSDK' in window
// ) {
//     const VKID = window.VKIDSDK;
//
//     VKID.Config.init({
//         app: 54015625,
//         redirectUrl: 'http://localhost/users/login',
//         responseMode: VKID.ConfigResponseMode.Callback,
//         source: VKID.ConfigSource.LOWCODE,
//         scope: '', // Заполните нужными доступами по необходимости
//     });
//
//     const oneTap = new VKID.OneTap();
//
//     oneTap.render({
//         container: document.currentScript.parentElement,
//         showAlternativeLogin: true,
//         oauthList: [
//             'ok_ru',
//             'mail_ru'
//         ]
//     })
//         .on(VKID.WidgetEvents.ERROR, vkidOnError)
//         .on(VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload) {
//             const code = payload.code;
//             const deviceId = payload.device_id;
//
//             VKID.Auth.exchangeCode(code, deviceId)
//                 .then(vkidOnSuccess)
//                 .catch(vkidOnError);
//         });
//
//     function vkidOnSuccess(data) {
//         // Обработка полученного результата
//     }
//
//     function vkidOnError(error) {
//         // Обработка ошибки
//     }
// }

// Получаем глобальный объект VK ID
const VKID = window.VKIDSDK;

// Настройка SDC
VKID.config.set({
//     В метод передать данные
    app: 54015625, // ID Приложения
    redirectUrl: 'http://localhost/users/login',
    responseMode: VKID.ConfigResponseMode.Callback,
    source: VKID.ConfigSource.LOWCODE,
    scope: '', // Заполните нужными доступами по необходимости
});


// Создание экземпляра кнопки.
const oneTap = new VKID.OneTap();

// Получение контейнера из разметки.
const container = document.getElementById('VkIdSdkOneTap');

// Проверка наличия кнопки в разметке.
if (container) {
    // Отрисовка кнопки в контейнере с именем приложения APP_NAME, светлой темой и на русском языке.
    oneTap.render({container: container, scheme: VKID.Scheme.LIGHT, lang: VKID.Languages.RUS})
        .on(VKID.WidgetEvents.ERROR, handleError); // handleError — какой-либо обработчик ошибки.
}

