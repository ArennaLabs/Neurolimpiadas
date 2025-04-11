document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
    
    // Mostrar la primera diapositiva
    slides[0].classList.add('opacity-100');
    
    // Cambiar diapositivas automáticamente
    setInterval(function() {
      slides[currentSlide].classList.remove('opacity-100');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('opacity-100');
    }, 5000);
  });