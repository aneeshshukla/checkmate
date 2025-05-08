async function updateMetrics() {
  const response = await fetch("/update_metrics");
  const data = await response.json();

  // Update UI elements
  document.querySelector(
    ".card p:nth-child(2)"
  ).innerHTML = `<strong>CPU Usage:</strong> ${data.cpu_usage}%`;
  document.querySelector(
    ".card p:nth-child(3)"
  ).innerHTML = `<strong>Memory Usage:</strong> ${data.ram_usage}%`;
  document.querySelector(
    ".card p:nth-child(4)"
  ).innerHTML = `<strong>GPU Usage:</strong> ${data.gpu_usage ?? "N/A"}%`;
  document.querySelector(
    ".card p:nth-child(5)"
  ).innerHTML = `<strong>Focused App:</strong> ${data.focused_app}`; //`__________________`; //
}
// Refresh metrics every 1 seconds
setInterval(updateMetrics, 1000);
