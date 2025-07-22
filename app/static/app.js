const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const output = document.getElementById("output");
const ctx = canvas.getContext("2d");

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
    sendFrames();
  });

const socket = new WebSocket("ws://localhost:8000/ws/hand");

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.gesture) {
    output.innerText = "Gestura detectada: " + data.gesture;
  } else if (data.error) {
    output.innerText = "Error: " + data.error;
  }
};

function sendFrames() {
  setInterval(() => {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
      if (blob && socket.readyState === WebSocket.OPEN) {
        blob.arrayBuffer().then(buffer => {
          socket.send(buffer);
        });
      }
    }, "image/jpeg");
  }, 500);  // 2 frames per second
}

function getSpeech() {
  fetch("/api/speech")
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        output.innerText = "Frase reconocida: " + data.phrase;
      } else {
        output.innerText = "No se reconoció ninguna frase.";
      }
    });
}
