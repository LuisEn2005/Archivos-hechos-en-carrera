document.addEventListener('DOMContentLoaded',function(){
    let Texto = document.getElementById("Nombre");
    let Email = document.getElementById("Email");
    let Telefono = document.getElementById("Telefono");
    let infoNombre = document.getElementById("InfoNombre");
    let infoCorreo = document.getElementById("InfoCorreo");
    let infoTelefono = document.getElementById("InfoTele");
    
    window.Procesar = function(){
        let name = Texto.value.trim();
        let correo = Email.value.trim();
        let tele = Telefono.value.trim();
        const nombrePattern = /^[a-zA-Z\s]+$/;
        const correoPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const telePattern = /^[0-9]{9}$/;
        if(name === "" || !nombrePattern.test(name)){
            infoNombre.value = "Incorrecto";
        }
        else{
            infoNombre.value="Correcto";
        }
        if(correo === "" || !correoPattern.test(correo)){
            infoCorreo.value = "Incorrecto";
        }
        else{
            infoCorreo.value="Correcto";
        }
        if(tele === "" || !telePattern.test(tele)){
            infoTelefono.value = "Incorrecto";
        }
        else{
            infoTelefono.value="Correcto";
        }
    };
});