
var v = document.getElementById("srch");

v.addEventListener("keyup", function(event){
    if (event.keyCoce === 13){
        event.preventDefault();
        asdf();
    }
});
function asdf(){
    var v = document.getElementById("srch");
    if (v.value != ""){
        location.href = "/search/" + v.value;
    }
    else {
        v.classList.add('bg-red-500');
    }
}


