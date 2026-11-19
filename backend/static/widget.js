(function () {
  var script = document.currentScript || document.querySelector('script[data-skillbridge]');
  var API = (script && script.dataset.api) || "http://localhost:8000";
  var THEME = (script && script.dataset.theme) || "dark";
  var TITLE = (script && script.dataset.title) || "Quick Ed Assistant";
  var SUBTITLE = (script && script.dataset.subtitle) || "Online";
  var ACCENT = (script && script.dataset.accent) || "#facc15";
  var MAX = 500;

  var SUGGESTIONS = [
    "What courses do you offer?",
    "Python course fee?",
    "Next Java batch dates?",
    "Do you provide placements?"
  ];

  var host = document.createElement("div");
  host.setAttribute("data-skillbridge-widget", "");
  document.body.appendChild(host);
  var root = host.attachShadow({ mode: "open" });

  var light = THEME === "light";
  var css =
    ":host{all:initial}" +
    "*{box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif}" +
    ".fab{position:fixed;right:24px;bottom:24px;width:56px;height:56px;border-radius:50%;border:0;cursor:pointer;" +
      "background:" + ACCENT + ";display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(0,0,0,.25);" +
      "transition:transform .15s ease;z-index:2147483000}" +
    ".fab:hover{transform:scale(1.06)}" +
    ".fab svg{width:26px;height:26px;fill:#111}" +
    ".panel{position:fixed;right:24px;bottom:24px;width:380px;height:min(600px,calc(100vh - 48px));display:flex;flex-direction:column;" +
      "border-radius:16px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.35);z-index:2147483001;" +
      "background:" + (light ? "#fff" : "#0b0b0b") + ";border:1px solid " + (light ? "#e5e7eb" : "#262626") + "}" +
    ".panel[hidden]{display:none}" +
    ".head{display:flex;align-items:center;gap:10px;padding:10px 12px;border-bottom:1px solid " + (light ? "#eee" : "rgba(250,204,21,.35)") + ";" +
      "background:" + (light ? "#fff" : "#000") + "}" +
    ".logo{width:38px;height:38px;border-radius:50%;background:" + ACCENT + ";color:#111;font-weight:800;font-size:13px;" +
      "display:flex;align-items:center;justify-content:center;flex:0 0 auto}" +
    ".who{flex:1;min-width:0}" +
    ".name{font-size:15px;font-weight:600;color:" + (light ? "#111827" : "#fff") + ";white-space:nowrap;overflow:hidden;text-overflow:ellipsis}" +
    ".status{font-size:12px;color:" + (light ? "#16a34a" : ACCENT) + "}" +
    ".icon-btn{background:transparent;border:0;cursor:pointer;width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;color:" + (light ? "#4b5563" : "#9ca3af") + "}" +
    ".icon-btn:hover{background:" + (light ? "#f3f4f6" : "#1a1a1a") + "}" +
    ".icon-btn svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}" +
    ".body{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}" +
    ".msg{max-width:85%;padding:9px 12px;border-radius:16px;font-size:14px;line-height:1.45;white-space:pre-wrap;word-wrap:break-word}" +
    ".bot{align-self:flex-start;background:" + (light ? "#f1f5f9" : "#1f1f1f") + ";color:" + (light ? "#111827" : "#f3f4f6") + ";border-bottom-left-radius:4px}" +
    ".user{align-self:flex-end;background:" + ACCENT + ";color:#111;border-bottom-right-radius:4px}" +
    ".chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:2px}" +
    ".chip{font-size:12px;padding:6px 11px;border-radius:999px;cursor:pointer;background:transparent;" +
      "border:1px solid " + (light ? "#d1d5db" : "rgba(250,204,21,.55)") + ";color:" + (light ? "#374151" : ACCENT) + "}" +
    ".chip:hover{background:" + ACCENT + ";color:#111;border-color:" + ACCENT + "}" +
    ".dots{align-self:flex-start;background:" + (light ? "#f1f5f9" : "#1f1f1f") + ";border-radius:16px;padding:12px 14px;display:flex;gap:4px}" +
    ".dots i{width:7px;height:7px;border-radius:50%;background:" + (light ? "#94a3b8" : ACCENT) + ";animation:b 1s infinite}" +
    ".dots i:nth-child(2){animation-delay:.15s}.dots i:nth-child(3){animation-delay:.3s}" +
    "@keyframes b{0%,80%,100%{opacity:.3;transform:translateY(0)}40%{opacity:1;transform:translateY(-3px)}}" +
    ".foot{border-top:1px solid " + (light ? "#eee" : "#1f1f1f") + ";padding:10px 12px 8px;background:" + (light ? "#fff" : "#000") + "}" +
    ".row{display:flex;align-items:flex-end;gap:8px}" +
    ".input{flex:1;resize:none;max-height:96px;border-radius:14px;padding:10px 12px;font-size:14px;line-height:1.4;outline:none;" +
      "background:" + (light ? "#fff" : "#141414") + ";color:" + (light ? "#111827" : "#f9fafb") + ";border:1px solid " + (light ? "#d1d5db" : "#333") + "}" +
    ".input:focus{border-color:" + ACCENT + "}" +
    ".send{width:38px;height:38px;border-radius:50%;border:0;cursor:pointer;background:" + ACCENT + ";display:flex;align-items:center;justify-content:center;flex:0 0 auto}" +
    ".send:disabled{opacity:.4;cursor:default}" +
    ".send svg{width:18px;height:18px;fill:#111}" +
    ".count{font-size:11px;color:" + (light ? "#9ca3af" : "#6b7280") + ";text-align:right;margin-top:4px}" +
    "@media(max-width:480px){.panel{right:0;bottom:0;width:100%;height:100%;border-radius:0}.fab{right:16px;bottom:16px}}";

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  var style = el("style");
  style.textContent = css;
  root.appendChild(style);

  var fab = el("button", "fab", '<svg viewBox="0 0 24 24"><path d="M12 3C6.9 3 3 6.4 3 10.6c0 2.3 1.2 4.3 3.2 5.7-.2 1.2-.8 2.3-1.7 3.2-.2.2 0 .6.3.6 2 0 3.7-.7 5-1.7 1 .3 2.1.4 3.2.4 5.1 0 9-3.4 9-7.6S17.1 3 12 3z"/></svg>');
  fab.setAttribute("aria-label", "Open chat");
  fab.setAttribute("aria-expanded", "false");
  root.appendChild(fab);

  var panel = el("div", "panel");
  panel.hidden = true;
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", TITLE);
  panel.innerHTML =
    '<div class="head">' +
      '<div class="logo">SB</div>' +
      '<div class="who"><div class="name"></div><div class="status"></div></div>' +
      '<button class="icon-btn min" aria-label="Minimize"><svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></button>' +
      '<button class="icon-btn close" aria-label="Close"><svg viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg></button>' +
    "</div>" +
    '<div class="body" role="log" aria-live="polite"></div>' +
    '<div class="foot">' +
      '<div class="row">' +
        '<textarea class="input" rows="1" maxlength="' + MAX + '" placeholder="Type your question..."></textarea>' +
        '<button class="send" aria-label="Send" disabled><svg viewBox="0 0 24 24"><path d="M3.4 20.4l17.5-8.4L3.4 3.6l.1 6.6L15 12 3.5 13.8z"/></svg></button>' +
      "</div>" +
      '<div class="count">0 / ' + MAX + "</div>" +
    "</div>";
  root.appendChild(panel);

  panel.querySelector(".name").textContent = TITLE;
  panel.querySelector(".status").textContent = SUBTITLE;
  var body = panel.querySelector(".body");
  var input = panel.querySelector(".input");
  var sendBtn = panel.querySelector(".send");
  var count = panel.querySelector(".count");

  var history = [];
  var busy = false;
  var greeted = false;

  function toggle(open) {
    panel.hidden = !open;
    fab.style.display = open ? "none" : "flex";
    fab.setAttribute("aria-expanded", String(open));
    if (open) {
      if (!greeted) {
        add("bot", "Hi! I'm the " + TITLE + ". Ask me about courses, fees, batches, trainers, projects or placement support.");
        addChips();
        greeted = true;
      }
      input.focus();
    }
  }

  function add(role, text) {
    var m = el("div", "msg " + role);
    m.textContent = text;
    body.appendChild(m);
    body.scrollTop = body.scrollHeight;
    return m;
  }

  function addChips() {
    var chips = el("div", "chips");
    SUGGESTIONS.forEach(function (s) {
      var c = el("button", "chip", s);
      c.addEventListener("click", function () {
        chips.remove();
        send(s);
      });
      chips.appendChild(c);
    });
    body.appendChild(chips);
  }

  function typing(on) {
    var t = body.querySelector(".dots");
    if (on && !t) {
      var d = el("div", "dots", "<i></i><i></i><i></i>");
      body.appendChild(d);
      body.scrollTop = body.scrollHeight;
    } else if (!on && t) {
      t.remove();
    }
  }

  function ask(msg) {
    busy = true;
    sendBtn.disabled = true;
    typing(true);
    var payload = { message: msg, history: history.slice(-6) };
    fetch(API + "/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status === 429 ? "Too many requests. Please wait a minute." : "Server error");
        return r.json();
      })
      .then(function (d) {
        typing(false);
        add("bot", d.answer);
        history.push({ role: "user", content: msg }, { role: "assistant", content: d.answer });
      })
      .catch(function (e) {
        typing(false);
        add("bot", e.message || "Something went wrong. Please try again.");
      })
      .finally(function () {
        busy = false;
        sendBtn.disabled = !input.value.trim();
      });
  }

  function send(text) {
    var msg = (text || input.value).trim();
    if (!msg || busy) return;
    if (body.querySelector(".chips")) body.querySelector(".chips").remove();
    add("user", msg);
    input.value = "";
    input.style.height = "auto";
    count.textContent = "0 / " + MAX;
    ask(msg);
  }

  fab.addEventListener("click", function () { toggle(true); });
  panel.querySelector(".close").addEventListener("click", function () { toggle(false); });
  panel.querySelector(".min").addEventListener("click", function () { toggle(false); });
  sendBtn.addEventListener("click", function () { send(); });

  input.addEventListener("input", function () {
    count.textContent = input.value.length + " / " + MAX;
    sendBtn.disabled = !input.value.trim() || busy;
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 96) + "px";
  });

  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  });
})();
