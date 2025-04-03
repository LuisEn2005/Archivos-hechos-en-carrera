function calculador(){
    var resultado = document.getElementById('resultado')
    var igual = document.getElementById
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    var n3 = document.getElementById("num3").value;
    var n4 = document.getElementById("num4").value;
    var n5 = document.getElementById("num5").value;
    var n6 = document.getElementById("num6").value;
    var n7 = document.getElementById("num7").value;
    var n8 = document.getElementById("num8").value;
    var n9 = document.getElementById("num9").value;
    var n0 = document.getElementById("num0").value;

    resultado = n1+n2+n3+n4+n5+n6+n7+n8+n9;
    
    document.getElementById("resultado").value = resultado;
}

function suma(){
    /*
    n1 = parseInt(document.getElementById("n1").value);
    n2 = parseInt(document.getElementById("n2").value);
    n3 = parseInt(document.getElementById("n3").value);
    resultado = n1 + n2 + n3;
    */
    document.getElementById("resultado").value = resultado;
}

function resta(){
    /*
    n1 = parseInt(document.getElementById("n1").value);
    n2 = parseInt(document.getElementById("n2").value);
    n3 = parseInt(document.getElementById("n3").value);
    resultado = n1 - n2 - n3;
    */
    document.getElementById("resultado").value = resultado;
}

function producto(){
    /*
    n1 = parseInt(document.getElementById("n1").value);
    n2 = parseInt(document.getElementById("n2").value);
    n3 = parseInt(document.getElementById("n3").value);
    resultado = n1 * n2 * n3;
    */
    document.getElementById("resultado").value = resultado;
}

function division(){
    n1 = parseInt(document.getElementById("n1").value);
    n2 = parseInt(document.getElementById("n2").value);
    n3 = parseInt(document.getElementById("n3").value);
    resultado = n1 / n2 / n3;
    document.getElementById("resultado").value = resultado;
}