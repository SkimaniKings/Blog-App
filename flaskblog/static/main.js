
// $(document).ready(function(){
//     let numberOfLikes = 0
//     $("#like").click(function(){
//         numberOfLikes = +1
//         document.getElementById("like").innerHTML = numberOfLikes;

//     });

// });

let click = 0;
let clicks = 0;
function onClick() {
    click += 1;
    document.getElementById("click").innerHTML = click;
}
function onClicks() {
    clicks += 1;
    document.getElementById("clicks").innerHTML = clicks;
}


// $(document).ready(function(){
//     $("#dd").click(function(){
//         $("#cc").show("5000")
//     });
// });