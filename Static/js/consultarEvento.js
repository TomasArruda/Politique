$(document).ready(function(){

	 var tipoEventoCmbBox = $('#cmbBoxEvento');
	 var tipoEventoNome = $('#cmbBoxEvento option:selected').text();
	 var divTipoElemento = $('#tipoEvento');

	$("#cmbBoxEvento").change(function(){

		var tipoEventoCmbBox = $('#cmbBoxEvento');
		var tipoEventoNome = $('#cmbBoxEvento option:selected').text();

		if (tipoEventoNome === "Capacitação Interna") {
		    $('#tabela-interna').show();
		    $('#tabela-externa').hide();
		    $('#tabela-institucional').hide();
		} else if (tipoEventoNome === "Capacitação Externa") {
		  	$('#tabela-interna').hide();
		    $('#tabela-externa').show();
		    $('#tabela-institucional').hide();		  
		} else {
		   $('#tabela-interna').hide();
		    $('#tabela-externa').hide();
		    $('#tabela-institucional').show();	
		}
 	
 	})
})