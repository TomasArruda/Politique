$(document).ready(function(){
    
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
function ClickHandler(row, id, token, e, urlRemover, urlEditar) {
    financiamentoId = id;
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
        $('#removerLink').attr('href', urlRemover);
        $('#editarForm').attr('action', urlEditar);
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

$('#inputPesquisa').bind('input', filtrarEvento);

function filtrarEvento(){
   
    var pesquisaString = $(this).val();
    var variavel = $('#cmb-variavel option:selected').text();

    var filtrados = $('.'+variavel).filter(function(index) {
      return (this.innerHTML.toLowerCase().indexOf(pesquisaString.toLowerCase()) != -1)
    }).parent();
      
    var naoFiltrados = $('.'+variavel).filter(function(index) {
      return (this.innerHTML.toLowerCase().indexOf(pesquisaString.toLowerCase()) == -1)
    }).parent();

    filtrados.show();
    naoFiltrados.hide();
};
