		<!-- abstract -->
		{if $doc->ab|@count > 0 or $doc->ab_pt|@count > 0 or $doc->ab_es|@count > 0 or $doc->ab_en|@count > 0}
			<div class="description">

                {if $doc->ab_pt|@count > 0}
                    {$texts.LABEL_ABSTRACT_PT}

                    {capture name=abstract}
                        {occ element=$doc->ab_pt separator=<br/>}
                    {/capture}

                    {if $smarty.capture.abstract|count_characters > 500 && $printMode neq 'true'}
                        {assign var="ab1" value=$smarty.capture.abstract|substr:0:500}
                        {assign var="ab2" value=$smarty.capture.abstract|substr:500}
                        <div>
                            {$ab1}
                            <a href="#" onclick="$('#ab_pt_{$pos}').fadeIn('slow');$(this).css('display','none');return false">({$texts.MORE})</a>
                            <span id="ab_pt_{$pos}" style="display:none;">
                                {$ab2}
                            </span>
                        </div>
                    {else}
                        <div>
                            {$smarty.capture.abstract}
                        </div>
                    {/if}
                {/if}
                {if $doc->ab_es|@count > 0}
                    {$texts.LABEL_ABSTRACT_ES}

                    {capture name=abstract}
                        {occ element=$doc->ab_es separator=<br/>}
                    {/capture}

                    {if $smarty.capture.abstract|count_characters > 500 && $printMode neq 'true'}
                        {assign var="ab1" value=$smarty.capture.abstract|substr:0:500}
                        {assign var="ab2" value=$smarty.capture.abstract|substr:500}
                        <div>
                            {$ab1}
                            <a href="#" onclick="$('#ab_es_{$pos}').fadeIn('slow');$(this).css('display','none');return false">({$texts.MORE})</a>
                            <span id="ab_es_{$pos}" style="display:none;">
                                {$ab2}
                            </span>
                        </div>
                    {else}
                        <div>
                            {$smarty.capture.abstract}
                        </div>
                    {/if}
                {/if}
                {if $doc->ab_en|@count > 0}
                    {$texts.LABEL_ABSTRACT_EN}

                    {capture name=abstract}
                        {occ element=$doc->ab_en separator=<br/>}
                    {/capture}

                    {if $smarty.capture.abstract|count_characters > 500 && $printMode neq 'true'}
                        {assign var="ab1" value=$smarty.capture.abstract|substr:0:500}
                        {assign var="ab2" value=$smarty.capture.abstract|substr:500}
                        <div>
                            {$ab1}
                            <a href="#" onclick="$('#ab_en_{$pos}').fadeIn('slow');$(this).css('display','none');return false">({$texts.MORE})</a>
                            <span id="ab_en_{$pos}" style="display:none;">
                                {$ab2}
                            </span>
                        </div>
                    {else}
                        <div>
                            {$smarty.capture.abstract}
                        </div>
                    {/if}
                {/if}
			</div>
		{/if}
