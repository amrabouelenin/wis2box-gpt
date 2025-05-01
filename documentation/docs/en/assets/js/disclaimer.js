document.addEventListener("DOMContentLoaded", function () {
  const lang = window.location.pathname.split("/")[1];
  const defaultLang = "en"; // Change if your default is different

  if (
    lang !== defaultLang &&
    !localStorage.getItem("translationDisclaimerShown")
  ) {
    const disclaimer = document.createElement("div");
    disclaimer.style.position = "fixed";
    disclaimer.style.bottom = "20px";
    disclaimer.style.left = "20px";
    disclaimer.style.right = "20px";
    disclaimer.style.padding = "1em";
    disclaimer.style.backgroundColor = "#f9edbe";
    disclaimer.style.border = "1px solid #f0c36d";
    disclaimer.style.borderRadius = "8px";
    disclaimer.style.boxShadow = "0 2px 5px rgba(0,0,0,0.2)";
    disclaimer.style.zIndex = "1000";
    disclaimer.innerHTML = `
        <strong>Disclaimer:</strong> This translation was generated using an AI model (ChatGPT). While we strive for accuracy, there may be errors or inconsistencies. For authoritative information, please refer to the original English version.
        <button style="margin-left: 1em;" onclick="this.parentElement.remove(); localStorage.setItem('translationDisclaimerShown', 'true')">Dismiss</button>
      `;
    document.body.appendChild(disclaimer);
  }
});
