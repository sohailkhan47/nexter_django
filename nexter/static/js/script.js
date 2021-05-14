'use strict';
const btnOpen = document.querySelector('.open');
const btnClose = document.querySelector('.close');
const nav = document.querySelector('.header__nav');
const link = document.querySelectorAll('.header__item');
// const not_liked = document.querySelectorAll('.not_liked');
// const liked = document.querySelectorAll('.liked');
if (btnOpen) {
btnOpen.addEventListener('click', function () {
  btnOpen.classList.add('hidden');
  btnClose.classList.remove('hidden');
  nav.classList.remove('hidden');
});

btnClose.addEventListener('click', function () {
  btnOpen.classList.remove('hidden');
  btnClose.classList.add('hidden');
  nav.classList.add('hidden');
})};
for (let i = 0; i < link.length; i++) {
  link[i].addEventListener('click', function () {
    btnClose.classList.add('hidden');
    btnOpen.classList.remove('hidden');
    nav.classList.add('hidden');
  });
}

const popupBtn = document.querySelector('.popup__btn');
const popup = document.querySelector('.popup');
const popupClose = document.querySelector('.popup__close');
const body = document.querySelector('.container');
const popUpContent = document.querySelector('.popup__content');

const hidePopUp = function () {
  popup.classList.remove('show_form');
  body.style.overflow = 'visible';
  popUpContent.style.transform = 'translate(-50%, -50%) scale(.5)';
  popUpContent.style.opacity = '0';
};

if (popupBtn) {
  popupBtn.addEventListener('click', function () {
    popup.classList.add('show_form');
    popUpContent.style.transform = 'translate(-50%, -50%) scale(1)';
    popUpContent.style.opacity = '1';
    popup.style.overflow = 'auto';
    if (popup.classList.contains('show_form')) {
      body.style.overflow = 'hidden';
    }
  });
  popupClose.addEventListener('click', hidePopUp);
}

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && popup.classList.contains('show_form')) {
    hidePopUp();
  }
});

// Testing the like icon functionality
const likeJs = document.querySelector('.js__like');
const liked = document.querySelector('.home__liked');
// if (likeJs) {
//   likeJs.addEventListener('click', function () {
//   }
// };

setTimeout(function () {
  $('#message').fadeOut('slow');
}, 3000);