function check(){
    let pass1 = document.getElementByName("pass1").value;
    let pass2 = document.getElementByName("pass2").value;
    let sub = document.getElementByName("sub");
    if(pass1.length && (pass1!==pass2)){
        alert("Re-check your password");
        sub.disabled = true;
    }
    else{
        sub.disabled = false;
    }
}