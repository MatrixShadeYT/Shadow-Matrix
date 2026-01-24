const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
canvas.height = canvas.width*(9/16);
canvas.width = canvas.width;
function animate() {
    window.requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
window.requestAnimationFrame(animate);