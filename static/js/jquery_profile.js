// Mobile menu toggle
document.getElementById('mobile-menu-button').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
});

// Category dropdown
const categoryToggle = document.getElementById('category-toggle');
const categoryDropdown = document.getElementById('category-dropdown');

categoryToggle.addEventListener('click', function () {
    categoryDropdown.classList.toggle('hidden');
});

// Close dropdown when clicking outside
document.addEventListener('click', function (event) {
    if (!categoryToggle.contains(event.target) && !categoryDropdown.contains(event.target)) {
        categoryDropdown.classList.add('hidden');
    }
});

// Select category
categoryDropdown.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('selected-category').textContent = this.textContent;
        categoryDropdown.classList.add('hidden');
    });
});

// Condition buttons
const conditionButtons = document.querySelectorAll('.condition-btn');
conditionButtons.forEach(button => {
    button.addEventListener('click', function () {
        conditionButtons.forEach(btn => {
            btn.classList.remove('bg-blue-50', 'border-blue-300', 'text-blue-700');
        });
        this.classList.add('bg-blue-50', 'border-blue-300', 'text-blue-700');
        document.getElementById('condition').value = this.textContent.trim();
    });
});

// Tags functionality
const tagInput = document.getElementById('tag-input');
const addTagBtn = document.getElementById('add-tag-btn');
const tagsContainer = document.getElementById('tags-container');
const tags = [];

function addTag(tag) {
    if (tags.length >= 5) {
        alert('Можно добавить не более 5 тегов');
        return;
    }

    if (tag.trim() === '') return;

    if (!tags.includes(tag)) {
        tags.push(tag);

        const tagElement = document.createElement('div');
        tagElement.className = 'inline-flex items-center bg-blue-50 text-blue-600 rounded-full px-3 py-1 text-xs font-medium';
        tagElement.innerHTML = `
                    ${tag}
                    <button type="button" class="ml-2 text-blue-600 hover:text-blue-800 remove-tag" data-tag="${tag}">
                        <i class="fas fa-times"></i>
                    </button>
                `;

        tagsContainer.appendChild(tagElement);
        tagInput.value = '';
    }
}

addTagBtn.addEventListener('click', function () {
    addTag(tagInput.value);
});

tagInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        addTag(tagInput.value);
    }
});

// Remove tag
tagsContainer.addEventListener('click', function (e) {
    if (e.target.classList.contains('remove-tag') || e.target.parentElement.classList.contains('remove-tag')) {
        const tagToRemove = e.target.classList.contains('remove-tag')
            ? e.target.getAttribute('data-tag')
            : e.target.parentElement.getAttribute('data-tag');

        const index = tags.indexOf(tagToRemove);
        if (index !== -1) {
            tags.splice(index, 1);
        }

        e.target.closest('div').remove();
    }
});

// Image upload preview
const imageUpload = document.getElementById('image-upload');
const imagePreviewContainer = document.getElementById('image-preview-container');
const maxImages = 10;
let uploadedImages = [];

imageUpload.addEventListener('change', function (e) {
    const files = Array.from(e.target.files);

    if (files.length + uploadedImages.length > maxImages) {
        alert(`Можно загрузить не более ${maxImages} фотографий`);
        return;
    }

    files.forEach(file => {
        if (!file.type.match('image.*')) return;

        const reader = new FileReader();

        reader.onload = function (e) {
            uploadedImages.push({
                name: file.name,
                url: e.target.result
            });

            updateImagePreviews();
        };

        reader.readAsDataURL(file);
    });
});

function updateImagePreviews() {
    // Clear existing previews except the upload button
    const uploadBtn = imagePreviewContainer.querySelector('label');
    imagePreviewContainer.innerHTML = '';

    uploadedImages.forEach((image, index) => {
        const preview = document.createElement('div');
        preview.className = 'relative image-preview group';
        preview.innerHTML = `
                    <img src="${image.url}" alt="Preview" class="w-full h-full object-cover rounded-lg">
                    <button type="button" class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 remove-image" data-index="${index}">
                        <i class="fas fa-times text-xs"></i>
                    </button>
                `;
        imagePreviewContainer.appendChild(preview);
    });

    // Re-add upload button if we have space
    if (uploadedImages.length < maxImages) {
        imagePreviewContainer.appendChild(uploadBtn);
    }

    // Update file input to allow remaining slots
    const remainingSlots = maxImages - uploadedImages.length;
    imageUpload.setAttribute('multiple', remainingSlots > 1);
}

// Remove image
imagePreviewContainer.addEventListener('click', function (e) {
    if (e.target.classList.contains('remove-image') || e.target.parentElement.classList.contains('remove-image')) {
        const index = e.target.classList.contains('remove-image')
            ? parseInt(e.target.getAttribute('data-index'))
            : parseInt(e.target.parentElement.getAttribute('data-index'));

        uploadedImages.splice(index, 1);
        updateImagePreviews();
    }
});

// Character count for description
const description = document.getElementById('description');
const charCount = document.getElementById('char-count');

description.addEventListener('input', function () {
    charCount.textContent = description.value.length;
});

// Form submission
const form = document.getElementById('ad-form');

form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Validate required fields
    if (!validateForm()) {
        alert('Пожалуйста, заполните все обязательные поля');
        return;
    }

    // Here you would typically send the form data to the server
    alert('Объявление успешно опубликовано!');
    // form.submit();
});

function validateForm() {
    const requiredFields = ['title', 'price', 'exchange-for', 'description', 'city'];

    for (const field of requiredFields) {
        const element = document.getElementById(field);
        if (!element.value.trim()) {
            element.focus();
            return false;
        }
    }

    if (tags.length === 0) {
        alert('Добавьте хотя бы один тег');
        tagInput.focus();
        return false;
    }

    if (uploadedImages.length === 0) {
        alert('Добавьте хотя бы одно фото товара');
        imageUpload.focus();
        return false;
    }

    return true;
}

// Save draft
document.getElementById('save-draft-btn').addEventListener('click', function () {
    alert('Черновик успешно сохранен!');
});
