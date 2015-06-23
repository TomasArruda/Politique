$(document).ready(function(){
    addRowHandlers();
    
    $(document).click( function(e){

        if ($('#dropdown:visible')) {
            $('#dropdown').hide();
        }

        if(!$(e.target).closest('#modalEditarIniciativa').length) {
            if($('#modalEditarIniciativa').is(":visible")) {
                $('#modalEditarIniciativa').hide()
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
                    website = cells[0].firstChild;
                    realizada = cells[1].firstChild;
                    apoio = cells[1].firstChild;
                    percepcao = cells[2].firstChild;
                    Presenca = cells[3].firstChild;
                    publicoAlvo = cells[4].firstChild;
                    duracao = cells[5].firstChild;
                    questoesChaves = cells[6].firstChild;
                    anoFundacao = cells[7].firstChild;
                    contato = cells[8].firstChild;
                    nome = cells[9].firstChild;
                    missao = cells[10].firstChild;
                    tipoMembro = cells[11].firstChild;
                    parceiros = cells[12].firstChild;
                    membro = cells[13].firstChild;
                    data = cells[14].firstChild;
                    principaisProgramas = cells[15].firstChild;
                    areaAtuacao = cells[16].firstChild;

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
    if($('#modalEditarIniciativa:hidden')){
        event.stopPropagation();
        console.log(data.textContent);
        document.getElementById('inputNome').value = nome.textContent;
        document.getElementById('inputData').value = data.textContent;
        document.getElementById('tipoMembro').value = tipoMembro.textContent;
        document.getElementById('inputPublico').value = publicoAlvo.textContent;
        document.getElementById('inputDuracao').value = duracao.textContent;
        document.getElementById('inputQuestoes').value = questoesChaves.textContent;
        document.getElementById('inputArea').value = areaAtuacao.textContent;
        document.getElementById('inputMissao').value = missao.textContent;
        document.getElementById('inputAnoFund').value = anoFundacao.textContent;
        document.getElementById('inputWebsite').value = website.textContent;
        document.getElementById('inputParceiros').value = parceiros.textContent;
        document.getElementById('inputProgramas').value = principaisProgramas.textContent;
        document.getElementById('inputApoio').value = apoio.textContent;
        document.getElementById('inputRealizada').value = realizada.textContent;
        document.getElementById('inputPercepcao').value = percepcao.textContent;
        document.getElementById('inputContato').value = contato.textContent;

        $('#modalEditarIniciativa').toggle();
        $('#dropdown').hide();
    }
}