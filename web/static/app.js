const statusLine = document.getElementById("status-line");
const agentsEl = document.getElementById("agents");
const statsEl = document.getElementById("stats");
const eventLog = document.getElementById("event-log");
const form = document.getElementById("config-form");
const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");

function formPayload() {
  const data = new FormData(form);
  const num = (name) => Number(data.get(name));
  const seedRaw = data.get("seed");
  return {
    number_of_freshers: num("number_of_freshers"),
    run_time: num("run_time"),
    min_calls_per_wave: num("min_calls_per_wave"),
    max_calls_per_wave: num("max_calls_per_wave"),
    min_sleep_interval: num("min_sleep_interval"),
    max_sleep_interval: num("max_sleep_interval"),
    min_call_duration: num("min_call_duration"),
    max_call_duration: num("max_call_duration"),
    seed: seedRaw === "" || seedRaw === null ? null : Number(seedRaw),
  };
}

function renderStatus(snapshot) {
  const isRunning = snapshot.status === "running";
  startBtn.disabled = isRunning;
  startBtn.title = isRunning ? "Simulation is already running" : "Start a new simulation";
  stopBtn.disabled = !isRunning;
  stopBtn.title = !isRunning ? "No simulation is currently running" : "Stop the current simulation";
  statusLine.textContent = `Status: ${snapshot.status} · loop ${snapshot.loop || 0}`;

  if (!snapshot.agents || snapshot.agents.length === 0) {
    agentsEl.innerHTML = `<p class="status" style="grid-column: 1 / -1; margin-top: 0;">No agents active. Start a simulation to see them here.</p>`;
  } else {
    agentsEl.innerHTML = snapshot.agents
      .map(
        (a) => `
      <article class="agent">
        <div class="name">${a.name}</div>
        <span class="state ${a.state}">${a.state}</span>
        <div>calls: ${a.calls_handled}</div>
      </article>`
    )
    .join("");
  }
  statsEl.textContent = JSON.stringify(snapshot.stats || {}, null, 2);
}

async function refresh() {
  const res = await fetch("/api/simulation/status");
  const data = await res.json();
  renderStatus(data);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const originalText = startBtn.textContent;
  startBtn.textContent = "Starting...";
  startBtn.disabled = true;
  startBtn.setAttribute("aria-busy", "true");
  let res;
  try {
    res = await fetch("/api/simulation/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formPayload()),
    });
  } catch (err) {
    statusLine.textContent = `Error: ${err.message}`;
    startBtn.textContent = originalText;
    startBtn.disabled = false;
    startBtn.removeAttribute("aria-busy");
    return;
  }
  const data = await res.json();
  if (!res.ok) {
    statusLine.textContent = `Error: ${data.detail || res.statusText}`;
    startBtn.textContent = originalText;
    startBtn.disabled = false;
    startBtn.removeAttribute("aria-busy");
    return;
  }
  startBtn.textContent = originalText;
  startBtn.removeAttribute("aria-busy");
  renderStatus(data.status);
  connectEvents();
});

document.getElementById("stop-btn").addEventListener("click", async () => {
  const res = await fetch("/api/simulation/stop", { method: "POST" });
  const data = await res.json();
  renderStatus(data.status);
});

let eventSource;
function connectEvents() {
  if (eventSource) {
    eventSource.close();
  }
  eventSource = new EventSource("/api/simulation/events");
  eventSource.onmessage = (msg) => {
    const data = JSON.parse(msg.data);
    const li = document.createElement("li");
    li.textContent = `[${data.kind}] ${data.message || ""}`;
    eventLog.prepend(li);
    refresh();
  };
}

refresh();
setInterval(refresh, 1500);
