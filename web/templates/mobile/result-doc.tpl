{foreach from=$result->response->docs item=doc name=doclist}

	{* assign var=refID value=$doc->id|regex_replace:"/.*-/":"" *}
	{assign var=refID value=$doc->id|substring_after:"-"}

<div id="{$doc->id}" class="record">

	<div class="data">       
		<!-- title -->
		<h3>
        {$smarty.foreach.doclist.index+$pagination.from}.
		{if $doc->db eq 'LIS'}
			{assign var=url value=$doc->ur[0]}

			<a href="{$url}" target="_blank">
				{occ element=$doc->ti separator=/}
			</a>
        {elseif $doc->db eq 'DECS'}
            {assign var=ti value=ti_`$smarty.request.lang`}

			<a href="decs_detail.php?term={$doc->$ti[0]}&lang={$smarty.request.lang}" target="_blank">
				{$doc->$ti[0]}
			</a>            
		{else}
			{if $doc->db|contains:"COCHRANE"}
				<a href="#" onclick="javascript:show_cochrane(this,'{$doc->db}','{$doc->id}')" target="_blank">
					{occ element=$doc->ti separator=/}
				</a>
			{else}
				<a href="mobile/resources/{$doc->id}">
					{occ element=$doc->ti separator=/}
				</a>
			{/if}
		{/if}
		</h3>
		<!-- author -->
		{occ element=$doc->au separator=; class=author}
		<!-- source -->
		{if $doc->db|contains:"COCHRANE"}
			{occ element=$doc->db separator=; class=source suffix=SOURCE_ translation=$texts}
		{else}
			{if $doc->type == 'article' AND  $doc->fo[0]|count > 0}
				{occ  element=$doc->fo separator=; class=source}
			{/if}
		{/if}
        
        {if $doc->db eq 'DECS'}
            {assign var=ab value=ab_`$smarty.request.lang`}
            {$doc->$ab[0]}
        {/if}

		<!-- database -->
		<div class="source">
			{translate text=$doc->type suffix=TYPE_ translation=$texts}

            [{translate text=$doc->db suffix=DB_ translation=$texts}

			{if $doc->db|contains:"MEDLINE"}
				<span>PMID:</span> {$doc->id|substring_after:"-"}
            {elseif $doc->db|contains:"COCHRANE"}
                 <span>ID:</span> {$doc->id}
            {elseif $doc->db|contains:"-"}
                <span>ID:</span> {$doc->id|substring_after:"-"}
            {elseif $doc->db|contains:"campusvirtualsp"}
			{else}
				<span>ID:</span> {$doc->id}
			{/if}]

            {occ label=$texts.LABEL_LANG element=$doc->la separator=; translation=$texts suffix=LANG_}
		</div>

        
        {if $scieloLinkList|@count > 0}
            <div class="abstractFulltextList">
                
            </div>
        {/if}

	</div>
	<div class="spacer"></div>

   	<div class="user-actions">
        {include file="$media/doc-actions-bar.tpl"}
    </div>

</div>
{/foreach}