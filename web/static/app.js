const statusLine = document.getElementById("status-line");
const agentsEl = document.getElementById("agents");
const statsEl = document.getElementById("stats");
const eventLog = document.getElementById("event-log");
const form = document.getElementById("config-form");

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
  statusLine.textContent = `Status: ${snapshot.status} · loop ${snapshot.loop || 0}`;

  const isRunning = snapshot.status === "running";
  document.getElementById("start-btn").disabled = isRunning;
  document.getElementById("stop-btn").disabled = !isRunning;

  const agents = snapshot.agents || [];
  if (agents.length === 0) {
    agentsEl.innerHTML = `<p class="status" style="grid-column: 1 / -1; margin-top: 0;">No agents running. Click "Start" to begin.</p>`;
  } else {
    agentsEl.innerHTML = agents
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
  const res = await fetch("/api/simulation/start", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formPayload()),
  });
  const data = await res.json();
  if (!res.ok) {
    statusLine.textContent = `Error: ${data.detail || res.statusText}`;
    return;
  }
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
