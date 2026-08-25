document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    items.forEach((item) => io.observe(item));
  } else {
    items.forEach((item) => item.classList.add("in"));
  }
});

document.addEventListener("DOMContentLoaded", () => {
  // al-folio normally supplies this interaction. Our isolated theme does it here.
  document.querySelectorAll(".publications-page .bibliography .bibtex.btn").forEach((button) => {
    button.setAttribute("role", "button");
    button.setAttribute("tabindex", "0");

    const findTarget = () => {
      const item = button.closest("li");
      if (!item) return null;
      const candidates = [...item.querySelectorAll(".bibtex")];
      return candidates.find((el) => el !== button && !el.classList.contains("btn"));
    };

    const toggle = () => {
      const target = findTarget();
      if (!target) return;
      const isHidden = target.classList.toggle("hidden");
      button.classList.toggle("is-open", !isHidden);
      button.setAttribute("aria-expanded", String(!isHidden));
    };

    button.setAttribute("aria-expanded", "false");
    button.addEventListener("click", (event) => {
      event.preventDefault();
      toggle();
    });
    button.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggle();
      }
    });
  });

  document.querySelectorAll(".publications-page .bibliography .abstract.btn").forEach((button) => {
    const item = button.closest("li");
    if (!item) return;
    const target = [...item.querySelectorAll(".abstract")]
      .find((el) => el !== button && !el.classList.contains("btn"));
    if (!target) return;

    button.addEventListener("click", (event) => {
      event.preventDefault();
      target.classList.toggle("hidden");
    });
  });
});
