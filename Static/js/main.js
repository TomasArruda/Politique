$(document).ready(function(){

	$( ".btn-show" ).click(function() {

	  	$(this).next().slideToggle( "slow" );

	  	if($(this).hasClass("consulta")){

			if($(this).hasClass("last")){
		  		$(this).removeClass("last");
			} else {
			  	$(this).addClass("last");
			}	
		} 
	});
});
