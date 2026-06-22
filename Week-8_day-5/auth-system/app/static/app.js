const apiBase = "/admin";
const resultOutput = document.getElementById("result-output");

async function fetchUsers() {
  try {
    const response = await fetch(`${apiBase}/users`);
    const users = await response.json();
    const tableBody = document.getElementById("user-table-body");
    tableBody.innerHTML = "";

    users.forEach((user) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${user.id}</td>
        <td>${user.username}</td>
        <td>${user.email}</td>
        <td><span class="status">${user.is_active ? "Active" : "Inactive"}</span></td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    setResult(`Error loading users: ${error.message}`);
  }
}

async function assignRole() {
  const userId = Number(document.getElementById("assign-role-user").value);
  const roleId = Number(document.getElementById("assign-role-role").value);
  const payload = { user_id: userId, role_id: roleId };

  await postAction("assign-role", payload);
}

async function assignPermission() {
  const roleId = Number(document.getElementById("assign-permission-role").value);
  const permissionId = Number(document.getElementById("assign-permission-permission").value);
  const assignToUserId = document.getElementById("assign-permission-user").value;
  const payload = {
    role_id: roleId,
    permission_id: permissionId,
    assign_to_user_id: assignToUserId ? Number(assignToUserId) : null,
  };

  await postAction("assign-permission", payload);
}

async function postAction(route, payload) {
  try {
    const response = await fetch(`${apiBase}/${route}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || JSON.stringify(data));
    }

    setResult(JSON.stringify(data, null, 2));
  } catch (error) {
    setResult(`Request failed: ${error.message}`);
  }
}

function setResult(value) {
  resultOutput.textContent = value;
}

window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("fetch-users").addEventListener("click", fetchUsers);
  document.getElementById("role-submit").addEventListener("click", assignRole);
  document.getElementById("permission-submit").addEventListener("click", assignPermission);
  // auth handlers
  const registerBtn = document.getElementById("register-submit");
  if (registerBtn) registerBtn.addEventListener("click", registerUser);

  const loginBtn = document.getElementById("login-submit");
  if (loginBtn) loginBtn.addEventListener("click", loginUser);

  const changeBtn = document.getElementById("change-submit");
  if (changeBtn) changeBtn.addEventListener("click", changePassword);

  const meBtn = document.getElementById("me-button");
  if (meBtn) meBtn.addEventListener("click", getCurrentUser);
  fetchUsers();
});


let authToken = null;

async function registerUser() {
  const username = document.getElementById("register-username").value;
  const email = document.getElementById("register-email").value;
  const password = document.getElementById("register-password").value;

  try {
    const resp = await fetch("/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password }),
    });
    const data = await resp.json();
    if (!resp.ok) throw new Error(data.detail || JSON.stringify(data));
    setResult(JSON.stringify(data, null, 2));
  } catch (err) {
    setResult(`Request failed: ${err.message}`);
  }
}

async function loginUser() {
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  try {
    const resp = await fetch("/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await resp.json();
    if (!resp.ok) throw new Error(data.detail || JSON.stringify(data));
    authToken = data.access_token;
    setResult(JSON.stringify(data, null, 2));
  } catch (err) {
    setResult(`Request failed: ${err.message}`);
  }
}

async function changePassword() {
  const old_password = document.getElementById("change-old").value;
  const new_password = document.getElementById("change-new").value;
  if (!authToken) {
    setResult("You must be logged in to change password.");
    return;
  }

  try {
    const resp = await fetch("/auth/change-password", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${authToken}` },
      body: JSON.stringify({ old_password, new_password }),
    });
    const data = await resp.json();
    if (!resp.ok) throw new Error(data.detail || JSON.stringify(data));
    setResult(JSON.stringify(data, null, 2));
  } catch (err) {
    setResult(`Request failed: ${err.message}`);
  }
}

async function getCurrentUser() {
  if (!authToken) {
    setResult("Not logged in");
    return;
  }
  try {
    const response = await fetch("/auth/me", { headers: { Authorization: `Bearer ${authToken}` } });
    const data = await response.json();
    setResult(JSON.stringify(data, null, 2));
  } catch (err) {
    setResult(`Request failed: ${err.message}`);
  }
}
