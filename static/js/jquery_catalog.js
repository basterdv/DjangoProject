/ Mobile menu toggle
document.getElementById('mobile-menu-button').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
});

// Filter functionality
const categoryItems = document.querySelectorAll('.category-item');
const categoryItemsMobile = document.querySelectorAll('.category-item-mobile');
const productCards = document.querySelectorAll('.product-card');

function filterProducts(category) {
    productCards.forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });

    // Update active state for desktop filters
    categoryItems.forEach(item => {
        if (item.dataset.category === category) {
            item.classList.add('active', 'bg-blue-600', 'text-white');
            item.classList.remove('bg-gray-100');
        } else {
            item.classList.remove('active', 'bg-blue-600', 'text-white');
            item.classList.add('bg-gray-100');
        }
    });

    // Update active state for mobile filters
    categoryItemsMobile.forEach(item => {
        if (item.dataset.category === category) {
            item.classList.add('active', 'bg-blue-600', 'text-white');
            item.classList.remove('bg-gray-100');
        } else {
            item.classList.remove('active', 'bg-blue-600', 'text-white');
            item.classList.add('bg-gray-100');
        }
    });
}

// Desktop category filtering
categoryItems.forEach(item => {
    item.addEventListener('click', function () {
        const category = this.dataset.category;
        filterProducts(category);
    });
});

// Mobile category filtering
categoryItemsMobile.forEach(item => {
    item.addEventListener('click', function () {
        const category = this.dataset.category;
        filterProducts(category);
    });
});

// Mobile filter toggle
const mobileFilterButton = document.getElementById('filter-mobile-button');
const mobileFilterContainer = document.getElementById('mobile-filter-container');
const mobileFilter = document.getElementById('mobile-filter');
const filterOverlay = document.getElementById('filter-overlay');
const closeMobileFilter = document.getElementById('close-mobile-filter');

mobileFilterButton.addEventListener('click', function () {
    mobileFilterContainer.classList.remove('hidden');
    setTimeout(() => {
        mobileFilter.classList.add('active');
    }, 10);
});

closeMobileFilter.addEventListener('click', function () {
    mobileFilter.classList.remove('active');
    setTimeout(() => {
        mobileFilterContainer.classList.add('hidden');
    }, 300);
});

filterOverlay.addEventListener('click', function () {
    mobileFilter.classList.remove('active');
    setTimeout(() => {
        mobileFilterContainer.classList.add('hidden');
    }, 300);
});

// ;(function (m, e, t, r, i, k, a) {
//     m[i] =
//         m[i] ||
//         function () {
//             ;(m[i].a = m[i].a || []).push(arguments)
//         }
//     m[i].l = 1 * new Date()
//     for (var j = 0; j < document.scripts.length; j++) {
//         if (document.scripts[j].src === r) {
//             return
//         }
//     }
//     ;(k = e.createElement(t)),
//         (a = e.getElementsByTagName(t)[0]),
//         (k.async = 1),
//         (k.src = r),
//         a.parentNode.insertBefore(k, a)
// })(window, document, 'script', 'https://mc.yandex.ru/metrika/tag.js', 'ym')
//
// ym(101904266, 'init', {
//     clickmap: true,
//     trackLinks: true,
//     accurateTrackBounce: true,
//     webvisor: true,
// })