$(document).ready(
	function(){
		var lang = document.documentElement.lang;

        $("div.pubmed > a").each(
		function(){
			var pmid=$(this).attr("href");
            pmid=pmid.replace(/mdl\-/,'');
			this.title='PubMed Linkout Service';
			this.rel="pubmed_linkout.php?pmid="+ pmid +"&lang="+lang;
			$(this).cluetip(
				{
                    activation: 'click',
					hoverClass:'highlight',
					sticky:true,
					closePosition:'title',
					closeText:'<img src="image/common/gtk-close.png" alt="close" />',
                    width: '420px',
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