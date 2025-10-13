const API_KEY = "f45d51406f914de6899151327251010";
const BASE = "https://api.weatherapi.com/v1/current.json"; // Use HTTPS to avoid browser blocks

const $ = (id) => document.getElementById(id);
const searchBtn = $("search");
const qInput = $("q");
const loadingEl = $("loading");
const errorEl = $("error");

async function fetchWeather(q) {
  errorEl.style.display = "none";
  loadingEl.style.display = "block";

  try {
    const url = `${BASE}?key=${API_KEY}&q=${encodeURIComponent(q)}&aqi=yes`;
    const res = await fetch(url);

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data = await res.json();
    render(data);
  } catch (err) {
    showError(err.message);
  } finally {
    loadingEl.style.display = "none";
  }
}

function render(data) {
  if (!data || !data.location) return showError("Invalid response");

  $("location").textContent = `${data.location.name}, ${data.location.country}`;
  $("localtime").textContent = data.location.localtime || "--";
  $("temp").textContent = `${data.current.temp_c}°C`;
  $("condition").textContent = data.current.condition.text;
  $("humidity").textContent = `${data.current.humidity}%`;
  $("wind").textContent = `${data.current.wind_kph} kph`;
  $("feelslike").textContent = `${data.current.feelslike_c}°C`;

  const iconUrl = data.current.condition.icon.startsWith("//")
    ? "https:" + data.current.condition.icon
    : data.current.condition.icon;

  $("icon").src = iconUrl;
  $("icon").alt = data.current.condition.text;
}

function showError(msg) {
  errorEl.style.display = "block";
  errorEl.className = "error";
  errorEl.textContent = msg;
}

searchBtn.addEventListener("click", () =>
  fetchWeather(qInput.value || "London")
);
qInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") fetchWeather(qInput.value || "London");
});

fetchWeather(qInput.value || "London");
