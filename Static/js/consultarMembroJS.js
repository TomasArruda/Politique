$(document).ready(function(){
    addRowHandlers();
    
    $(document).click( function(e){

        if ($('#dropdown:visible')) {
            $('#dropdown').hide();
        }

        if(!$(e.target).closest('#modalEditarMembro').length) {
            if($('#modalEditarMembro').is(":visible")) {
                $('#modalEditarMembro').hide()
            }
        }
    });    

});

function ClickHandler(row, id, token, e, urlRemover, urlEditar) {
    iniciativaId = id;
    cells = row.getElementsByTagName("td");
    username = cells[0].firstChild;
    first_name = cells[1].firstChild;
    setor = cells[2].firstChild;

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
    if($('#modalEditarMembro:hidden')){
        event.stopPropagation();
        document.getElementById('inputNome').value = first_name.textContent;
        document.getElementById('inputEmail').value = username.textContent;

        $('#modalEditarMembro').toggle();
        $('#dropdown').hide();
    }
}