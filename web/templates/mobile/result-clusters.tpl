{assign var="facetBrowse" value=$smarty.post.fb|substring_before:":"}

<div class="bContent" id="refine_facet">
{foreach from=$result->facet_counts item=cluster}

  {foreach key=key item=item from=$cluster}

	{assign var="label" value="REFINE_$key"}
	{assign var="totalItems" value=$item|@count}

	{if $totalItems gt 0}
        {* caso o usuario esteja vendo mais itens do cluster mostra o div aberto *}
        {if $facetBrowse eq $key}
        	<div id="{$key}">
        {else}
            <div id="{$key}" class="closed">
        {/if}
		{if $key == 'fulltext'}
			<strong onclick="showHideBox('{$key}')">{$texts.$label}</strong>
			(<a href="#" onclick="javascript:applyFilter('{$item[0][0]}','fulltext')">{$item[0][1]}</a>)

		{else}
			<strong onclick="showHideBox('{$key}')">{$texts.$label}</strong>			
			<ul id="{$key}_set">
			{if $key == 'type'}
				{foreach key=clusterKey item=clusterItem from=$item}

					{capture name=type}{translate text=$clusterItem[0] suffix=TYPE_ translation=$texts}{/capture}
					{if $smarty.capture.type ne ''}
						<li>
							<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">{$smarty.capture.type}</a> ({$clusterItem[1]})
						</li>
					{/if}
				{/foreach}

			{elseif $key == 'mh_cluster'}

				{foreach key=clusterKey item=clusterItem from=$item}
					<li>
						<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','mj')">{$clusterItem[0]}</a> ({$clusterItem[1]})
					</li>
				{/foreach}

			{elseif $key == 'limit'}

                {foreach key=clusterKey item=clusterItem from=$item}
                    {capture name=limit}{translate text=$clusterItem[0] suffix=LIMIT_ translation=$texts}{/capture}
                    {if $smarty.capture.limit ne ''}
                        <li>
                            <a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">{$smarty.capture.limit}</a> ({$clusterItem[1]})
                        </li>
                    {/if}
                {/foreach}

			{elseif $key == 'type_of_study'}

				{foreach key=clusterKey item=clusterItem from=$item}
                    {capture name=study}{translate text=$clusterItem[0] suffix=STUDY_ translation=$texts}{/capture}

                    {if $smarty.capture.study ne ''}
    					<li>
	    					<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','type_of_study')">{$smarty.capture.study}</a>    ({$clusterItem[1]})
					    </li>
                    {/if}
				{/foreach}

			{elseif $key == 'la'}

				{foreach key=clusterKey item=clusterItem from=$item}

					{capture name=lang}{translate text=$clusterItem[0] suffix=LANG_ translation=$texts}{/capture}
					{if $smarty.capture.lang ne ''}
						<li>
							<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">{$smarty.capture.lang}</a> ({$clusterItem[1]})
						</li>
					{/if}
				{/foreach}

            {elseif $key == 'clinical_aspect'}

                {foreach key=clusterKey item=clusterItem from=$item}

                    {capture name=lang}{translate text=$clusterItem[0] suffix=ASPECT_ translation=$texts}{/capture}
                    {if $smarty.capture.lang ne ''}
                        <li>
                            <a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">{$smarty.capture.lang}</a> ({$clusterItem[1]})
                        </li>
                    {/if}
                {/foreach}

			{else}
				{foreach key=clusterKey item=clusterItem from=$item}
					<li>
						<a href="#" onclick="javascript:applyFilter('{$clusterItem[0]}','{$key}')">{$clusterItem[0]}</a> ({$clusterItem[1]})
					</li>
				{/foreach}
			{/if}
		{/if}
        {* FIX: show more option for mobile template *}
		</ul>
	</div>

	{/if}
  {/foreach}
{/foreach}
</div>
