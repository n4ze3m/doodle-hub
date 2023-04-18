const canvas = document.getElementById('drawing-board');
const ctx = canvas.getContext('2d');

const colorPicker = document.getElementById('color-picker');
const range = document.getElementById('range');

const rangeValue = document.getElementById('range-value');
const colorPickerPreview = document.getElementById('color-picker-preview');

rangeValue.innerText = `${range.value} px`;
colorPickerPreview.style.backgroundColor = colorPicker.value;

colorPicker.addEventListener('input', () => {
    if (isErasing) return;
    ctx.strokeStyle = colorPicker.value;
    colorPickerPreview.style.backgroundColor = colorPicker.value;
});

range.addEventListener('input', () => {
    ctx.lineWidth = range.value;
    rangeValue.innerText = `${range.value} px`;
});

let pos = { x: 0, y: 0 };
let isDrawing = false;
let undoStack = [];

let isErasing = false;

const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
let width = window.innerWidth * 0.6;
let height = window.innerHeight * 0.5;

if (isMobile) {
    width = window.innerWidth * 0.8;
    height = window.innerHeight * 0.5;
}
canvas.width = width;
canvas.height = height;

function resizeCanvas() {
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    let width = window.innerWidth * 0.6;
    let height = window.innerHeight * 0.5;
    
    if (isMobile) {
        width = window.innerWidth * 0.8;
        height = window.innerHeight * 0.5;
    }
    canvas.width = width;
    canvas.height = height;
}

window.addEventListener('resize', resizeCanvas);

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('touchstart', startDrawing);

canvas.addEventListener('mousemove', draw);
canvas.addEventListener('touchmove', draw);

canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseleave', stopDrawing);
canvas.addEventListener('touchend', stopDrawing);

document.addEventListener('keydown', handleKeyDown);

const colorBrushBtn = document.getElementById('color-brush');
const eraserBtn = document.getElementById('eraser');
const colorBrushContainer = document.getElementById('color-brush-container');
const eraserContainer = document.getElementById('eraser-container');
colorBrushContainer.classList.add('bg-gray-100');


colorBrushBtn.addEventListener('click', () => {
    isErasing = false;
    ctx.strokeStyle = colorPicker.value;
    eraserContainer.classList.remove('bg-gray-100');
    colorBrushContainer.classList.add('bg-gray-100');
});

eraserBtn.addEventListener('click', () => {
    isErasing = true;
    ctx.strokeStyle = 'white';

    eraserContainer.classList.add('bg-gray-100');
    colorBrushContainer.classList.remove('bg-gray-100');
});

function startDrawing(e) {
    e.preventDefault();
    isDrawing = true;
    setPosition(e);
}

function draw(e) {
    e.preventDefault();
    if (!isDrawing) return;
    ctx.lineWidth = range.value;
    ctx.lineCap = 'round';

    ctx.beginPath();
    ctx.moveTo(pos.x, pos.y);
    setPosition(e);
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();

    undoStack.push({ x: pos.x, y: pos.y });
}

function stopDrawing(e) {
    e.preventDefault();
    isDrawing = false;
}


function setPosition(e) {
    const canvasRect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / canvasRect.width;
    const scaleY = canvas.height / canvasRect.height;
    if (e.touches) {
        pos.x = (e.touches[0].pageX - canvasRect.left) * scaleX;
        pos.y = (e.touches[0].pageY - canvasRect.top) * scaleY;
    } else {
        pos.x = (e.pageX - canvasRect.left) * scaleX;
        pos.y = (e.pageY - canvasRect.top) * scaleY;
    }
}

function handleKeyDown(e) {
    if (e.ctrlKey && e.key === 'z') {
        e.preventDefault();
        undo();
    }
}

function undo() {

}