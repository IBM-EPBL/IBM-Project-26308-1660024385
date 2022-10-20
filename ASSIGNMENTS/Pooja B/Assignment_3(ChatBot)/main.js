require("dotenv").config();

window.watsonAssistantChatOptions = {
  integrationID: process.env.integration,
  region: "jp-tok",
  serviceInstanceID: process.env.service,
  onLoad: function (instance) {
    instance.render();
  },
};
setTimeout(function () {
  const t = document.createElement("script");
  t.src =
    "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
    (window.watsonAssistantChatOptions.clientVersion || "latest") +
    "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});
