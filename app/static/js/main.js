const boxes = document.querySelectorAll('.item-box');
const descs = document.getElementsByClassName('.item-desc');
const button = document.getElementById('button')

for (let i = 0; i < boxes.length; i++) {
    const currentBox = boxes[i];
        currentBox.addEventListener("mouseenter", function(){
            currentBox.style.paddingBottom = "20%";
            currentBox.style.transform = "scaleY(1.0)";
            currentBox.style.transition = "1s";
        })
        currentBox.addEventListener("mouseleave", function(){
            setTimeout(() => {
                currentBox.style.paddingBottom = "1%";
                currentBox.style.display == "none";
            }, 500);
        })
}


button.addEventListener("click", function(){
    for (let i = 0; i < boxes.length; i++) {
    const currentBox = boxes[i];
        descs.style.display = "block"
    }
})


for (let i = 0; i < descs.length; i++) {
    const currentDesc = descs[i];
        currentDesc.addEventListener("mouseenter", function(){
            currentDesc.style.display == "block";
            currentDesc.style.color = "aqua"
            currentDesc.style.backgroundColor = "aqua"
        })
        currentDesc.addEventListener("mouseleave", function(){
            setTimeout(() => {
                currentDesc.style.display == "none";
            }, 500);
        })
}
