<div class="bookmark">
    {if $media}

        <a href="{$media}/resources/{$doc->id}"><img src="http://s7.addthis.com/static/btn/sm-share-en.gif" width="83" height="16" alt="Bookmark and Share" style="border:0"/><!--span>{$texts.SHARE}</span--></a>
    {else}
        <a href="/resources/{$doc->id}"><img src="http://s7.addthis.com/static/btn/sm-share-en.gif" width="83" height="16" alt="Bookmark and Share" style="border:0"/><!--span>{$texts.DISPLAY.simple}</span--></a>
    {/if}
</div>
