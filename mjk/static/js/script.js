let sm = 576,
  md = 768,
  lg = 992,
  xl = 1200,
  xxl = 1360;

let wdWidth = () => {
  return window.innerWidth;
};
let wdHeight = () => {
  return window.innerHeight;
};

$(document).ready(function () {
  let hideMenu = () => {
    $(".hamburger").removeClass("is-active");
    $(".header__menu").fadeOut();
  };

  let hideHeaderDropdownMenu = () => {
    $(".header__menu--dropdown>span, .header__menu--dropdown>a").removeClass(
      "active"
    );
    $(".header__menu--dropdown > ul").slideUp();
    if (wdWidth() > lg) {
      setTimeout(() => {
        $(".header__menu--dropdown > ul").css({ display: "" });
      }, 1000);
    }
  };

  //window resizes

  let bodyPaddingReset = () => {
    $("body").css({
      paddingTop: 0,
    });
  };

  let headerResize = () => {
    if (wdWidth() < md) {
      $(".header__menu").append($(".header__phone, .header__mail"));
    } else {
      $(".header-phone-mail-after-md").append(
        $(".header__phone, .header__mail")
      );
    }

    if (wdWidth() < lg) {
      $(".header__menu").append($(".header .button__gray"));
    } else {
      $(".header-button-after-sm").append($(".header .button__gray"));
    }

    $("body").css({
      paddingTop: $(".header").outerHeight() + "px",
    });
  };

  let resize = () => {
    bodyPaddingReset();
    headerResize();
    hideMenu();
    // hideHeaderDropdownMenu();
  };

  resize();
  $(window).on("resize", resize);

  let scrollBehaviorMenu = (e) => {
    hideMenu();
  };

  let scrollBehaviorHeader = (e) => {
    let top = $(window).scrollTop();
    let $header = $(".header");

    let maxTop = wdWidth() > md ? 20 : 20;

    if (!$header.hasClass("scroll") && top > maxTop) {
      $header.addClass("scroll");
    }
    if ($header.hasClass("scroll") && top < maxTop) {
      $header.removeClass("scroll");
      setTimeout(() => {
        headerResize();
      }, 200);
    }
  };

  let scrollBehaviorHeaderMenu = (e) => {
    // hideHeaderDropdownMenu();
  };

  let scrollBehaviorHeaderBg = (e) => {
    $(".header.transparent").css({ background: "" });
  };
  let scrollWindow = (e) => {
    scrollBehaviorMenu(e);
    scrollBehaviorHeader(e);
    scrollBehaviorHeaderMenu(e);
    scrollBehaviorHeaderBg(e);
  };

  scrollWindow();
  $(window).on("scroll", scrollWindow);

  let missMenuOpen = (e) => {
    if (
      !$(e.target).closest(".header__menu").length &&
      $(".hamburger").hasClass("is-active")
    ) {
      hideMenu();
    }
  };

  let missHeaderDropdownMenu = (e) => {
    if (!$(e.target).closest(".header__menu").length) {
      // hideHeaderDropdownMenu();
    }
  };

  let missModals = (e) => {
    if (
      !$(e.target).closest(".modal .modal__container").length &&
      !$(e.target).closest(".header__menu").length
    ) {
      closeModals();
    }
  };

  let notTargets = (e) => {
    missMenuOpen(e);
    missHeaderDropdownMenu(e);
    missModals(e);
  };

  $(window).on("click", notTargets);

  // $(".header__menu--dropdown > span").on("click", function (e) {
  //   e.preventDefault();
  //   e.stopPropagation();
  //   e.stopImmediatePropagation();

  //   if (wdWidth() < lg) {
  //     $(this).toggleClass("active");
  //     if (wdWidth() < lg) {
  //       $(".header__menu--dropdown > span + ul").slideToggle();
  //     } else {
  //       $(".header__menu--dropdown > span + ul").fadeToggle();
  //     }
  //   }

  //   if ($(this).hasClass("active")) {
  //     $("body").css({ overflow: "hidden" });
  //   } else {
  //     $("body").css({ overflow: "" });
  //   }
  // });

  //hamburger

  $(".hamburger").on("click", function (e) {
    e.preventDefault();
    e.stopPropagation();

    let top = $(window).scrollTop();
    if (top < 20 && !$(".hamburger").hasClass("is-active")) {
      $(".header.transparent").css({ background: "#272727" });
    } else {
      $(".header.transparent").css({ background: "" });
    }

    $(this).toggleClass("is-active");
    $(".header__menu").slideToggle();
  });

  //Modals open

  $(".open__feedback").on("click", function (e) {
    e.preventDefault();
    e.stopPropagation();
    $(".modal__feedback").fadeIn();
    $("body").css({ overflow: "hidden" });
    hideMenu(e);
  });

  $(".open__kp").on("click", function (e) {
    e.preventDefault();
    e.stopPropagation();
    $(".modal__kp").fadeIn();
    $("body").css({ overflow: "hidden" });
    hideMenu(e);
  });

  // Modals close

  let closeModals = (e) => {
    if (wdWidth() < lg) {
      hideMenu();
      // hideHeaderDropdownMenu();
      $(".modal").fadeOut();
    } else {
      $(".modal").fadeOut();
    }
    $("body").css({ overflow: "" });
  };

  $(".modal__close").on("click", function (e) {
    e.preventDefault();

    closeModals(e);
  });

  new Swiper(".swiper-banner", {
    spaceBetween: 0,
    navigation: {
      nextEl: ".swiper-banner .swiper-button-next",
      prevEl: ".swiper-banner .swiper-button-prev",
    },
    slidesPerView: 1,
    rewind: true,
    // autoplay: {
    //   delay: 6000,
    // },
    loop: $(".swiper-banner .swiper-slide").length > 1 ? true : false,
    speed: 600,
    // effect: 'fade',
    // breakpoints: {
    //   // when window width is >= 320px
    //   320: {
    //     slidesPerView: 1,
    //     spaceBetween: 20,
    //   },
    //   576: {
    //     slidesPerView: 2,
    //   },
    //   992: {
    //     slidesPerView: 3,
    //   },
    //   1200: {
    //     slidesPerView: 1,
    //   },
    // },
  });

  $(".email").mask("A", {
    translation: {
      A: { pattern: /[\w@\-.+]/, recursive: true },
    },
  });

  let optionsPhone = {
    onComplete: function (cep, e, $elem) {

      setTimeout(() => {
        $elem.parent().addClass("success");
        $elem.parent().removeClass("error");
      }, 200);
    },
    onChange: function (cep, e, $elem) {
      setTimeout(() => {
        
        $elem.parent().addClass("error");
      }, 100);
        
    },
    onInvalid: function (val, e, f, invalid, options) {},
  };

  $(".phone").mask("+0 000 000 00 00", optionsPhone);

  // $(".item__4 p").each(function (i, el) {
  //   let text = $(el).text().split("").slice(0, 125).join("") + "...";
  //   $(el).text(text);
  // });

  $('input[type="checkbox"][name="checkbox"]').on("change", function (e) {
    $(this)
      .closest("form")
      .find("button")
      .attr("disabled", function (index, attr) {
        return attr == "disabled" ? false : "disabled";
      });
  });

  $(document).on("click", "a[href^=\\#]", function (e) {
    e.preventDefault();
    let id = $(this).attr("href");
    $("html,body").animate(
      { scrollTop: $(id).offset().top - $(".header").outerHeight() },
      600
    );
  });

  $(".object-swiper .swiper-buttons").on("click", function (e) {
    e.preventDefault();
    // e.stopPropagation();
  });

  $(".object-swiper").each(function (i, el) {
    let swiper = new Swiper(el, {
      spaceBetween: 0,
      navigation: {
        nextEl: $(el).find(".swiper-button-next")[0],
        prevEl: $(el).find(".swiper-button-prev")[0],
      },
      slidesPerView: 1,
      rewind: true,
      autoplay: {
        delay: 4500 + +(`${i}` + "000"),
      },
      loop: $(el).find(".swiper-slide").length > 1 ? true : false,
      speed: 600,
      // effect: 'fade',
      // breakpoints: {
      //   // when window width is >= 320px
      //   320: {
      //     slidesPerView: 1,
      //     spaceBetween: 20,
      //   },
      //   576: {
      //     slidesPerView: 2,
      //   },
      //   992: {
      //     slidesPerView: 3,
      //   },
      //   1200: {
      //     slidesPerView: 1,
      //   },
      // },
      on: {
        init: function (swiper) {
          if (swiper.slides.length <= 1) {
            $(el).find(".swiper-buttons").remove();
          }
        },
      },
    });
  });

  $("select").niceSelect();

  (function () {
    let $inputRequired = $(".modal__kp .form__input2.required  input");

    let Validate = (inputText, index) => {
      var nameformat = /^[+а-я0-9ё][а-я0-9ё\.\s,]{0,50}$/i;

      if (inputText.match(nameformat)) {
        if (inputText.length) {
          $inputRequired.eq(index).parent().removeClass("error");
          $inputRequired.eq(index).parent().addClass("success");
          return true;
        } else {
          $inputRequired.eq(index).parent().removeClass("success");
          $inputRequired.eq(index).parent().addClass("error");
        }
      } else {
        $inputRequired.eq(index).parent().removeClass("success");
        $inputRequired.eq(index).parent().addClass("error");
      }
    };

    let validation = (index) => {
      let value = $inputRequired.eq(index).prop("value");
      Validate(value, index);
    };

    let checkInputRequired = () => {
      $inputRequired.each(function (i, el) {
        validation(i);
      });

      let filter = $inputRequired.parent().filter(function (i, el) {
        if ($(el).hasClass("success")) {
          return false;
        } else {
          document.querySelector(".modal__kp").scrollTop = 0;
          return true;
        }
      });

      return filter.length == 0;
    };

    $inputRequired.on("input", function (e) {
      let index = $inputRequired.index(this);
      validation(index);
    });

    let clearClassErrorForm = () => {
      $(".form__input2.required").removeClass("error");
      $(".form__input2.required").addClass("success");
    };

    $(".modal__kp form button").on("click", function (e) {
      e.preventDefault();

      if (checkInputRequired()) {
        setTimeout(() => {
          let form = document.querySelector(".modal__kp form");
          form.submit();
        }, 500);
      }
    });
  })();
});
