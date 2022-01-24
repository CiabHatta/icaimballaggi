var swiper = new Swiper(".swiper-container", {
    slidesPerView: "auto",
    spaceBetween: 30,
    freeMode: true,
    autoHeight: true, 
    centeredSlides: false,
    loop: false,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    scrollbar: {
        el: '.swiper-scrollbar',
        draggable: true,
    },
  });

window.addEventListener('load', function () {

    var cookieconsent = initCookieConsent();

    cookieconsent.run({
        current_lang: 'it',
        page_scripts: true,
        autorun: true,

        onAccept: function () {
            // do something ...
        },

        languages: {
            en: {
                consent_modal: {
                    title: 'Utilizziamo i cookie',
                    description: 'I cookie verranno utilizzati per migliorare la tua esperienzia',
                    primary_btn: {
                        text: 'Accetta',
                        role: 'accept_all'  //'accept_selected' or 'accept_all'
                    },
                    secondary_btn: {
                        text: 'Rifiuta',
                        role: 'accept_necessary'   //'settings' or 'accept_necessary'
                    }
                },
                settings_modal: {
                    title: 'Impostazioni',
                    save_settings_btn: 'Salva Impostazioni',
                    accept_all_btn: 'Accetta tutti',
                    reject_all_btn: 'Rifiuta tutti', // optional, [v.2.5.0 +]
                    close_btn_label: 'Chiudi',
                    blocks: [
                        {
                            title: 'Cookie usage',
                            description: 'Your cookie usage disclaimer'
                        }, {
                            title: 'Strictly necessary cookies',
                            description: 'Category description ... ',
                            toggle: {
                                value: 'necessary',
                                enabled: false,
                                readonly: true
                            }
                        }, {
                            title: 'Analytics cookies',
                            description: 'Category description ...',
                            toggle: {
                                value: 'analytics',
                                enabled: false,
                                readonly: false
                            }
                        },
                    ]
                }
            }
        }
    });
});


window.onload = function() {

animateCSS('#loader-wrap', 'fadeOut').then((message) => {
    document.querySelector("#loader-wrap").style.display = "none";
});
};

window.onscroll = function() {scrollFunction()};

const animateCSS = (element, animation, prefix = 'animate__') =>
// We create a Promise and return it
new Promise((resolve, reject) => {
const animationName = `${prefix}${animation}`;
const node = document.querySelector(element);

node.classList.add(`${prefix}animated`, animationName);

// When the animation ends, we clean the classes and resolve the Promise
function handleAnimationEnd(event) {
  event.stopPropagation();
  node.classList.remove(`${prefix}animated`, animationName);
  resolve('Animation ended');
}

node.addEventListener('animationend', handleAnimationEnd, {once: true});
});

function toggleNavbar(action){

    var sidebar = document.getElementById("sidebar");
    var btn = document.getElementById("menu-btn");
    
    console.log(sidebar.getAttribute('style'));
    if (action == 'open') {
        sidebar.setAttribute('style', 'display:flex !important')
        animateCSS('.side-navbar', 'slideInRight').then((message) => {
        });
    }
    else {
        animateCSS('.side-navbar', 'slideOutRight').then((message) => {
            sidebar.setAttribute('style', 'display:none')
        });
        
    }
    
    
}

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("navbar").style.backgroundColor = "white";
        document.getElementById("navbar").style.boxShadow = "0px 6px 8px rgba(0,0,0,0.111)";
        document.getElementById("scroll-top-btn").style.display= "flex";
    } else {
        document.getElementById("navbar").style.backgroundColor = "transparent";
        document.getElementById("navbar").style.boxShadow= "none";
        document.getElementById("scroll-top-btn").style.display= "none";
        
    }
}
function scrolltop(){
    window.scrollTo(0, 0);
}