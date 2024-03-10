$(document).ready(function() {
        var carousel = $('.carousel');
        var slides = $('.carousel .slide');
        var slideWidth = slides.first().width();
        var currentIndex = 0;

        function showSlide(index) {
            var translateValue = -index * slideWidth;
            carousel.css('transform', 'translateX(' +translateValue + px);
        }

        function nextSlide() {
            currentIndex = (currentIndex + 1) % slides.length;
            showSlide(currentSlides);
            }
            setInterval(nextSlide, 5000);
       });