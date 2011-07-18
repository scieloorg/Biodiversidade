<div class="infoBar">
	<div class="totalResults">
		{$texts.RESULTS}&#160;
		<strong>{$pagination.from}-{$pagination.to}</strong> de <strong>{$pagination.total|number_format:0:",":"."}</strong>
	</div>

	{if $pagination.last gt 1}
		<div class="pagination">
	
			{if $pagination.page gt 1}

				{math assign="previous" equation="(((current - 1) * count) - count) + 1" current=$pagination.page count=$pagination.count}

				<span>&lt;&lt; <a href="javascript:changeFormParameter('from','1')">{$texts.FIRST_PAGE}</a></span>
				<span>&lt; <a href="javascript:changeFormParameter('from','{$previous}')">{$texts.PREVIOUS_PAGE}</a></span>
			{else}
				<span>&lt;&lt; {$texts.FIRST_PAGE}</span>
				<span>&lt; {$texts.PREVIOUS_PAGE}</span>
			{/if}
			
			{foreach from=$pagination.pages item=iPage}
			
				{math assign="nextFrom" equation="((current - 1) * count) + 1" current=$iPage count=$pagination.count}
			
				{if $iPage eq $pagination.page}	
					<span>{$iPage}</span>	
				{else}
					<span><a href="javascript:changeFormParameter('from','{$nextFrom}')" >{$iPage}</a></span>	
				{/if}
				
			{/foreach}
	
			{if $pagination.page eq $pagination.last}	
				<span>{$texts.NEXT_PAGE} &gt;</span>
			{else}
				{math assign="nextFrom" equation="( ((current - 1) * count) + count) + 1" current=$pagination.page count=$pagination.count}
	
				<span><a href="javascript:changeFormParameter('from','{$nextFrom}')">{$texts.NEXT_PAGE}</a> &gt;</span>
			{/if}
	
		</div>
	{/if}
</div>
