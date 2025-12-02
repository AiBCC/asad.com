// Enhanced Main JavaScript for Portfolio
document.addEventListener("DOMContentLoaded", function () {
  // Navbar scroll effect
  const navbar = document.querySelector("nav");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("bg-white/95", "dark:bg-dark-900/95", "shadow-sm");
      navbar.classList.remove("bg-white/90", "dark:bg-dark-900/90");
    } else {
      navbar.classList.remove(
        "bg-white/95",
        "dark:bg-dark-900/95",
        "shadow-sm"
      );
      navbar.classList.add("bg-white/90", "dark:bg-dark-900/90");
    }
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const href = this.getAttribute("href");
      if (href !== "#") {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
            block: "start",
          });
        }
      }
    });
  });

  // Project card animations
  const projectCards = document.querySelectorAll(".group");
  projectCards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-8px)";
    });

    card.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0)";
    });
  });

  // Form handling with enhanced validation
  const contactForm = document.querySelector("form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const submitBtn = this.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      // Basic form validation
      const requiredFields = this.querySelectorAll("[required]");
      let isValid = true;

      requiredFields.forEach((field) => {
        if (!field.value.trim()) {
          field.classList.add("border-red-500");
          isValid = false;
        } else {
          field.classList.remove("border-red-500");
        }
      });

      if (!isValid) {
        showNotification("Please fill in all required fields.", "error");
        return;
      }

      // Show loading state
      submitBtn.innerHTML =
        '<i class="fas fa-spinner fa-spin mr-2"></i>Sending...';
      submitBtn.disabled = true;

      // Simulate form submission
      setTimeout(() => {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
        showNotification(
          "Message sent successfully! I'll get back to you soon.",
          "success"
        );
        this.reset();
      }, 2000);
    });

    // Real-time validation
    const inputs = contactForm.querySelectorAll("input, textarea");
    inputs.forEach((input) => {
      input.addEventListener("input", function () {
        if (this.value.trim()) {
          this.classList.remove("border-red-500");
          this.classList.add("border-green-500");
        } else {
          this.classList.remove("border-green-500");
        }
      });

      input.addEventListener("blur", function () {
        this.classList.remove("border-green-500");
      });
    });
  }

  // Enhanced notification system
  function showNotification(message, type = "success") {
    // Remove existing notifications
    document.querySelectorAll(".notification").forEach((notification) => {
      notification.remove();
    });

    const notification = document.createElement("div");
    notification.className = `notification fixed top-4 right-4 z-50 px-6 py-4 rounded-lg shadow-lg transition-all duration-300 transform translate-x-full ${
      type === "success" ? "bg-green-500 text-white" : "bg-red-500 text-white"
    }`;

    notification.innerHTML = `
            <div class="flex items-center space-x-3">
                <i class="fas fa-${
                  type === "success" ? "check" : "exclamation"
                }-circle text-lg"></i>
                <span class="font-medium">${message}</span>
                <button class="ml-4 hover:opacity-70 transition-opacity">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;

    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
      notification.classList.remove("translate-x-full");
    }, 100);

    // Close button functionality
    notification.querySelector("button").addEventListener("click", () => {
      notification.classList.add("translate-x-full");
      setTimeout(() => {
        if (notification.parentNode) {
          notification.remove();
        }
      }, 300);
    });

    // Auto remove after 5 seconds
    setTimeout(() => {
      if (notification.parentNode) {
        notification.classList.add("translate-x-full");
        setTimeout(() => {
          if (notification.parentNode) {
            notification.remove();
          }
        }, 300);
      }
    }, 5000);
  }

  // Intersection Observer for scroll animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate-fade-in");
        // Stop observing after animation
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  // In the main.js file, update the Intersection Observer section:
  document
    .querySelectorAll(
      ".project-card, .certification-card, .volunteer-card, .experience-card"
    )
    .forEach((el) => {
      el.classList.add("opacity-0", "translate-y-8");
      observer.observe(el);
    });
  // Add click animation to buttons
  document.querySelectorAll("button, a[href]").forEach((element) => {
    element.addEventListener("click", function (e) {
      // Add ripple effect for buttons
      if (
        this.classList.contains("bg-primary-500") ||
        this.classList.contains("btn")
      ) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const ripple = document.createElement("span");
        ripple.style.cssText = `
                    position: absolute;
                    border-radius: 50%;
                    background: rgba(255,255,255,0.6);
                    transform: scale(0);
                    animation: ripple 0.6s linear;
                    pointer-events: none;
                    width: 100px;
                    height: 100px;
                    left: ${x - 50}px;
                    top: ${y - 50}px;
                `;

        this.style.position = "relative";
        this.style.overflow = "hidden";
        this.appendChild(ripple);

        setTimeout(() => {
          ripple.remove();
        }, 600);
      }
    });
  });

  // Add CSS for animations
  if (!document.querySelector("#portfolio-animations")) {
    const style = document.createElement("style");
    style.id = "portfolio-animations";
    style.textContent = `
            @keyframes fadeIn {
                from { 
                    opacity: 0; 
                    transform: translateY(20px); 
                }
                to { 
                    opacity: 1; 
                    transform: translateY(0); 
                }
            }
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
            .animate-fade-in {
                animation: fadeIn 0.6s ease-out forwards;
            }
            .line-clamp-3 {
                display: -webkit-box;
                -webkit-line-clamp: 3;
                -webkit-box-orient: vertical;
                overflow: hidden;
            }
            .timeline-item {
                transition: all 0.6s ease-out;
            }
        `;
    document.head.appendChild(style);
  }

  // Add scroll to top functionality
  const scrollToTopBtn = document.createElement("button");
  scrollToTopBtn.innerHTML = '<i class="fas fa-chevron-up"></i>';
  scrollToTopBtn.className =
    "fixed bottom-8 right-8 w-12 h-12 bg-primary-500 hover:bg-primary-600 text-white rounded-full shadow-lg hover:shadow-xl transition-all duration-300 opacity-0 invisible z-40 flex items-center justify-center";
  scrollToTopBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  document.body.appendChild(scrollToTopBtn);

  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      scrollToTopBtn.classList.remove("opacity-0", "invisible");
      scrollToTopBtn.classList.add("opacity-100", "visible");
    } else {
      scrollToTopBtn.classList.remove("opacity-100", "visible");
      scrollToTopBtn.classList.add("opacity-0", "invisible");
    }
  });
});

// Utility function for dynamic year in footer
function updateCurrentYear() {
  const yearElements = document.querySelectorAll("[data-current-year]");
  const currentYear = new Date().getFullYear();
  yearElements.forEach((element) => {
    element.textContent = currentYear;
  });
}

// Initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", updateCurrentYear);
