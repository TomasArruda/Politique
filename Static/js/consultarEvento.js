$(document).ready(function(){

	$("#cmbBoxEvento").change(function(){

		var tipoEventoCmbBox = $('#cmbBoxEvento');
		var tipoEventoNome = $('#cmbBoxEvento option:selected').text();

		if (tipoEventoNome === "Capacitação Interna") {
		    $('#tabela-interna').show();
		    $('#cmb-interna').show();
		    $('#tabela-externa').hide();
		    $('#cmb-externa').hide();
		    $('#tabela-institucional').hide();
		    $('#cmb-institucional').hide();
		} else if (tipoEventoNome === "Capacitação Externa") {
		  	$('#tabela-interna').hide();
		    $('#cmb-interna').hide();
		    $('#tabela-externa').show();
		    $('#cmb-externa').show();
		    $('#tabela-institucional').hide();
		    $('#cmb-institucional').hide();		  
		} else {
		    $('#tabela-interna').hide();
		    $('#cmb-interna').hide();
		    $('#tabela-externa').hide();
		    $('#cmb-externa').hide();
		    $('#tabela-institucional').show();
		    $('#cmb-institucional').show();	
		}
 	
 	});

	$("#cmbBoxEventoModal").change(tipoEventoSelecionado)

 	$(document).click( function(e){

        if ($('#dropdown:visible')) {
            $('#dropdown').hide();
        }

        if(!$(e.target).closest('#modalEditarEvento').length) {
            if($('#modalEditarEvento').is(":visible")) {
                $('#modalEditarEvento').hide()
            }
        }
    }); 
})

function tipoEventoSelecionado() {
	var tipoEventoCmbBox = $('#cmbBoxEventoModal');
	var tipoEventoNome = $('#cmbBoxEventoModal option:selected').text();

	if (tipoEventoNome === "Capacitação Interna") {
		$('#tipoEvento').html('<div class="editar-form-div"><label for="inputMaterial">Material</label><input type="text" name="material" id="inputMaterial" class="editar-form-input" placeholder=""></div>');
	} else if (tipoEventoNome === "Capacitação Externa") {
	$('#tipoEvento').html('<div class="editar-form-div"><label for="inputCusto">Custo</label><input type="text" name="custo" id="inputCusto" class="editar-form-input" placeholder=""></div><div class="editar-form-div"><label for="inputPalestrante">Palestrante</label><input type="text" name="palestrante" id="inputPalestrante" class="editar-form-input" placeholder=""></div>');
	} else {
	$('#tipoEvento').html('<div class="editar-form-div"><label for="inputCusto">Custo</label><input type="text" name="custo" id="inputCusto" class="editar-form-input" placeholder=""></div><div class="editar-form-div"><label for="inputMotivo">Motivo de patrocínio</label><input type="text" name="motivoPatrocinio" id="inputMotivo" class="editar-form-input" placeholder=""></div>');
	}
}

function ClickHandler(row, id, token, e, urlRemover, urlEditar) {
    iniciativaId = id;
    cells = row.getElementsByTagName('td');

    if (row.className.includes('linha-interna')) {
    	material = cells[0].firstChild;
    	tipoEvento = 1;
    	data = cells[1].firstChild;
    	feedback = cells[2].firstChild;
    	nome = cells[3].firstChild;
    } else if (row.className.includes('linha-externa')) {
    	feedback = cells[0].firstChild;
    	nome = cells[1].firstChild;
    	custo = cells[2].firstChild;
    	tipoEvento = 2;
    	data = cells[3].firstChild;
    	palestrante = cells[4].firstChild;
    } else {
    	feedback = cells[0].firstChild;
    	nome = cells[1].firstChild;
    	custo = cells[2].firstChild;
    	data = cells[3].firstChild;
    	tipoEvento = 3;
    	motivoPatrocinio = cells[4].firstChild;
    	empresasParceiras = cells[5].firstChild;
    }
    
    if ($('#dropdown:hidden')) {
        event.stopPropagation();   
        setposition(e);     
        $('#dropdown').toggle();
        $('#removerLink').attr('href', urlRemover);
        $('#editarForm').attr('action', urlEditar);
    }    
}

function setposition(e) {
    var bodyOffsets = document.body.getBoundingClientRect();
    tempX = e.pageX - bodyOffsets.left;
    tempY = e.pageY;

    $("#dropdown").css({ 'top': tempY, 'left': tempX });
}

function showModal(){
    if($('#modalEditarEvento:hidden')){
        event.stopPropagation();
        document.getElementById('inputNome').value = nome.textContent;
        document.getElementById('inputData').value = data.textContent;
        document.getElementById('inputFeedback').value = feedback.textContent;
        var tipoEventoString
        if (tipoEvento === 1) {
        	tipoEventoString = 'Capacitação Interna';
        } else if (tipoEvento === 2) {
        	tipoEventoString = 'Capacitação Externa';
        }

        //Definindo novos inputs baseado no valor atual do tipo de evento
        document.getElementById('cmbBoxEventoModal').value = tipoEvento        
        tipoEventoSelecionado();

        if (tipoEventoString === "Capacitação Interna") {
        	document.getElementById('inputMaterial').value = material.textContent;
        } else if (tipoEventoString === "Capacitação Externa") {
        	document.getElementById('inputCusto').value = custo.textContent;
        	document.getElementById('inputPalestrante').value = palestrante.textContent;
        } else {
        	document.getElementById('inputCusto').value = custo.textContent;
        	document.getElementById('inputMotivo').value = motivoPatrocinio.textContent;
        }

        $('#modalEditarEvento').toggle();
        $('#dropdown').hide();
    }
}

$('#inputPesquisa').bind('input', filtrarEvento);

function filtrarEvento(){
	var pesquisaString = $(this).val()
	var variavel = $('select:visible.cmb-variavel option:selected').text()

	var filtrados = $('.'+variavel).filter(function(index) {
	  return (this.innerHTML.toLowerCase().indexOf(pesquisaString.toLowerCase()) != -1)
	}).parent()
	  
	var naoFiltrados = $('.'+variavel).filter(function(index) {
	  return (this.innerHTML.toLowerCase().indexOf(pesquisaString.toLowerCase()) == -1)
	}).parent()

	filtrados.show()
	naoFiltrados.hide() 
};