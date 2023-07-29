let Demobts = document.querySelector('button');
Demobts.addEventListener('click', inputMsg);

function inputMsg(){
    let name = prompt('Enter your name');
Demobts.textContent = 'roll no. 16:' + name
}