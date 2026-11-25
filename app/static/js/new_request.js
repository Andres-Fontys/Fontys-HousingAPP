const category = document.getElementById('category');
const otherLabel = document.getElementById('category-other-label');
const otherInput = document.getElementById('category-other');

category.addEventListener('change', () => {
    const isOther = category.value === 'Other';
    otherLabel.hidden = !isOther;
    otherInput.required = isOther;
    if (!isOther) otherInput.value = '';
});