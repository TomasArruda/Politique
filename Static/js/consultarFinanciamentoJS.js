$(document).ready(function(){
    addRowHandlers();
    
    $(document).click( function(e){

        if ($('#dropdown:visible')) {
            $('#dropdown').hide();
        }

        if(!$(e.target).closest('#modalEditarFinanciamento').length) {
            if($('#modalEditarFinanciamento').is(":visible")) {
                $('#modalEditarFinanciamento').hide()
            }
        }
    });    

});

function addRowHandlers() {
    var table = document.getElementById("tabela");
    var rows = table.getElementsByTagName("tr");

    for (i = 0; i < rows.length; i++) {
        var currentRow = table.rows[i];
        var createClickHandler = 
            function(row) 
            {
                return function(e) { 
                    cells = row.getElementsByTagName("td");
                    instituicaoResponsavel = cells[0].firstChild;
                    vencedoresAnteriores = cells[1].firstChild;
                    nome = cells[2].firstChild;
                    processo = cells[3].firstChild;
                    tema = cells[4].firstChild;
                    prazos = cells[5].firstChild;
                    valor = cells[6].firstChild;
                    membro = cells[7].firstChild;
                    projetos = cells[8].firstChild;

                    if ($('#dropdown:hidden')) {
                        event.stopPropagation();   
                        setposition(e);     
                        $('#dropdown').toggle();
                    }
                };
            };

        currentRow.onclick = createClickHandler(currentRow);
    }
}

function setposition(e) {
    var bodyOffsets = document.body.getBoundingClientRect();
    tempX = e.pageX - bodyOffsets.left;
    tempY = e.pageY;
  console.log(tempX);

    $("#dropdown").css({ 'top': tempY, 'left': tempX });
}

function showModal(){
    if($('#modalEditarFinanciamento:hidden')){
        event.stopPropagation();
        document.getElementById('inputInstitResponsavel').value = instituicaoResponsavel.textContent;
        document.getElementById('inputVencedores').value = vencedoresAnteriores.textContent;
        document.getElementById('inputNome').value = nome.textContent;
        document.getElementById('inputProcesso').value = processo.textContent;
        document.getElementById('inputTema').value = tema.textContent;
        document.getElementById('inputPrazos').value = prazos.textContent;
        document.getElementById('inputValor').value = valor.textContent;
        //document.getElementById('inputMembro').value = membro.textContent;
        document.getElementById('inputProjetos').value = projetos.textContent;

        $('#modalEditarFinanciamento').toggle();
        $('#dropdown').hide();
    }
}