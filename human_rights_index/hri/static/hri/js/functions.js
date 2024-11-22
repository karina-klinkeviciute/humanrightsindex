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

document.addEventListener("DOMContentLoaded", function () {
    const pageTitle = document.querySelector('#page-title');
    // Add the scroll event listener
    window.addEventListener('scroll', function () {
        if (window.scrollY > 1) { // Fade out the title if scrolled down even slightly
            pageTitle.classList.add('hidden');
        } else {
            pageTitle.classList.remove('hidden');
        }
    });
});