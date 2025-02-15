// error.js
document.addEventListener("DOMContentLoaded", function () {
    console.log("🚨 Error Page Loaded!");

    // Redirect to dashboard after 10 seconds
    setTimeout(() => {
        window.location.href = 'dashboard.html';
    }, 10000);

    // Animate button click effects
    document.querySelectorAll(".error-actions button").forEach(button => {
        button.addEventListener("click", function () {
            button.style.transform = "scale(0.95)";
            setTimeout(() => {
                button.style.transform = "scale(1)";
            }, 150);
        });
    });
});
