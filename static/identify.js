const buttons = document.querySelectorAll(".button")

for(let button of buttons){
    button.addEventListener('click', function(e){
        let next = button.id;
        button.parentElement.classList.remove('active');
        document.querySelector(`#tab-${next}`).classList.add('active');
    });
}