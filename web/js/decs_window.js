$(document).ready(
	function(){
		var lang = document.documentElement.lang;
		
		$("div.tags > a").each(
		function(){
			var descriptor=$(this).html();
			descriptor=descriptor.replace(/\/.*/,'');
			this.title=descriptor;
			this.rel="decs_tooltip.php?term="+escape(descriptor)+"&lang="+lang;
			$(this).cluetip(
				{
					hoverClass:'highlight',
					sticky:true,
					closePosition:'title',
					closeText:'<img src="image/common/gtk-close.png" alt="close" />',
					fx: { 
						open: 'fadeIn',
						openSpeed: 'slow'
					},
					hoverIntent: {    
                      sensitivity:  1,
           			  interval:     500,
           			  timeout:      0
    				}
				}
			);
		}
	);
});