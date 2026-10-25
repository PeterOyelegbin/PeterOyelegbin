// Set dynamic current year
document.getElementById('year').textContent = new Date().getFullYear();

// PROJECT CAROUSEL LOGIC
let currentProjectSlide = 0;
const track = document.getElementById('projectCarouselTrack');
const totalProjectSlides = track.children.length;
const projectDots = document.querySelectorAll('.project-dot');

function updateProjectCarousel() {
    track.style.transform = `translateX(-${currentProjectSlide * 100}%)`;
    projectDots.forEach((dot, index) => {
        if (index === currentProjectSlide) {
            dot.classList.remove('bg-slate-700');
            dot.classList.add('bg-emerald-400');
        } else {
            dot.classList.remove('bg-emerald-400');
            dot.classList.add('bg-slate-700');
        }
    });
}

function moveProjectSlide(direction) {
    currentProjectSlide = (currentProjectSlide + direction + totalProjectSlides) % totalProjectSlides;
    updateProjectCarousel();
}

function goToProjectSlide(slideIndex) {
    currentProjectSlide = slideIndex;
    updateProjectCarousel();
}

// REVIEWS CAROUSEL LOGIC
let currentReviewSlide = 0;
const reviewTrack = document.getElementById('reviewCarouselTrack');
const totalReviewSlides = reviewTrack.children.length;
const reviewDots = document.querySelectorAll('.review-dot');

function updateReviewCarousel() {
    reviewTrack.style.transform = `translateX(-${currentReviewSlide * 100}%)`;
    reviewDots.forEach((dot, index) => {
        if (index === currentReviewSlide) {
            dot.classList.remove('bg-slate-700');
            dot.classList.add('bg-emerald-400');
        } else {
            dot.classList.remove('bg-emerald-400');
            dot.classList.add('bg-slate-700');
        }
    });
}

function moveReviewSlide(direction) {
    currentReviewSlide = (currentReviewSlide + direction + totalReviewSlides) % totalReviewSlides;
    updateReviewCarousel();
}

function goToReviewSlide(slideIndex) {
    currentReviewSlide = slideIndex;
    updateReviewCarousel();
}

// STAR RATING FORM LOGIC
const selectedRatingInput = document.getElementById('selectedRating');
let selectedStarRating = parseInt(selectedRatingInput.value, 10);
function setRating(rating) {
    selectedStarRating = rating;
    selectedRatingInput.value = rating;
    const starContainer = document.getElementById('starRatingContainer');
    const stars = starContainer.querySelectorAll('i');
    stars.forEach((star, index) => {
        if (index < rating) {
            star.className = 'fa-solid fa-star cursor-pointer text-amber-400 transition-colors';
        } else {
            star.className = 'fa-solid fa-star cursor-pointer text-slate-600 hover:text-amber-400 transition-colors';
        }
    });
}
// Initialize default 5 stars
setRating(selectedStarRating);
