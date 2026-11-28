
const selected = {};

document.querySelectorAll(".chips").forEach(group => {
    group.addEventListener("click", e => {
        const btn = e.target.closest(".chip");
        if (!btn) return;
        group.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
        btn.classList.add("active");
        selected[group.dataset.group] = btn.dataset.value;

        const out = document.querySelector("#selection");
        if (out) {
            out.textContent = selected.color && selected.size ? `Selected: ${selected.color}, size ${selected.size}` : "Please select a color and size.";
        }
    });
});