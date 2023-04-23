const button = document.getElementById('user-menu-button');
const dropdown = document.getElementById('nav-dropdown');

if (button && dropdown) {
    button.addEventListener('click', () => {
        const isExpanded = dropdown.classList.contains('hidden');
        if (isExpanded) {
            dropdown.classList.remove('hidden');
        } else {
            dropdown.classList.toggle('hidden');
        }
    });

    document.addEventListener('click', (event) => {
        const isClickInsideDropdown = dropdown.contains(event.target);
        const isClickInsideButton = button.contains(event.target);
        if (!isClickInsideDropdown && !isClickInsideButton) {
            dropdown.classList.add('hidden');
        }
    });
}