// window.onload = function () {
//     window.YaAuthSuggest.init(
//         {
//             client_id: 'b7986b6acead461082b4bbf881148c8f',
//             response_type: 'token',
//             redirect_uri: 'http://localhost/users/yandex_auth_callback'
//         },
//         'http://localhost',
//         {
//             view: "button",
//             parentId: "YaAuthButton",
//             buttonSize: 'm',
//             buttonView: 'main',
//             buttonTheme: 'light',
//             buttonBorderRadius: "22",
//             buttonIcon: 'ya',
//         }
//     )
//         .then(({handler}) => {
//             document.getElementById('YaAuthButton').addEventListener('click', handler);
//         })
//         .then(data => console.log('Сообщение с токеном', data))
//         .catch(error => console.log('Обработка ошибки', error))
// };

window.onload = function () {
    window.YaAuthSuggest.init({
            client_id: 'b7986b6acead461082b4bbf881148c8f',
            response_type: 'token',
            redirect_uri: 'http://localhost/users/yandex_auth_callback'
        },
        'http://localhost',
        {
            view: 'button',
            parentId: 'YaAuthButton',
            buttonView: 'main',
            buttonTheme: 'light',
            buttonSize: 'm',
            buttonBorderRadius: 0
        }
    )
        .then(function (result) {
            return result.handler();
        })
        .catch(function (error) {
            console.log('Что-то пошло не так: ', error);
            document.body.innerHTML += `Что-то пошло не так: ${JSON.stringify(error)}`;
        });
};