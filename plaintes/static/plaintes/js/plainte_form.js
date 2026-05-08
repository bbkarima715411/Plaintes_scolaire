function updateFilledState(field) {
    if (field.value.trim() !== '') {
        field.classList.add('field-filled');
    } else {
        field.classList.remove('field-filled');
    }
}

document.querySelectorAll('.plainte-form-field input, .plainte-form-field select, .plainte-form-field textarea').forEach(function(field) {
    updateFilledState(field);
    field.addEventListener('input', function() {
        updateFilledState(field);
    });
    field.addEventListener('change', function() {
        updateFilledState(field);
    });
});
