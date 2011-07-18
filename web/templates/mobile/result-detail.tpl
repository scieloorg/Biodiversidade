{foreach from=$result->response->docs item=doc name=doclist}

	{assign var=refID value=$doc->id|regex_replace:"/.*-/":""}

<div class="resultSet">
   <div id="{$doc->id}" class="record">

	<div class="data">
		<!-- title -->
		<h3>
		{if $doc->db eq 'LIS'}
			{assign var=url value=$doc->ur[0]}

			<a href="{$url}">
				{occ element=$doc->ti separator=/}
			</a>

		{else}
			{occ element=$doc->ti separator=/}
		{/if}
		</h3>
		<!-- author -->
		{occ label=$texts.LABEL_AUTHOR element=$doc->au separator=; class=author}
		<!-- source -->
		{if $doc->db|contains:"COCHRANE"}
			{occ label=$texts.LABEL_SOURCE element=$doc->fo separator=; class=source suffix=SOURCE_ translation=$texts}
		{else}
			{if $doc->fo[0]|count > 0}
				{assign var=journal value=$doc->fo[0]|substring_before:";"}

				{if $doc->type == 'article' AND $journal|count > 0}
					<div class="source">
						{$texts.LABEL_SOURCE}:
						<a href="http://portal.revistas.bvs.br/transf.php?xsl=xsl/titles.xsl&xml=http://catserver.bireme.br/cgi-bin/wxis1660.exe/?IsisScript=../cgi-bin/catrevistas/catrevistas.xis|database_name=TITLES|list_type=title|cat_name=ALL|from=1|count=50&lang=pt&comefrom=home&home=false&task=show_magazines&request_made_adv_search=false&lang=pt&show_adv_search=false&help_file=/help_pt.htm&connector=ET&search_exp={$journal}" target="_blank"><span>{$journal}</span></a>;
						{$doc->fo[0]|substring_after:";"}
					</div>
				{else}
					{occ label=$texts.LABEL_SOURCE element=$doc->fo separator=; class=source}
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
			{else}
				<span>ID:</span> {$doc->id|substring_after:"-"}
			{/if}
			]
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
				{capture name=abstract}
					{occ element=$doc->ab separator=<hr/>}
				{/capture}
				<span>
					{$smarty.capture.abstract}
				</span>
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
        {include file="$media/  doc-actions-bar.tpl"}

        <div class="bookmark">
                <!-- AddThis Button BEGIN -->
                <script type="text/javascript">addthis_pub  = 'bvs.regional';</script>
                <a href="http://www.addthis.com/bookmark.php" onmouseover="return addthis_open(this, '', '[URL]', '[TITLE]')" onmouseout="addthis_close()" onclick="return addthis_sendto()"><img src="http://s9.addthis.com/button1-bm.gif" width="125" height="16" border="0" alt="" /></a>
                <script type="text/javascript" src="http://s7.addthis.com/js/152/addthis_widget.js"></script>
                <!-- AddThis Button END -->
        </div>

	</div>
   </div>
</div>
{/foreach}