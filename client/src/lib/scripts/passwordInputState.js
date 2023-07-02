export const switchPassword = () => {

    const passwordInput = document.getElementById("password");

    if (passwordInput.type === "password") passwordInput.type = "text";
    else passwordInput.type = "password";

    const passwordIcon = document.getElementById("passwordIcon");

    if (passwordIcon.src.endsWith("eye-open.svg")) passwordIcon.src = "/icons/profile/eye-closed.svg";
    else passwordIcon.src = "/icons/profile/eye-open.svg";

    const passwordIconBtn = document.getElementById("passwordIconBtn");

    if (passwordIconBtn?.classList.contains("btn-primary")) passwordIconBtn.className = "btn btn-square btn-secondary";
    else passwordIconBtn.className = "btn btn-square btn-primary";

};