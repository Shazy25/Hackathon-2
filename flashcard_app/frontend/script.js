const toggleBtn = document.getElementById('toggle-btn');
const sidebar = document.querySelector('.sidebar');
const mainContent = document.querySelector('.main-content');

toggleBtn.addEventListener('click', () => {
  sidebar.classList.toggle('active');
  mainContent.classList.toggle('shifted');
});
document.getElementById("generateBtn").addEventListener("click", async () => {
  const notes = document.getElementById("notes").value;
  if (!notes.trim()) return alert("Please enter your notes");

  const response = await fetch("http://127.0.0.1:5000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ notes }),
  });

  const data = await response.json();
  const cardGrid = document.getElementById("cardGrid");
  cardGrid.innerHTML = "";

  data.flashcards.forEach((card) => {
    const div = document.createElement("div");
    div.className = "flashcard";
    div.innerHTML = `<div class="front">card.front</div><div class="back">{card.back}</div>`;
    cardGrid.appendChild(div);
  });

  document.getElementById("cardSection").style.display = "block";
});



