import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Anniversary, Bunga ❤️</title>

<style>
* {
    box-sizing: border-box;
}

:root {
    --pink: #ff6f9f;
    --pink-dark: #e94f83;
    --soft-pink: #fff0f5;
    --text: #593c49;
    --white: #ffffff;
}

body {
    margin: 0;
    font-family: "Segoe UI", Arial, sans-serif;
    color: var(--text);
    background: linear-gradient(135deg, #fff0f5, #ffe0eb, #fff8fa);
    overflow-x: hidden;
}

header {
    text-align: center;
    padding: 55px 18px 35px;
}

header h1 {
    font-size: clamp(2rem, 7vw, 3.5rem);
    color: var(--pink-dark);
    margin-bottom: 12px;
}

header p {
    font-size: 1.05rem;
    line-height: 1.8;
    max-width: 650px;
    margin: auto;
}

.heart {
    display: inline-block;
    animation: heartbeat 1.3s infinite;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

.container {
    width: min(900px, 92%);
    margin: 0 auto 35px;
}

.card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 22px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(190, 83, 120, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.9);
}

h2 {
    color: var(--pink-dark);
    text-align: center;
    margin-top: 0;
}

.timer {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-top: 22px;
}

.time-box {
    padding: 18px 5px;
    border-radius: 16px;
    background: var(--soft-pink);
    text-align: center;
}

.time-box strong {
    display: block;
    font-size: clamp(1.3rem, 5vw, 2rem);
    color: var(--pink-dark);
}

.time-box span {
    font-size: 0.85rem;
}

.letter {
    line-height: 2;
    white-space: pre-line;
    font-size: 1.02rem;
}

button {
    border: none;
    padding: 12px 20px;
    margin: 5px;
    border-radius: 25px;
    background: var(--pink);
    color: white;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: 0.2s;
}

button:hover {
    background: var(--pink-dark);
    transform: translateY(-2px);
}

button:focus-visible {
    outline: 3px solid #b72c65;
    outline-offset: 3px;
}

.button-row {
    text-align: center;
    margin-top: 18px;
}

.slide {
    display: none;
    min-height: 190px;
    padding: 15px 5px;
    text-align: center;
    animation: fadeIn 0.4s ease;
}

.slide.active {
    display: block;
}

.slide h3 {
    color: var(--pink-dark);
    font-size: 1.35rem;
}

.slide p {
    line-height: 1.9;
    max-width: 650px;
    margin: 15px auto;
    white-space: pre-line;
}

.dots {
    text-align: center;
    margin: 12px 0;
}

.dot {
    width: 11px;
    height: 11px;
    padding: 0;
    margin: 4px;
    border-radius: 50%;
    background: #f4bfd1;
}

.dot.active {
    background: var(--pink-dark);
}

.question-card {
    padding: 18px;
    background: #fff7fa;
    border-radius: 16px;
    margin-top: 15px;
    text-align: center;
}

.question-card h3 {
    line-height: 1.6;
}

.answers {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 5px;
}

.response {
    min-height: 45px;
    line-height: 1.8;
    margin-top: 15px;
    color: var(--pink-dark);
    font-weight: 600;
}

.progress {
    color: #a16c80;
    font-size: 0.9rem;
    text-align: center;
}

.gallery {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}

.photo-card {
    overflow: hidden;
    border-radius: 18px;
    background: white;
    box-shadow: 0 5px 18px rgba(190, 83, 120, 0.12);
}

.photo-card img {
    display: block;
    width: 100%;
    height: 260px;
    object-fit: cover;
    background: #ffe4ed;
}

.caption {
    padding: 15px;
    line-height: 1.7;
    font-size: 0.95rem;
    text-align: center;
}

.surprise {
    display: none;
    text-align: center;
    background: #fff0f6;
    padding: 24px;
    margin-top: 18px;
    border-radius: 18px;
    line-height: 1.9;
    white-space: pre-line;
    animation: fadeIn 0.5s ease;
}

.surprise.show {
    display: block;
}

footer {
    text-align: center;
    padding: 20px;
    line-height: 1.8;
    color: #98677b;
}

.floating-heart {
    position: fixed;
    bottom: -30px;
    z-index: -1;
    pointer-events: none;
    animation: floatUp 8s linear forwards;
    opacity: 0.55;
}

@keyframes floatUp {
    from {
        transform: translateY(0) rotate(0deg);
        opacity: 0.6;
    }
    to {
        transform: translateY(-110vh) rotate(35deg);
        opacity: 0;
    }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(7px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 560px) {
    .card {
        padding: 20px 16px;
    }

    .gallery {
        grid-template-columns: 1fr;
    }

    .photo-card img {
        height: 300px;
    }

    .timer {
        gap: 6px;
    }

    .time-box {
        padding: 14px 3px;
    }

    .time-box span {
        font-size: 0.75rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>

<body>

<header>
    <h1>Happy Anniversary, Bunga <span class="heart">❤️</span></h1>
    <p>
        Buat Bunga Yaumil Khairiyah, orang yang punya tempat spesial
        di hati aku. Aku bikin halaman kecil ini khusus buat kamu. 🥹💕
    </p>
</header>

<main class="container">

    <section class="card">
        <h2>Sejak Hari Kita Bersama 💗</h2>
        <p style="text-align:center; line-height:1.8">
            Dari tanggal 26 Oktober 2025 sampai hari ini,
            kita sudah punya banyak cerita.
        </p>

        <div class="timer">
            <div class="time-box">
                <strong id="days">0</strong>
                <span>Hari</span>
            </div>
            <div class="time-box">
                <strong id="hours">0</strong>
                <span>Jam</span>
            </div>
            <div class="time-box">
                <strong id="minutes">0</strong>
                <span>Menit</span>
            </div>
            <div class="time-box">
                <strong id="seconds">0</strong>
                <span>Detik</span>
            </div>
        </div>
    </section>

    <section class="card">
        <h2>Ada Sedikit Pesan Buat Kamu 💌</h2>

        <p class="letter">Sayang, happy anniversary yaa ❤️

Nggak kerasa kita sudah sampai di hari ini. Aku senang banget bisa kenal kamu dan punya kesempatan buat jalanin hubungan ini sama kamu.

Makasih ya sudah hadir di hidup aku. Makasih buat perhatian kamu, waktu yang kamu luangin, cerita-cerita kecil kita, dan hal sederhana yang kadang bikin hari aku jadi lebih baik.

Aku tahu aku belum sempurna. Kadang mungkin aku bikin kamu kesal, kurang peka, atau belum bisa jadi seperti yang kamu harapkan. Kalau ada sikap aku yang bikin kamu sedih, aku minta maaf ya, sayang. Aku masih belajar buat jadi pasangan yang lebih baik buat kamu.

Aku nggak bisa janji kalau semuanya bakal selalu mudah. Tapi aku mau kita sama-sama belajar, saling ngerti, saling jaga, dan nggak gampang nyerah waktu ada masalah.

Semoga kita masih punya banyak waktu buat bikin kenangan baru, ketawa bareng, cerita tentang hari kita, dan saling nemenin saat salah satu dari kita lagi nggak baik-baik aja.

Pokoknya, aku senang kamu ada di sini. Aku sayang kamu, Bunga. Hari ini, besok, dan semoga di banyak hari setelahnya juga. ❤️

Happy anniversary, sayangku. 🥹🌷</p>
    </section>

    <section class="card">
        <h2>Kalau Aku Boleh Cerita... 💕</h2>

        <div class="slideshow">
            <div class="slide active">
                <h3>Aku Senang Kenal Kamu</h3>
                <p>Aku nggak tahu semua hal bakal berjalan seperti apa ke depannya, tapi aku bersyukur karena salah satu cerita hidupku ada kamu di dalamnya. Kenal kamu jadi hal yang berarti buat aku. ❤️</p>
            </div>

            <div class="slide">
                <h3>Kalau Aku Lagi Kangen</h3>
                <p>Kadang aku kangen cuma karena hal kecil. Pengin ngobrol sama kamu, denger cerita kamu, atau sekadar tahu kamu hari ini baik-baik aja. Sesederhana itu, tapi berarti buat aku. 🥹</p>
            </div>

            <div class="slide">
                <h3>Maaf Kalau Aku Masih Banyak Kurang</h3>
                <p>Aku sadar aku masih punya banyak kekurangan. Kalau suatu saat aku bikin kamu kecewa, semoga kita bisa ngobrol baik-baik, ya. Aku pengin terus belajar memahami kamu, bukan cuma berharap kamu memahami aku. ❤️</p>
            </div>

            <div class="slide">
                <h3>Semoga Kita Terus Sama-Sama</h3>
                <p>Aku berharap kita bisa terus tumbuh bareng. Bukan berarti nggak akan pernah ada masalah, tapi semoga kita selalu punya alasan buat saling mendengarkan dan memperbaiki semuanya bersama. 🌷</p>
            </div>

            <div class="slide">
                <h3>Buat Kamu, Bunga</h3>
                <p>Terima kasih sudah jadi bagian dari hari-hari aku. Aku mungkin nggak selalu pandai merangkai kata, tapi aku harap kamu bisa merasakan kalau kamu memang berarti buat aku. Happy anniversary, sayang. 💗</p>
            </div>
        </div>

        <div class="dots" id="slideDots"></div>

        <div class="button-row">
            <button onclick="changeSlide(-1)">← Sebelumnya</button>
            <button onclick="changeSlide(1)">Selanjutnya →</button>
        </div>
    </section>

    <section class="card">
        <h2>Aku Mau Tanya Sesuatu Nih 🥺</h2>
        <p style="text-align:center; line-height:1.8">
            Jawab yang jujur yaa, jangan asal pencet. Hehe. ❤️
        </p>

        <div id="questionArea"></div>

        <p class="progress" id="questionProgress"></p>

        <div class="button-row">
            <button id="restartQuestions" onclick="restartQuestions()" style="display:none">
                Jawab Lagi 💗
            </button>
        </div>
    </section>

    <section class="card">
        <h2>Beberapa Kenangan Kita 📸</h2>
        <p style="text-align:center; line-height:1.8">
            Ada foto yang mungkin sederhana, tapi tetap punya cerita
            tersendiri buat aku. ❤️
        </p>

        <div class="gallery">
            <div class="photo-card">
                <img src="/static/foto_1.jpeg" alt="Kenangan pertama" loading="lazy">
                <div class="caption">
                    Suka banget lihat senyum kamu di foto ini.
                    Semoga kamu selalu punya alasan buat senyum, yaa. ❤️
                </div>
            </div>

            <div class="photo-card">
                <img src="/static/foto_2.jpeg" alt="Kenangan kedua" loading="lazy">
                <div class="caption">
                    Kalau diingat-ingat, hal sederhana bareng kamu aja
                    bisa jadi kenangan yang bikin aku senyum sendiri. 🥰
                </div>
            </div>

            <div class="photo-card">
                <img src="/static/foto_3.jpeg" alt="Kenangan ketiga" loading="lazy">
                <div class="caption">
                    Aku senang punya cerita sama kamu.
                    Semoga nanti kita punya lebih banyak momen yang bisa dikenang. 💕
                </div>
            </div>

            <div class="photo-card">
                <img src="/static/foto_4.jpeg" alt="Kenangan keempat" loading="lazy">
                <div class="caption">
                    Foto ini mungkin sederhana, tapi tetap punya cerita sendiri
                    buat aku. Apalagi karena ada kamu di dalamnya. 🥹
                </div>
            </div>

            <div class="photo-card">
                <img src="/static/foto_5.jpeg" alt="Kenangan kelima" loading="lazy">
                <div class="caption">
                    Semoga kita nggak cuma punya foto buat dikenang,
                    tapi juga banyak cerita indah yang bisa kita lewati bareng. 🌷
                </div>
            </div>

            <div class="photo-card">
                <img src="/static/foto_6.jpeg" alt="Kenangan keenam" loading="lazy">
                <div class="caption">
                    Kalau ditanya apa harapan aku, sederhana kok:
                    semoga kita masih bisa saling memilih dan saling menjaga. ❤️
                </div>
            </div>
        </div>
    </section>

    <section class="card">
        <h2>Terakhir, Ada Sesuatu Buat Kamu 🎁</h2>
        <p style="text-align:center; line-height:1.8">
            Coba pencet tombol di bawah ini, sayang.
            Ada pesan kecil yang belum aku bilang. 🥹
        </p>

        <div class="button-row">
            <button onclick="showSurprise()">Buka Pesan Rahasia ❤️</button>
        </div>

        <div class="surprise" id="surprise">
            Sayanggg ❤️🥹

            Happy anniversary, Bunga.

            Aku cuma mau bilang kalau aku senang punya kamu.
            Makasih sudah hadir dan jadi bagian dari cerita aku.

            Aku harap kamu selalu sehat, bahagia, dan dikelilingi
            hal-hal baik. Kalau nanti ada hari yang berat,
            semoga kamu ingat kalau kamu nggak harus menghadapi
            semuanya sendirian.

            Aku juga masih belajar jadi pasangan yang lebih baik.
            Semoga kita bisa terus saling ngerti, saling jaga,
            dan bikin banyak kenangan yang nantinya bisa kita
            ceritain sambil ketawa bareng.

            Aku sayang kamu, Bunga.
            Jangan lupa bahagia, yaa.
            Kalau bisa, salah satu alasan kamu bahagia itu aku. ❤️🌷
        </div>
    </section>

</main>

<footer>
    Dibuat dengan sepenuh hati, khusus buat Bunga. ❤️<br>
    Semoga kita punya lebih banyak cerita indah ke depannya. 🌷
</footer>

<script>
// TIMER ANNIVERSARY (Bulan di JavaScript: 0 = Jan, ..., 9 = Okt)
const anniversaryDate = new Date(2025, 9, 26, 0, 0, 0);

function updateTimer() {
    const now = new Date();
    let diff = now.getTime() - anniversaryDate.getTime();

    if (diff < 0) diff = 0;

    const totalSeconds = Math.floor(diff / 1000);
    const days = Math.floor(totalSeconds / 86400);
    const hours = Math.floor((totalSeconds % 86400) / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    document.getElementById("days").textContent = days;
    document.getElementById("hours").textContent = hours;
    document.getElementById("minutes").textContent = minutes;
    document.getElementById("seconds").textContent = seconds;
}

updateTimer();
setInterval(updateTimer, 1000);


// SLIDESHOW
const slides = document.querySelectorAll(".slide");
const dotsContainer = document.getElementById("slideDots");
let currentSlide = 0;

slides.forEach((slide, index) => {
    const dot = document.createElement("button");
    dot.className = "dot" + (index === 0 ? " active" : "");
    dot.setAttribute("aria-label", "Buka slide " + (index + 1));
    dot.onclick = () => showSlide(index);
    dotsContainer.appendChild(dot);
});

function showSlide(index) {
    currentSlide = (index + slides.length) % slides.length;

    slides.forEach((slide, i) => {
        slide.classList.toggle("active", i === currentSlide);
    });

    document.querySelectorAll(".dot").forEach((dot, i) => {
        dot.classList.toggle("active", i === currentSlide);
    });
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}


// PERTANYAAN INTERAKTIF
const questions = [
    {
        question: "Kamu senang nggak kita bisa sampai di hari ini? 🥹",
        answers: [
            {
                text: "Senang banget ❤️",
                response: "Aku juga senang banget. Semoga masih banyak hari bahagia yang bisa kita rayakan bareng, yaa. ❤️"
            },
            {
                text: "Senang dong 🥰",
                response: "Hehe, sini peluk virtual dulu! Makasih sudah jadi bagian dari cerita aku. 🤗"
            }
        ]
    },
    {
        question: "Kalau aku lagi kangen, kamu mau aku gangguin nggak? 🤭",
        answers: [
            {
                text: "Boleh dong",
                response: "Oke, nanti jangan heran kalau aku tiba-tiba nyariin kamu. Soalnya kadang kangen datang tanpa aba-aba. 😂❤️"
            },
            {
                text: "Asal jangan pas sibuk 😆",
                response: "Siap, Bu Bos! Aku tunggu waktu kamu senggang. Yang penting jangan lupa kabarin aku, yaa. 🥰"
            }
        ]
    },
    {
        question: "Kalau kita lagi ada masalah, kamu maunya gimana? 💗",
        answers: [
            {
                text: "Ngobrol baik-baik",
                response: "Aku juga mau begitu. Kita mungkin nggak selalu sepemikiran, tapi aku pengin kita tetap saling dengerin dan cari jalan keluarnya bareng. ❤️"
            },
            {
                text: "Kasih waktu buat tenang",
                response: "Iya, kita boleh tenang dulu kalau lagi emosi. Nanti kalau sudah siap, kita ngobrol lagi baik-baik, ya. 🫶"
            }
        ]
    },
    {
        question: "Apa harapan kamu buat hubungan kita? 🌷",
        answers: [
            {
                text: "Semoga langgeng",
                response: "Aamiin. Aku juga berharap begitu. Semoga kita bukan cuma bertahan, tapi juga terus belajar jadi lebih baik buat satu sama lain. ❤️"
            },
            {
                text: "Bahagia terus",
                response: "Aku juga pengin kita bahagia. Kalau ada hari yang nggak mudah, semoga kita tetap bisa saling menguatkan. 🥹"
            }
        ]
    },
    {
        question: "Terakhir nih, kamu sayang aku nggak? 😚",
        answers: [
            {
                text: "Sayang banget ❤️",
                response: "Aduh, sini peluk dulu! Aku juga sayang kamu, Bunga. Makasih ya sudah hadir di hidup aku. ❤️🥹"
            },
            {
                text: "Rahasiaaa 🤭",
                response: "Yah, malah bikin penasaran. Hehe, nggak apa-apa, nanti aku tanya langsung aja. 😆💕"
            }
        ]
    }
];

let currentQuestion = 0;

function renderQuestion() {
    const area = document.getElementById("questionArea");
    const progress = document.getElementById("questionProgress");
    const restart = document.getElementById("restartQuestions");

    if (currentQuestion >= questions.length) {
        area.innerHTML = `
            <div class="question-card">
                <h3>Yeay, pertanyaannya sudah selesai! 💗</h3>
                <p>Makasih ya sudah jawab. Semoga kita bisa terus saling
                memahami dan bikin banyak kenangan indah bareng.</p>
                <p><strong>Happy anniversary, Bunga! ❤️</strong></p>
            </div>
        `;

        progress.textContent = "Kamu sudah menjawab semua pertanyaan 🥰";
        restart.style.display = "inline-block";
        return;
    }

    const item = questions[currentQuestion];

    area.innerHTML = `
        <div class="question-card">
            <h3>${item.question}</h3>
            <div class="answers">
                ${item.answers.map((answer, index) => `
                    <button onclick="answerQuestion(${index})">
                        ${answer.text}
                    </button>
                `).join("")}
            </div>
            <div class="response" id="answerResponse" aria-live="polite"></div>
        </div>
    `;

    progress.textContent =
        `Pertanyaan ${currentQuestion + 1} dari ${questions.length}`;

    restart.style.display = "none";
}

function answerQuestion(answerIndex) {
    const item = questions[currentQuestion];
    const response = item.answers[answerIndex].response;
    const responseBox = document.getElementById("answerResponse");
    const buttons = document.querySelectorAll("#questionArea .answers button");

    buttons.forEach(button => button.disabled = true);
    responseBox.textContent = response;

    const nextButton = document.createElement("button");
    nextButton.textContent =
        currentQuestion === questions.length - 1
            ? "Selesai ❤️"
            : "Lanjut →";

    nextButton.onclick = () => {
        currentQuestion++;
        renderQuestion();
    };

    responseBox.appendChild(document.createElement("br"));
    responseBox.appendChild(nextButton);
}

function restartQuestions() {
    currentQuestion = 0;
    renderQuestion();
}

renderQuestion();


// PESAN KEJUTAN
function showSurprise() {
    const surprise = document.getElementById("surprise");
    surprise.classList.add("show");
    surprise.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}


// HATI-HATI KECIL YANG MELAYANG
function createFloatingHeart() {
    const heart = document.createElement("div");
    heart.className = "floating-heart";
    heart.textContent = ["❤️", "💕", "💗", "🌷"][
        Math.floor(Math.random() * 4)
    ];

    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (15 + Math.random() * 18) + "px";
    heart.style.animationDuration = (6 + Math.random() * 4) + "s";

    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 10000);
}

setInterval(createFloatingHeart, 1000);
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    # Mengambil port dari environment variable (Render) atau menggunakan 5000 jika lokal
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)