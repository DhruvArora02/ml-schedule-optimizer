let tasks = [];

function addTask() {
  const t = {
    title: document.getElementById("title").value,
    duration: Number(document.getElementById("duration").value),
    deadline_hrs: Number(document.getElementById("deadline").value),
    difficulty: Number(document.getElementById("difficulty").value),
  };

  tasks.push(t);
  document.getElementById("task-list").innerHTML += `<p>${t.title}</p>`;
}

async function optimize() {
  const res = await fetch("http://localhost:5000/optimize", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tasks })
  });

  const data = await res.json();

  document.getElementById("result").innerHTML =
    data.map(t => `<p>${t.title} — stress: ${t.stress}</p>`).join("");
}
