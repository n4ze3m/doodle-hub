inputUrl = document.getElementById("share-url");
btn = document.getElementById("cpy-btn");
btnEmpty = document.getElementById("cpy-btn-empty");


if (inputUrl && btn) {
    btn.addEventListener("click", function () {
        inputUrl.select();
        document.execCommand("copy");
        alert("Copied the text: " + inputUrl.value);
    });
}

if (btnEmpty && inputUrl) {
    btnEmpty.addEventListener("click", function () {
        inputUrl.select();
        document.execCommand("copy");
        alert("Copied the text: " + inputUrl.value);
    });
}



function shareImage(data) {
    const xData = data.getAttribute('x-data')
    fetch(xData).then((response) => {
        return response.blob();
    }).then((blob) => {
        let shareData = {
            title: 'Doodle',
            text: 'Check out my doodle!',
            files: [new File([blob], "lol.png", { type: "image/png" })],

        }
        navigator.share(shareData)
            .then(() => console.log('Share was successful.'))
            .catch((error) => console.log('Sharing failed', error));
    });
}


function downloadImage(data) {
    const xData = data.getAttribute('x-data')
    fetch(xData).then((response) => {
        return response.blob();
    }).then((blob) => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'doodle.png';
        document.body.appendChild(a);
        a.click();
        a.remove();
    });
}