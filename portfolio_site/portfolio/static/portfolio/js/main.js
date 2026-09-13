document.addEventListener("DOMContentLoaded", function () {
  var sidebar = document.getElementById("sidebar");
  var navToggle = document.getElementById("navToggle");
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".side-nav-link"));
  var sections = navLinks
    .map(function (link) {
      var id = link.getAttribute("data-section");
      return document.getElementById(id);
    })
    .filter(Boolean);

  // Mobile sidebar toggle
  if (navToggle && sidebar) {
    navToggle.addEventListener("click", function () {
      sidebar.classList.toggle("is-open");
    });

    navLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        sidebar.classList.remove("is-open");
      });
    });
  }

  // Scroll-spy: highlight the nav link for the section currently in view
  function setActiveLink(id) {
    navLinks.forEach(function (link) {
      link.classList.toggle("is-active", link.getAttribute("data-section") === id);
    });
  }

  if ("IntersectionObserver" in window && sections.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            setActiveLink(entry.target.id);
          }
        });
      },
      { rootMargin: "-40% 0px -50% 0px", threshold: 0 }
    );

    sections.forEach(function (section) {
      observer.observe(section);
    });
  } else if (navLinks.length) {
    setActiveLink(navLinks[0].getAttribute("data-section"));
  }
});
