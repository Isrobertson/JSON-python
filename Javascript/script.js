// this js script is just to convert input into a file

const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const fData= new FormData(form);
    console.log(fData);
})