// journal.js
document.addEventListener("DOMContentLoaded", () => {
    const saveButton = document.getElementById("saveEntry");
    const entriesList = document.getElementById("entriesList");
    let journalEntries = JSON.parse(localStorage.getItem("journalEntries")) || [];

    function displayEntries() {
        entriesList.innerHTML = "";
        if (journalEntries.length === 0) {
            entriesList.innerHTML = "<p>No entries yet. Start tracking now! 📝</p>";
            return;
        }
        journalEntries.forEach((entry, index) => {
            const entryDiv = document.createElement("div");
            entryDiv.classList.add("entry");
            entryDiv.innerHTML = `
                <p><strong>Mood:</strong> ${entry.mood}</p>
                <p><strong>Spent on:</strong> ${entry.spending} | <strong>Amount:</strong> ₹${entry.amount}</p>
                <p><strong>Notes:</strong> ${entry.notes}</p>
                <button class="deleteEntry" data-index="${index}">❌ Delete</button>
            `;
            entriesList.appendChild(entryDiv);
        });
        document.querySelectorAll(".deleteEntry").forEach(button => {
            button.addEventListener("click", deleteEntry);
        });
    }

    saveButton.addEventListener("click", () => {
        const mood = document.getElementById("mood").value;
        const spending = document.getElementById("spending").value.trim();
        const amount = document.getElementById("amount").value.trim();
        const notes = document.getElementById("notes").value.trim();
        if (!spending || !amount) {
            alert("Please fill in all fields.");
            return;
        }
        const newEntry = { mood, spending, amount, notes };
        journalEntries.push(newEntry);
        localStorage.setItem("journalEntries", JSON.stringify(journalEntries));
        displayEntries();
    });

    function deleteEntry(event) {
        const index = event.target.getAttribute("data-index");
        journalEntries.splice(index, 1);
        localStorage.setItem("journalEntries", JSON.stringify(journalEntries));
        displayEntries();
    }
    displayEntries();
});
