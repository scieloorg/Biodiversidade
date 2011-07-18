
{if $doc->db eq 'DECS'}
    <div class="text_abstract">
        <a href="#" onclick="javascript:refineByIndex('{$doc->ti_pt[0]}','mh')"><img src="./image/common/viewFullText.gif"/></a>
        <a href="#" onclick="javascript:refineByIndex('{$doc->ti_pt[0]}','mh')">{$texts.SEARCH_USING_TERMINOLOGY}</a>
    </div>

{else}

    {capture name=fulltextlinks}
         {iahlinks scielo=$links->response->docs document=$doc->ur id=$doc->id lang=$lang la_text=$doc->la la_abstract=$doc->la_ab}
    {/capture}

    {* mostra linha com links para resumo e texto completo disponiveis para scielo *}
    {if $scieloLinkList|@count > 0}
        <div class="text_abstract">
            <img src="./image/common/icon_scielo.gif"/>
            {$abstractFulltextList}
        </div>
    {/if}

    {* mostra linha com resumo e texto completo informadas no documento *}
    {if  $scieloLinkList|@count == 0 AND ($doc->ab|@count > 0 OR $fulltextLinkList|@count > 0)}
        <div class="text_abstract">
            <a name="abs"><img src="./image/common/viewFullText.gif"/></a>
            {if  $doc->ab|@count > 0}
                <span>
                    <a href="mobile/resources/{$doc->id}">{$texts.ABSTRACT_IN}
                    {if  $doc->la_ab neq ''}
                        {occ element=$doc->la_ab translation=$texts suffix=LANG_ separator=| text_transform=lowercase}</a>
                    {else}
                        {occ element=$doc->la translation=$texts suffix=LANG_ separator=| text_transform=lowercase}</a>
                    {/if}
                </span>
            {/if}
            {if $fulltextLinkList|@count > 1}
                <span>
                    &#160;{$texts.FULLTEXT_IN}
                    {occ element=$doc->la translation=$texts suffix=LANG_ separator=| text_transform=lowercase}
                </span>
                <div class="showBox">
                    {$smarty.capture.fulltextlinks}
                </div>

            {elseif $fulltextLinkList|@count > 0}
                <span>
                    <a href="{$fulltextLinkList[0]}" target="_blank">
                    &#160;{$texts.FULLTEXT_IN}
                        {occ element=$doc->la translation=$texts suffix=LANG_ separator=| text_transform=lowercase}
                    </a>
                </span>
            {/if}
        </div>
    {/if}

    {if isset($smarty.cookies.userTK)}
        <div class="scielo">
                <a href="#">
                    <img src="./image/common/icon_addToFolder.gif"/>
                    &#160;<span>{$texts.ADD_TO_COLLECTION}</span>
                </a>
        </div>
    {/if}

{/if}
