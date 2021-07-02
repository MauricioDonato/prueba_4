function validaRut(){
        campo = document.getElementById("rut_r").value;
        errorr_rut = 0
	if ( campo.trim().length == 0 ){ errorr_rut = 0; }
	if ( campo.trim().length < 8 ){  errorr_rut = 0; }

	campo = campo.trim().replace('-','')
	campo = campo.trim().replace(/\./g,'')

	var suma = 0;
	var caracteres = "1234567890kK";
	var contador = 0;    
	for (var i=0; i < campo.trim().length; i++){
		u = campo.trim().substring(i, i + 1);
		if (caracteres.indexOf(u) != -1)
		contador ++;
	}
	if ( contador==0 ) {  errorr_rut = 0 }
	
	var rut =campo.trim().substring(0,campo.trim().length-1)
	var drut = campo.trim().substring( campo.trim().length-1 )
	var dvr = '0';
	var mul = 2;
	
	for (i= rut.trim().length -1 ; i >= 0; i--) {
		suma = suma + rut.trim().charAt(i) * mul
                if (mul == 7) 	mul = 2
		        else	mul++
	}
	res = suma % 11
	if (res==1)		dvr = 'k'
                else if (res==0) dvr = '0'
	else {
		dvi = 11-res
		dvr = dvi + ""
	}
	if ( dvr != drut.toLowerCase() ) {  errorr_rut = 0; }
	else {  errorr_rut = 1; }
}

function validarUsuario(){
    var usuario = document.getElementById("rut_r").value;
    var usuario_nom = document.getElementById("nombre_usuario").value

    if(usuario == usuario_nom)
    {
        error_rut = 1;

    }
    else{
        document.getElementById("error_un").style.visibility = "visible";
        error_rut = 0;
    }
}

/* La siguiente instrucción extiende las capacidades de jquery.validate() para que
	admita el método RUT, por ejemplo:

$('form').validate({
	rules : { rut : { required:true, rut:true} } ,
	messages : { rut : { required:'Escriba el rut', rut:'Revise que esté bien escrito'} }
})
// Nota: el meesage:rut sobrescribe la definición del mensaje de más abajo
*/
// comentar si jquery.Validate no se está usando
jQuery.validator.addMethod("rut", function(value, element) { 
        return this.optional(element) || validaRut(value); 
}, "Revise el RUT");