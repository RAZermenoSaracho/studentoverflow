/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

/* EXTRA JS FOR DROPDOWNS
When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropdownFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

// Toggle form de respuesta en question.html
function toggleAnswerForm() {
  const form = document.getElementById('answer-form');
  if (form) {
      form.classList.toggle('d-none');
  }
}

// Tabs en profile.html
document.addEventListener('DOMContentLoaded', function () {
  const triggerTabList = [].slice.call(document.querySelectorAll('#profileTabs a'));
  triggerTabList.forEach(function (triggerEl) {
      const tabTrigger = new bootstrap.Tab(triggerEl);
      triggerEl.addEventListener('click', function (e) {
          e.preventDefault();
          tabTrigger.show();
      });
  });
});

function toggleCategoryFilter() {
    const form = document.getElementById("category-filter-container");
    form.classList.toggle("d-none");
}

// Tom Select
document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector('#categories-select')) {
        new TomSelect('#categories-select', {
            plugins: ['remove_button'],
            persist: false,
            maxItems: null,
            valueField: 'value',
            labelField: 'text',
            searchField: ['text'],
            create: false,
            render: {
                item: function(data, escape) {
                    return `<div>${escape(data.text)}</div>`;
                },
                option: function(data, escape) {
                    return `<div>${escape(data.text)}</div>`;
                }
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const options = {
        plugins: ['remove_button'],
        persist: false,
        create: true, // Permite agregar categorías nuevas
        delimiter: ",",
        maxItems: null,
    };

    if (document.querySelector("#ask-categories")) {
        new TomSelect("#ask-categories", options);
    }

    if (document.querySelector("#edit-categories")) {
        new TomSelect("#edit-categories", options);
    }
});
