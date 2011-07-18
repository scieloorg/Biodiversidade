<div class="infoBar">
	<div class="totalResults">
		{$texts.RESULTS}&#160;
		<strong>{$pagination.from}-{$pagination.to}</strong> de <strong>{$pagination.total|number_format:0:",":"."}</strong>
	</div>

	{if $pagination.last gt 1}
		<div class="pagination">
	
			{if $pagination.page gt 1}

				{math assign="previous" equation="(((current - 1) * count) - count) + 1" current=$pagination.page count=$pagination.count}

				<span>&lt; <a href="javascript:changeFormParameter('from','{$previous}')">{$texts.PREVIOUS_PAGE}</a></span>
			{/if}
			
	
			{if $pagination.page eq $pagination.last}	

			{else}
				{math assign="nextFrom" equation="( ((current - 1) * count) + count) + 1" current=$pagination.page count=$pagination.count}
	
				<span><a href="javascript:changeFormParameter('from','{$nextFrom}')">{$texts.NEXT_PAGE}</a> &gt;</span>
			{/if}
	
		</div>
	{/if}
</div>
