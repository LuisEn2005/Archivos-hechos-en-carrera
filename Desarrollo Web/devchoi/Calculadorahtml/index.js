const txtOp1 = document.getElementById("Op1");

const txtOperacion = document.getElementById("Operacion");

const txtOp2 = document.getElementById("Op2");

const BtnCalcular = document.getElementById("Calcular");

const Resultado = document.getElementById("Resultado");

BtnCalcular.addEventListener('click', Calcular);

function Calcular(){
    const operacion = txtOperacion.value;
    const Op1 = parseFloat(txtOp1.value);
    const Op2 = parseFloat(txtOp2.value);

    //console.log(txtOperando.value) imprime en la consola de la página el texto del input operador
    if((operacion == "+" || operacion == "-" || operacion == "*" || operacion == "/") && !isNaN(Op1) && !isNaN(Op2)){
        let result;
        switch(operacion){
            case "+":
                result = Op1 + Op2;
                break;
            case "-":
                result = Op1 - Op2;
                break;
            case "*":
                result = Op1 * Op2;
                break;
            case "/":
                result = Op1 / Op2;
                break;
        }
        Resultado.style = "color:green";
        Resultado.innerText = "= " + result;
    }
    else{
        Resultado.style = "color:red";
        Resultado.innerText = "Calculo imposible";
    }
}