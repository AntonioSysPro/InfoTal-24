document.addEventListener('DOMContentLoaded', function() {
    const botonesLeerMas = document.querySelectorAll('.leer-mas');

    botonesLeerMas.forEach(function(boton) {
        boton.addEventListener('click', function() {
            const noticia = boton.parentNode;
            const parrafo = noticia.querySelector('p');
            parrafo.classList.toggle('expandido');
            if (parrafo.classList.contains('expandido')) {
                boton.textContent = 'Leer menos';
            } else {
                boton.textContent = 'Leer más';
            }
        });
    });
});
