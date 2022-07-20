function check(){
    let pass1 = document.getElementById("p1").value;
    let pass2 = document.getElementById("p2").value;
    let sub = document.getElementById("s");
    if(pass1.length>5 && (pass1===pass2)){
        return true;
    }
    else{
        alert("Re-check your password");
        return false;
    }
}