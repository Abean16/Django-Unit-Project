const boxes = document.querySelectorAll('.item-box');
const descs = document.querySelectorAll('.item-desc');
const desc = document.getElementById('item-desc');
const button = document.getElementById('button');

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
    if(desc.style.display = "none"){
        desc.style.display = "block" }
    else if(desc.style.display = "block"){
        desc.style.display = "none"
    }

})


for (let i = 0; i < descs.length; i++) {
    const currentDesc = descs[i];
        boxes.addEventListener("mouseenter", function(){
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
