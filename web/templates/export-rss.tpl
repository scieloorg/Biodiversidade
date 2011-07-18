<?xml version="1.0" encoding="UTF-8"?>

<rss version="2.0">
	<channel>
		<title>{$texts.TITLE}: {$smarty.request.q}</title>
		<link>{$url}</link>
		<description>{$texts.DESCRIPTION}</description>

		{foreach from=$result->response->docs item=doc}

			{capture name=scieloLinks}
				{iahlinks scielo=$links->response->docs document=$doc->ur id=$doc->id lang=$lang}
			{/capture}

			<item>
				<title><![CDATA[{occ element=$doc->ti separator=/}]]></title>
				<author><![CDATA[{occ element=$doc->au separator=;}]]></author>
            	<source><![CDATA[{occ element=$doc->fo separator=;}]]></source>

				{if $scieloLinkList|@count > 0}
					<link>{$scieloLinkList[0]|replace:"&":"&amp;"}</link>
				{elseif $doc->ur|@count > 0}
					<link>{$doc->ur[0]|replace:"&":"&amp;"}</link>
				{else}
					<link>{$url}?detail=1&amp;q=id:{$doc->id}</link>
				{/if}

				<description>
					<![CDATA[
                        {if isset($doc->au) }
                            {$texts.LABEL_AUTHOR}: {occ element=$doc->au separator=;}
                        {/if}
                        {if isset($doc->fo) }
                            <p>{$texts.LABEL_SOURCE}: {occ element=$doc->fo separator=;}</p>
                        {/if}
						{ if isset($doc->ab) }
							<span class="abstract"><p>{occ element=$doc->ab separator=/}</p></span>
						{/if}
                        { if isset($doc->mh) }
                            <p>
                                {$texts.LABEL_SUBJECT}:
                                {occ element=$doc->mh separator=;}
                            </p>
                        {/if}
					]]>
				</description>
			</item>
		{/foreach}
	</channel>
</rss>
