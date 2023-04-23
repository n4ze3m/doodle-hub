inputUrl = document.getElementById("share-url");
btn = document.getElementById("cpy-btn");


if (inputUrl && btn) {
    btn.addEventListener("click", function () {
        inputUrl.select();
        document.execCommand("copy");
        alert("Copied the text: " + inputUrl.value);
    });
}