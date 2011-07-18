
		<div class="search">
			<form name="searchForm" action="{$smarty.server.PHP_SELF}" method="post">
 				{if $config->search_collection_list->collection|@count > 1}
				  <div class="informationTypes">
					{foreach from=$config->search_collection_list->collection item=collection name=colIterator}
						{assign var=colName value=$collection->name}
						{assign var=colSite value=$collection->site}

						{if $colSite eq ''}
							{assign var=colSite value=$config->site}	
							{assign var=colId value=$colName|upper}
						{else}	
							{assign var=colId value="`$colName`-`$colSite`"|upper}
						{/if}

						{if ($col == $colName && $site == $colSite) }
							{assign var=selectColPos value=$smarty.foreach.colIterator.index}
	
							<a href="#" onclick="changeCollection('{$colName}','{$colSite}')" class="selected">{$texts.COLLECTIONS.$colId}</a>
						{else}
							<a href="#" onclick="changeCollection('{$colName}','{$colSite}')">{$texts.COLLECTIONS.$colId}</a>
						{/if}
					{/foreach}
				  </div>
				{/if}

				<div class="searchForm">
                                    <input type="hidden" name="lang" value="{$lang}"/>
                                    <input type="hidden" name="col" value="{$col}"/>
                                    <input type="hidden" name="site" value="{$site}"/>
                                    <input type="hidden" name="count" value="{$config->documents_per_page}"/>
                                    <input type="hidden" name="filter" value="{$filter|replace:"\\\"":"&quot;"}"/>
                                    <input type="hidden" name="filterLabel" value="{$filterLabel}"/>
                                    <input type="hidden" name="media" value="{$media}"/>
                                    <input type="hidden" name="where" value="{$smarty.request.where}"/>

                                    <!-- fields used by javascript functions -->
                                    <input type="hidden" name="pageFrom" value="{$from}"/>
                                    <input type="hidden" name="from" value=""/>
                                    <input type="hidden" name="addfilter" value=""/>
                                    <input type="hidden" name="backfilter" value=""/>
                                    <input type="hidden" name="printMode" value=""/>
                                    <input type="hidden" name="output" value=""/>
                                    <input type="hidden" name="fb" value=""/>

                                    {if isset($smarty.request.debug)}
                                            <input type="hidden" name="debug" value="1"/>
                                    {/if}

                                    {foreach from=$filter_chain item=filterValue}
                                            {assign var=fvalue value=$filterValue|replace:"\\\"":"&quot;"}
                                            <input type="hidden" name="filter_chain[]" value="{$fvalue}">
                                    {/foreach}

                                    <input type="text" name="q" value="{$q_escaped}" class="inputText" onKeyDown="if(event.keyCode==13) newSearch();"/>

                                    <input type="button" name="go" value="{$texts.SEARCH_SUBMIT}" class="submit" onclick="javascript:newSearch()" />
                                    <!--
                                    &#160;
                                    <a href="#"><?=$texts['SEARCH_ADVANCED']?></a>
                                    -->
				</div>

			</form>
		</div>
