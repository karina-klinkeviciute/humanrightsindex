const labels = document.querySelectorAll('label');

labels.forEach(label => {
    label.addEventListener('click', () => {
        const input = document.getElementById(label.htmlFor);
        input.checked = true;

        // Remove the 'active' class from all labels
        labels.forEach(label => label.classList.remove('active'));

        // Add the 'active' class to the clicked label
        label.classList.add('active');
    });
});
