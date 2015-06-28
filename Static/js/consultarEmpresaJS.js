$(document).ready(function(){
    addRowHandlers();
    
    $(document).click( function(e){

        if ($('#dropdown:visible')) {
            $('#dropdown').hide();
        }

        if(!$(e.target).closest('#modalEditarEmpresa').length) {
            if($('#modalEditarEmpresa').is(":visible")) {
                $('#modalEditarEmpresa').hide()
            }
        }
    });    

});

function ClickHandler(row, id, token, e, urlRemover, urlEditar) {
    empresaId = id;
    cells = row.getElementsByTagName("td");
    ramoAtuacao = cells[0].firstChild;
    nome = cells[1].firstChild;
    propostaApoio = cells[2].firstChild;
    tipoParceria = cells[3].firstChild;
    background = cells[4].firstChild;
    iniciativas = cells[5].firstChild;
    apoios = cells[6].firstChild;
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
    if($('#modalEditarEmpresa:hidden')){
        event.stopPropagation();
        document.getElementById('inputNome').value = nome.textContent;
        document.getElementById('inputRamo').value = ramoAtuacao.textContent;
        document.getElementById('inputBackground').value = background.textContent;
        document.getElementById('inputApoios').value = apoios.textContent;
        document.getElementById('inputProposta').value = nome.textContent;

        $('#modalEditarEmpresa').toggle();
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
