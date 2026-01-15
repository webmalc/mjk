(function() {
   function testWebP(callback) {
      var webP = new Image();
      webP.onload = webP.onerror = function () {
          callback(webP.height == 2);
      };
      webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
   };
   
   testWebP(function(support) {
      if(support == true) {
        document.querySelector('body').classList.add('webp');

      //   $('.noWebpBg').each((i, el) => {
      //    $(el).css({
      //       "backgroundImage": `url(${$(el).data().srcwebp}`,
      //    })
      //   })
      }else {
        document.querySelector('body').classList.remove('webp');

         // $(el).css({
         //    "backgroundImage": `url(${$(el).data().src}`,
         // })
      }


   });
})();