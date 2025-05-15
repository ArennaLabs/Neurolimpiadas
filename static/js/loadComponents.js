
async function cargarNavbar() {
    try {
        const response = await fetch('/template/componentes/navbar.html');
        const html = await response.text();

        // Insertar el HTML de la navbar
        document.getElementById('navbar-container').innerHTML = html;

        // Inicializar la funcionalidad del menú
        inicializarNavbar();
    } catch (error) {
        console.error('Error al cargar la navbar:', error);
    }
}

function inicializarNavbar() {
    const menuToggle = document.getElementById('menu-toggle');
    const closeMenu = document.getElementById('close-menu');
    const mobileDropdown = document.getElementById('mobile-dropdown');
    const menuContent = mobileDropdown.querySelector('div');

    function openMenu() {
        document.body.style.overflow = 'hidden';
        mobileDropdown.classList.remove('hidden');
        requestAnimationFrame(() => {
            menuContent.classList.remove('translate-x-full');
        });
    }

    function closeMenuHandler() {
        document.body.style.overflow = '';
        menuContent.classList.add('translate-x-full');
        setTimeout(() => {
            mobileDropdown.classList.add('hidden');
        }, 300);
    }

    menuToggle.addEventListener('click', openMenu);
    closeMenu.addEventListener('click', closeMenuHandler);

    // Cerrar al hacer clic en el overlay
    mobileDropdown.addEventListener('click', (e) => {
        if (e.target === mobileDropdown) {
            closeMenuHandler();
        }
    });

    // Prevenir scroll cuando el menú está abierto
    mobileDropdown.addEventListener('touchmove', (e) => {
        if (e.target === mobileDropdown) {
            e.preventDefault();
        }
    }, { passive: false });
}

// Cargar la navbar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', cargarNavbar);

// Cargar el footer desde un archivo HTML externo
document.addEventListener('DOMContentLoaded', function () {
    fetch('/template/componentes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-container').innerHTML = data;
        })
        .catch(error => console.error('Error cargando el footer:', error));
});