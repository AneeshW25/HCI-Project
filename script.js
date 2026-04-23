let slides = [];
let current = 0;

console.log("JS LOADED");

async function upload() {
    const file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Select a PPT file first");
        return;
    }

    // 🔥 SHOW MESSAGE IMMEDIATELY
    document.getElementById("explanation").innerText = " Starting presentation...";
    
    let formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData
        });

        // 🔥 UPDATE MESSAGE WHILE PROCESSING
        document.getElementById("explanation").innerText = "⏳ Preparing slides and narration...";

        const data = await res.json();

        slides = data.data;

        if (!slides || slides.length === 0) {
            alert("No slides generated");
            return;
        }

        // 🔥 START PRESENTATION
        playSlide(0);

    } catch (err) {
        console.error(err);
        alert("Error connecting to backend");
    }
}

function playSlide(index) {
    if (index >= slides.length) {
        alert("Presentation finished");
        return;
    }

    current = index;

    let slide = slides[index];

    let img = document.getElementById("slideImage");
    let text = document.getElementById("explanation");
    let audio = document.getElementById("audioPlayer");

    let imgUrl = "http://127.0.0.1:8000/static/" + slide.image;
    let audioUrl = "http://127.0.0.1:8000/static/" + slide.audio;

    console.log("Image:", imgUrl);
    console.log("Audio:", audioUrl);

    img.src = imgUrl;
    text.innerText = slide.explanation;

    audio.src = audioUrl;

    audio.play().catch(() => {});

    audio.onended = () => {
        playSlide(current + 1);
    };
}