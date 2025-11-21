const boxes = document.querySelectorAll('.item-box');
const descs = document.querySelectorAll('.item-desc');
const innerBoxes = document.querySelectorAll('.item-box-inner')

for (let i = 0; i < boxes.length; i++){
    const currentBox = boxes[i];
    const currentDesc = descs[i];
    const currentInnerBox = innerBoxes[i]

    currentBox.addEventListener("mouseenter", function(){
        currentBox.style.paddingBottom = "25%";
        currentBox.style.transform = "scaleY(1.0)";
        currentBox.style.transition = "1s";
        setTimeout(() => {
            currentDesc.style.display = "flex";  
            currentDesc.style.animation = "fadeIn 1s"
        }, 450);
    });

    currentBox.addEventListener("mouseleave", function(){
        setTimeout(() => {
            currentBox.style.paddingBottom = "1%";
            currentDesc.style.display = "none"; 
        }, 100);
    });
    
}

