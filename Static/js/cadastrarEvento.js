$(document).ready(function(){

	 var tipoEventoCmbBox = $('#cmbBoxEvento');
	 var tipoEventoNome = $('#cmbBoxEvento option:selected').text();
	 var divTipoElemento = $('#tipoEvento');

	$("#cmbBoxEvento").change(function(){
		  var tipoEventoCmbBox = $('#cmbBoxEvento');
		  var tipoEventoNome = $('#cmbBoxEvento option:selected').text();

		  if (tipoEventoNome === "Capacitação Interna") {
		      $('#tipoEvento').html('<div class="cadastrar-form-div"><label for="inputMaterial">Material</label><input type="text" name="material" id="inputMaterial" class="cadastrar-form-input" placeholder=""></div>');
		  } else if (tipoEventoNome === "Capacitação Externa") {
		   $('#tipoEvento').html('<div class="cadastrar-form-div"><label for="inputCusto">Custo</label><input type="text" name="custo" id="inputCusto" class="cadastrar-form-input" placeholder=""></div><div class="cadastrar-form-div"><label for="inputPalestrante">Palestrante</label><input type="text" name="palestrante" id="inputPalestrante" class="cadastrar-form-input" placeholder=""></div>');
		  } else {
		   $('#tipoEvento').html('<div class="cadastrar-form-div"><label for="inputCusto">Custo</label><input type="text" name="custo" id="inputCusto" class="cadastrar-form-input" placeholder=""></div><div class="cadastrar-form-div"><label for="inputMotivo">Motivo de patrocínio</label><input type="text" name="motivoPatrocinio" id="inputMotivo" class="cadastrar-form-input" placeholder=""></div>');
		  }
 	
 	})
})
