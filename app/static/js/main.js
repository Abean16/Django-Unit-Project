const boxes = document.querySelectorAll('.item-box');
const descs = document.querySelectorAll('.item-desc');

for (let i = 0; i < boxes.length; i++){
    const currentBox = boxes[i];
    const currentDesc = descs[i];
    let timeout;

    currentBox.addEventListener("mouseenter", function(){
        clearTimeout(timeout);

        currentBox.style.transition = "padding-bottom 1s";
        currentBox.style.paddingBottom = "25%"; 

        timeout = setTimeout(() => {
            currentDesc.style.display = "flex";  
            currentDesc.style.animation = "fadeIn 1s";
        }, 450);
    });

    currentBox.addEventListener("mouseleave", function(){
        clearTimeout(timeout); 

        timeout = setTimeout(() => {
            currentBox.style.paddingBottom = "1%";
            currentDesc.style.display = "none"; 
        }, 100);
    });
}
