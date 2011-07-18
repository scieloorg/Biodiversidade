
	<div class="parent">
		<a href="{$config->bvs_url}">
			<img src="./image/{$lang}/logo_bvs.gif" alt="{$texts.vhl_alternate}" title="{$texts.vhl_alternate}" />
		</a>
	</div>
	<div class="identification">
		<h2>{$texts.BVS_TITLE}</h2>
		<h1>{$texts.TITLE}</h1>
	</div>
	<div class="otherVersions">
		{foreach key=langcode item=language from=$texts.AVAILABLE_LANGUAGES}
			{if $langcode|lower eq $lang }
				{assign var="class" value=" class='selected'"}
			{else}
				{assign var="class" value=""}
			{/if}
			<a href="#" onclick="searchForm.q.value='';changeFormParameter('lang','{$langcode|lower}');" {$class}>{$language}</a>
		{/foreach}
	</div>
	<div class="spacer">&#160;</div>
