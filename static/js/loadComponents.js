document.addEventListener('DOMContentLoaded', function() {
    // Cargar el footer
    fetch('/template/componentes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-container').innerHTML = data;
        })
        .catch(error => console.error('Error cargando el footer:', error));
});