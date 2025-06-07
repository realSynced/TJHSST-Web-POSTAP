let timer;

// Start timer when page loads
window.onload = function () {
  let timerElement = document.getElementById("countdown");

  if (timerElement) {
    if (!localStorage.getItem("escapeEndTime")) {
      let fiveMinutes = 5 * 60 * 1000;

      let endTime = Date.now() + fiveMinutes;

      localStorage.setItem("escapeEndTime", endTime);
    }

    updateTimer();
    timer = setInterval(updateTimer, 1000);
  }
};

// Update timer
function updateTimer() {
  let timerElement = document.getElementById("countdown");
  if (!timerElement) {
    clearInterval(timer);
    return;
  }

  let endTime = localStorage.getItem("escapeEndTime");
  let timeLeft = endTime - Date.now();

  if (timeLeft <= 0) {
    clearInterval(timer);
    playerCaught();
    return;
  }

  let minutes = Math.floor(timeLeft / 60000);
  let seconds = Math.floor((timeLeft % 60000) / 1000);

  timerElement.innerHTML =
    minutes.toString().padStart(2, "0") +
    ":" +
    seconds.toString().padStart(2, "0");

  if (timeLeft < 60000) {
    timerElement.classList.add("time-warning");
  }
}

// Player got caught
function playerCaught() {
  // Reset timer
  localStorage.removeItem("escapeEndTime");

  window.location.href = "/start?caught=true";
}

function resetTimer() {
  localStorage.removeItem("escapeEndTime");
}

function redirectToStart() {
  resetTimer();

  // Redirect to start page
  window.location.href = "/start";
}
