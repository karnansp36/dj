// ==============================
// 📌 DOM ELEMENTS
// ==============================
const form = document.getElementById("campaignForm");
const statusText = document.getElementById("status");
const loader = document.getElementById("loader");

const sendLoopBtn = document.getElementById("sendLoop");
const sendParallelBtn = document.getElementById("sendParallel");

// ==============================
// 🔧 CONFIG
// ==============================
const API_URL = "https://emailcon.in/api/stud/form-trigger-campaign";

const CONFIG = {
  campaignId: "qyHnurLimg6Yb4SwA5rGdlRNTfEoW4qamg4gDS6Y/beIuBBKxmGo6ARV7K5u6iYv",
  token: "f521cee0578d126ee16893501bcb1403deb3e99f1873cf2219fa4105f6c53170"
};

// ==============================
// 📦 REPEATED EMAIL LIST (20)
// ==============================
const baseEmails = [
  "reviewmaster36@gmail.com",
  "calcifersp369@gmail.com",
  "flashtech369@gmail.com",
  "megarajan55@gmail.com",
  "emailcon.01012000@gmail.com"
];

const emailList = [];

for (let i = 0; i < 100; i++) {
  emailList.push(baseEmails[i % baseEmails.length]);
}

// ==============================
// 🧠 UTILS
// ==============================
function toggleLoader(show) {
  loader.classList.toggle("hidden", !show);
}

function getFormData() {
  return {
    name: document.getElementById("name").value.trim(),
    course: document.getElementById("course").value.trim()
  };
}

// Convert email list → contacts
function buildContacts(name, course) {
  return emailList.map((email, index) => ({
    Name: `${name}${index + 1}`,
    Email: email,
    Course: course
  }));
}

// ==============================
// 📩 API CALL
// ==============================
async function sendSingle(contact) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        ...CONFIG,
        formData: contact
      })
    });

    const data = await response.json();

    return { success: response.ok, data };

  } catch (error) {
    return { success: false, error };
  }
}

// ==============================
// 🔁 LOOP METHOD (SAFE)
// ==============================
async function sendLoop(contacts) {
  statusText.innerText = "🚀 Sending (Loop)...";
  statusText.style.color = "blue";

  let successCount = 0;

  for (let i = 0; i < contacts.length; i++) {
    const res = await sendSingle(contacts[i]);

    if (res.success) {
      successCount++;
      console.log(`✅ ${contacts[i].Email}`);
    } else {
      console.error(`❌ ${contacts[i].Email}`, res);
    }

    // progress update
    statusText.innerText = `Sending ${i + 1}/20...`;

    // small delay (rate limit safety)
    await new Promise(resolve => setTimeout(resolve, 200));
  }

  statusText.innerText = `✅ Loop Done: ${successCount}/20 sent`;
  statusText.style.color = "green";
}

// ==============================
// ⚡ PARALLEL METHOD (FAST)
// ==============================
async function sendParallel(contacts) {
  statusText.innerText = "⚡ Sending (Parallel)...";
  statusText.style.color = "blue";

  const promises = contacts.map(contact => sendSingle(contact));
  const results = await Promise.all(promises);

  const successCount = results.filter(r => r.success).length;

  statusText.innerText = `⚡ Parallel Done: ${successCount}/20 sent`;
  statusText.style.color = "green";
}

// ==============================
// 🎯 SINGLE SEND
// ==============================
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const { name, course } = getFormData();

  if (!name) {
    statusText.innerText = "Name is required!";
    statusText.style.color = "red";
    return;
  }

  toggleLoader(true);

  const contact = {
    Name: name,
    Email: baseEmails[0], // send to first email
    Course: course
  };

  const res = await sendSingle(contact);

  if (res.success) {
    statusText.innerText = "✅ Email sent successfully!";
    statusText.style.color = "green";
  } else {
    statusText.innerText = "❌ Failed to send email";
    statusText.style.color = "red";
  }

  toggleLoader(false);
});

// ==============================
// 🚀 SEND LOOP BUTTON
// ==============================
sendLoopBtn.addEventListener("click", async () => {
  const { name, course } = getFormData();

  if (!name) {
    statusText.innerText = "Name is required!";
    statusText.style.color = "red";
    return;
  }

  const contacts = buildContacts(name, course);

  toggleLoader(true);
  await sendLoop(contacts);
  toggleLoader(false);
});

// ==============================
// ⚡ SEND PARALLEL BUTTON
// ==============================
sendParallelBtn.addEventListener("click", async () => {
  const { name, course } = getFormData();

  if (!name) {
    statusText.innerText = "Name is required!";
    statusText.style.color = "red";
    return;
  }

  const contacts = buildContacts(name, course);

  toggleLoader(true);
  await sendParallel(contacts);
  toggleLoader(false);
});