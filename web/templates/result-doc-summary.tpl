{if isset($smarty.request.debug)}
	{debug}
{/if}

{foreach from=$result->response->docs item=doc name=doclist}

	{* assign var=refID value=$doc->id|regex_replace:"/.*-/":"" *}
	{assign var=refID value=$doc->id|substring_after:"-"}

<div id="{$doc->id}" class="record">

	<div class="yourSelectionCheck">
		<a onclick="markUnmark(this.firstChild,'{$doc->id}');"><img src="./image/common/box_unselected.gif" state="u" alt="{$texts.MARK_DOCUMENT}" title="{$texts.MARK_DOCUMENT}" /></a>
	</div>
	<div class="position">
		{$smarty.foreach.doclist.index+$pagination.from}.
	</div>
	<div class="data">

		<!-- title -->
		<h3>
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
				<a href="resources/{$doc->id}">
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
				{assign var=journal value=$doc->fo[0]|substring_before:";"}

				{if $journal|count > 0}
					<div>
						<a href="http://portal.revistas.bvs.br/transf.php?xsl=xsl/titles.xsl&xml=http://catserver.bireme.br/cgi-bin/wxis1660.exe/?IsisScript=../cgi-bin/catrevistas/catrevistas.xis|database_name=TITLES|list_type=title|cat_name=ALL|from=1|count=50&lang=pt&comefrom=home&home=false&task=show_magazines&request_made_adv_search=false&lang=pt&show_adv_search=false&help_file=/help_pt.htm&connector=ET&search_exp={$journal|noaccent}" target="_blank"><span>{$journal}</span></a>;
						{$doc->fo[0]|substring_after:";"}
					</div>
				{else}
					{occ  element=$doc->fo separator=; class=source}
				{/if}
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
        {include file="doc-actions-bar.tpl"}
    </div>

</div>
{/foreach}