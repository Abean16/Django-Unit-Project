const boxes = document.querySelectorAll('.item-box');
const descs = document.querySelectorAll('.item-desc');

for (let i = 0; i < boxes.length; i++){
    const currentBox = boxes[i];
    const currentDesc = descs[i];   

    currentBox.addEventListener("mouseenter", function(){
        currentBox.style.paddingBottom = "20%";
        currentBox.style.transform = "scaleY(1.0)";
        currentBox.style.transition = "1s";

        currentDesc.style.display = "block";  
        currentDesc.style.color = "aqua";
        currentDesc.style.backgroundColor = "black";
    });

    currentBox.addEventListener("mouseleave", function(){
        setTimeout(() => {
            currentBox.style.paddingBottom = "1%";
            currentDesc.style.display = "none"; 
            currentDesc.style.color = "yellow";
        }, 100);
    });
}

