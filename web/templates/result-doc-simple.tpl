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
		{occ label=$texts.LABEL_AUTHOR element=$doc->au separator=; class=author}
		<!-- source -->
		{if $doc->db|contains:"COCHRANE"}
			{occ element=$doc->db separator=; class=source suffix=SOURCE_ translation=$texts}
		{else}
			{if $doc->fo[0]|count > 0}
				{assign var=journal value=$doc->fo[0]|substring_before:";"}

				{if $doc->type == 'article' AND $journal|count > 0}
					<div class="source">
						<a href="http://portal.revistas.bvs.br/transf.php?xsl=xsl/titles.xsl&xml=http://catserver.bireme.br/cgi-bin/wxis1660.exe/?IsisScript=../cgi-bin/catrevistas/catrevistas.xis|database_name=TITLES|list_type=title|cat_name=ALL|from=1|count=50&lang=pt&comefrom=home&home=false&task=show_magazines&request_made_adv_search=false&lang=pt&show_adv_search=false&help_file=/help_pt.htm&connector=ET&search_exp={$journal|noaccent}" target="_blank"><span>{$journal}</span></a>;
						{$doc->fo[0]|substring_after:";"}
					</div>
				{else}
					{occ element=$doc->fo separator=; class=source}
				{/if}
			{/if}
		{/if}
		<!-- database -->
		<div class="database">
		</div>

		<!-- type -->
		<div class="source">
			<span class="type">
				<img src="image/common/type_{$doc->type}.gif"/>
				<span>{translate text=$doc->type suffix=TYPE_ translation=$texts}</span>
			</span>

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
			
            {if $doc->services|@contains:"LXP"}
                <a onclick="LLXP(this,'{$lang}')" title="LILACS Express" class="thickbox">
                    <span><img src="./image/common/icon_lilacs.gif"/></span>
                    &#160;LILACS Express
                </a>
            {/if}

			{occ label=$texts.LABEL_LANG element=$doc->la separator=; translation=$texts suffix=LANG_}
		</div>
		<!-- [pt] publication type -->
		{if $doc->pt|@count > 0}
			<div class="tags">
				{$texts.LABEL_PUBLICATION}:
				{occ element=$doc->pt separator=;}
			</div>
		{/if}

		<!-- abstract -->
		{if $doc->ab|@count > 0 or $doc->ab_pt|@count > 0 or $doc->ab_es|@count > 0 or $doc->ab_en|@count > 0}
			<div class="description">

                {if $doc->db eq 'DECS'}
                    {assign var=ab value=ab_`$smarty.request.lang`}
                    {capture name=abstract}
                        {$doc->$ab[0]}
                    {/capture}
                {else}
                    {capture name=abstract}
                        {occ element=$doc->ab separator=<hr/>}
                    {/capture}
                {/if}

				{if $smarty.capture.abstract|count_characters > 800 && $printMode neq 'true'}
					{assign var="ab1" value=$smarty.capture.abstract|substr:0:800}
					{assign var="ab2" value=$smarty.capture.abstract|substr:800}
					<span>
						{$ab1}
						<a href="#" onclick="$('#ab_{$doc->id}').fadeIn('slow');$(this).css('display','none');return false">({$texts.MORE})</a>
						<span id="ab_{$doc->id}" style="display:none;">
							{$ab2}
						</span>
					</span>
				{else}
					<span>
						{$smarty.capture.abstract}
					</span>
				{/if}
			</div>
		{/if}

		<!-- subject -->
		{if $doc->mh|@count > 0}
			<div class="tags">
				{$texts.LABEL_SUBJECT}:
				{foreach key=mhKey item=mh from=$doc->mh}
					<a href="#" onclick="javascript:refineByIndex('{$mh}','mh')">{$mh}</a>
				{/foreach}
			</div>
		{/if}

	</div>
	<div class="spacer"></div>

    <div class="user-actions">
         {include file="doc-actions-bar.tpl"}
    </div>

</div>
{/foreach}