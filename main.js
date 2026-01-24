import { Movement } from './js/movement.js';
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
canvas.height = canvas.width*(9/16);
canvas.width = canvas.width;

const head = new Movement({
    position: {
        x: canvas.width/2,
        y: canvas.height/2,
        z: 0
    },
    limits: {x: 100, y: 100}
})
const body = new Movement({
    position: {
        x: canvas.width/2,
        y: canvas.height/2 + 50,
        z: 0
    },
    limits: {x: 100, y: 100}
});

document.addEventListener('mousemove', (event) => {
    console.log(event.clientX, event.clientY);
    body.updatePosition({
        x: event.clientX,
        y: event.clientY
    });
},false);

function animate() {
    //window.requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.moveTo(head.position.x,head.position.y);
    ctx.lineTo(body.position.x,body.position.y);
    ctx.stroke();
    ctx.closePath();
}
window.requestAnimationFrame(animate);