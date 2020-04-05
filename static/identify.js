let buttons = document.querySelectorAll(".button-lg")
let start = document.querySelector("#start")

for(let button of buttons){
    let next = button.id;
    button.addEventListener('click', function(e){
        button.parentElement.parentElement.classList.remove('active');
        document.querySelector(`#tab-${next}`).classList.add('active');
        console.log(button.id);            
    });
    if (next == 'end'){
        $(button).hide();
        if(next =='end' && button.className == 'button-lg yes'){
            console.log('found the f');
            
        }
    }
}

start.addEventListener('click', function(e){
    start.textContent = "Restart";
    $(start).removeClass("active");
    for(let button of buttons){
        button.parentElement.parentElement.classList.remove('active');
    }
});


//render a start over button, add fish link, restarting removes active from start