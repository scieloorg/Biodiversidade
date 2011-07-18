{if $result eq ''}
	<div class="noResults">
		{$texts.COLLECTION_UNAVAILABLE}
	</div>
{elseif isset($result->response->connection_problem)}
	<div class="noResults">
		{$texts.CONNECTION_ERROR}
	</div>
{elseif $numFound eq '0'}
	<div class="noResults">
		{$texts.NO_RESULTS}
	</div>
{else}

<div class="results">

	<div class="resultServices">
		<div id="searchHistory" class="searchHistory closed">
		<h4>
			<a onclick="showHideBox('searchHistory');" title="{$texts.SHOW_HIDE}">
				<span>{$texts.HISTORY}</span>&#160;
				(<span id="sizeOfHistorySearch"></span>)
			</a>
		</h4>
		<div class="history bContent">
			<ul id="searchHistoryList" class="showBox">
				<!-- Preenchido pelo PHP 'searchHistory.php' na funcão 'printSearchItem($term)' -->
			</ul>
			<span class="arrowBox"></span>
			<script type="text/javascript">retrieveSearchTerms();</script>
		</div>
		<div id="searchHistoryOperators" class="popup" style="display:none">
			<h4>
				<span>{$texts.OPERATORS}</span>
				<img src="image/common/close.gif" onclick="showhideLayers('searchHistoryOperators')"/>
			</h4>
			<ul>
				<li onclick="addTermToSearch(this.innerHTML);">OR</li>
				<li onclick="addTermToSearch(this.innerHTML);">AND</li>
				<li onclick="addTermToSearch(this.innerHTML);">AND NOT</li>
			</ul>
		</div>
	</div>

	<div id="yourSelection" class="yourSelection closed">
		<h4>
			<a onclick="showHideBox('yourSelection')" title="{$texts.SHOW_HIDE}">
				<span>{$texts.YOUR_SELECTION}</span>&#160;
				(<span id="sizeOfBookmarks_0"></span>)
			</a>
		</h4>
		<div class="selection bContent">
			<ul class="showBox">
			<p>
				{$texts.SELECTION.YOU_HAVE}&#160;<span id="sizeOfBookmarks_1">0</span>&#160;{$texts.SELECTION_REGISTERS}.
			</p>
				<li><a onclick="showBookmarks()">{$texts.SELECTION_LIST_REGISTERS}</a></li>
				<li><a onclick="clearBookmarks()" href="index.php?">{$texts.SELECTION_CLEAR_LIST}</a></li>
			</ul>
			<span class="arrowBox"></span>
		</div>
	</div>

	<div class="refineSearch" id="refineSearch">
		<!--h4><a href="#" onclick="showHideBox('refineSearch')" title="{$texts.SHOW_HIDE}"><span>{$texts.REFINE}</span></a></h4-->
		<div class="collapseAll" onclick="expandRetractResults('retract')">
			<img src="image/common/resultServices_minus_icon2.jpg" alt="Collapse All"/>
			&#160;{$texts.RETRACT_ALL}
		</div>
		<div class="expandAll" onclick="expandRetractResults('expand')">
			<img src="image/common/resultServices_plus_icon2.jpg" alt="Expand All"/>
			&#160;{$texts.EXPAND_ALL}
		</div>

		{include file="result-clusters.tpl"}

	</div>
    <div></div>


</div>
{if $numFound > 0}
    <div class="resultOptions">
				<div class="resultNavigation">{include file="result-navigation.tpl"}</div>
				<div class="resultsBar">
						<div class="selectAll" id="selectAll">
							<input type="button" value="{$texts.SELECT_PAGE}" onclick="markAll(); showhideLayers('selectAll');showhideLayers('clearAll')" />
						</div>
	                    <div class="clearAll" id="clearAll" style="display: none">
	                        <input type="button" value="{$texts.UNSELECT_PAGE}" onclick="unmarkAll();showhideLayers('clearAll');showhideLayers('selectAll')" />
	                    </div>
						<div class="orderBy">
							
							<select name="sortBy" class="inputText" onchange="javascript:changeOrderBy(this);">
								<option value="">{$texts.SORT_OPTIONS}</option>
								{foreach from=$colectionData->sort_list->sort item=sortItem}
									{assign var=sortName value=$sortItem->name|upper}
									{assign var=sortValue value=$sortItem->value}
	
									{if $sortName neq ''}
										{if $sortName == $smarty.request.sort}
											<option value="{$sortName}" selected="1">{$texts.SORT.$sortName}</option>
										{else}
											<option value="{$sortName}">{$texts.SORT.$sortName}</option>
										{/if}
									{/if}
								{/foreach}
							</select>
						</div>
	
	                    {if $colectionData->format_list->format|@count > 0}
	                        <div class="format">
	                            
	                            <select name="fmt" class="inputText" onchange="javascript:changeDisplayFormat(this);">
									<option value="">{$texts.FORMAT_OPTIONS}</option>								
	                                {foreach from=$colectionData->format_list->format item=formatItem}
	                                    {assign var=formatName value=$formatItem->name|strip}
	                                    {assign var=textsDisplay value=$texts.DISPLAY}
	
	                                    {if $formatName neq ''}
	                                        {if $formatName == $smarty.request.fmt}
	                                            <option value="{$formatName}" selected="1">{$texts.DISPLAY.$formatName}</option>
	                                        {else}
	                                            <option value="{$formatName}">{$texts.DISPLAY.$formatName}</option>
	                                        {/if}
	                                    {/if}
	                                {/foreach}
	                            </select>
	                        </div>
	                    {/if}
	
						<div class="feed">
							<a class="RSS" href="index.php?output=rss&site={$site}&col={$col}&lang={$lang}{$getParams}"><span>RSS</span></a>
							<a class="XML" href="index.php?output=xml&site={$site}&col={$col}&lang={$lang}{$getParams}"><span>XML</span></a>
						</div>
						<div class="export">
							<a href="#" onclick="showhideLayers('megaBox')">{$texts.SEND_RESULT}</a>
							<div id="megaBox" class="emailBox boxContent" style="display:none;">
								<div class="alphaBg"> </div>
								<div class="megaBox">
									<div class="identificationBar">
										{$texts.SEND_RESULT_TO}: <span onclick="showhideLayers('megaBox')">X</span>
									</div>
									
									<div class="optionEmail" id="option1" style="display:block;">
									<ul class="menu">
										<li class="active"><a href="#" onclick="showLayer('option1');hideLayer('option2');hideLayer('option3');">{$texts.SEND_BY_EMAIL}</a></li>
										<li><a href="#" onclick="hideLayer('option1');showLayer('option2');hideLayer('option3');">{$texts.PRINT}</a></li>
										<li><a href="#" onclick="hideLayer('option1');hideLayer('option2');showLayer('option3');">Exportar</a></li>
									</ul>
									<h3>{$texts.SEND_BY_EMAIL}</h3>
										<form method="post" class="mailForm" action="mail.php" name="mailSend" onsubmit="return sendMail(this);">
		                                    <input type="hidden" name="lang" value="{$lang}"/>
		                                    <input type="hidden" name="from" value="{$from}"/>
		                                    <input type="hidden" name="count" value="{$config->documents_per_page}"/>
		                                    <input type="hidden" name="q" value="{$q_escaped}"/>
		                                    <input type="hidden" name="where" value="{$smarty.request.where}"/>
		                                    <input type="hidden" name="index" value="{$smarty.request.index}"/>
											
											<div class="radioOptions">
												<input class="" type="radio" name="option" value="from_to" checked="true"> {$texts.THIS_PAGE}
												<input class="" type="radio" name="option" value="selected"> {$texts.YOUR_SELECTION}
                                                (<span id="sizeOfBookmarks_2">0</span>)
                                            </div>
											<div class="formBox inputName" >
												<span>{$texts.MAIL_FROM_NAME}</span>
												<input name="senderName" class="formEmail" type="text">
											</div>
											<div class="formBox inputEmail" >
												<span>{$texts.MAIL_FROM_EMAIL}</span>
												<input name="senderMail" class="formEmail" type="text">
											</div>
											<div class="formBox inputFor" >
												<span>{$texts.MAIL_TO_EMAIL_LIST}</span>
												<input name="recipientMail" class="formEmail" type="text">
											</div>
		                                    <div class="formBox inputFor" >
		                                        <span>{$texts.MAIL_SUBJECT}</span>
		                                        <input name="subject" class="formEmail" type="text">
		                                    </div>
		
											<div class="formBox inputMessage" >
												<span>{$texts.MAIL_COMMENT}</span>
												<textarea name="comments" class="formEmail" cols="48"></textarea>
											</div>
											<div class="actions">
												<input type="button" class="submit" onclick="showhideLayers('megaBox')" value="{$texts.CANCEL}" name="cancel"/>
												<input type="submit" class="submit" value="{$texts.SEND}" name="send"/>
		                                    </div>
		                                    <span id="sendingMail" class="transmission" style="display:none;">{$texts.MAIL_SENDING}</span>
		                                    <span id="mailSent" class="transmission" style="display:none;">{$texts.MAIL_SENT}</span>
		                                    <span id="mailError" class="transmission" style="display:none;">{$texts.MAIL_ERROR}</span>
										</form>
									</div>
									<div class="optionPrint" id="option2" style="display:none;">
									<ul class="menu">
										<li><a href="#" onclick="showLayer('option1');hideLayer('option2');hideLayer('option3');">{$texts.SEND_BY_EMAIL}</a></li>
										<li class="active"><a href="#" onclick="hideLayer('option1');showLayer('option2');hideLayer('option3');">{$texts.PRINT}</a></li>
										<li><a href="#" onclick="hideLayer('option1');hideLayer('option2');showLayer('option3');">Exportar</a></li>
									</ul>
										<h3>{$texts.PRINT}</h3>
										<form name="printForm">
										    <div class="radioOptions">
												<input class="" type="radio" name="printOption" value="all" id="print_page" checked="true"> {$texts.THIS_PAGE}
												<input class="" type="radio" name="printOption" value="selection" id="print_selection""> {$texts.YOUR_SELECTION}
		                                    </div>
											<div class="actions">
												<input type="button" class="submit" onclick="showhideLayers('megaBox')" value="{$texts.CANCEL}" name="cancel"/>
												<input type="button" class="submit" onclick="printMode(printForm.printOption)" value="{$texts.PRINT}" name="go"/>
											</div>
		                                </form>
									</div>
									<div class="optionExport" id="option3" style="display:none;">
									<ul class="menu">
										<li><a href="#" onclick="showLayer('option1');hideLayer('option2');hideLayer('option3');">{$texts.SEND_BY_EMAIL}</a></li>
										<li><a href="#" onclick="hideLayer('option1');showLayer('option2');hideLayer('option3');">{$texts.PRINT}</a></li>
										<li class="active"><a href="#" onclick="hideLayer('option1');hideLayer('option2');showLayer('option3');">Exportar</a></li>
									</ul>
										<h3>{$texts.EXPORT_CITATIONS_RIS}</h3>
										<form name="exportForm">
										    <div class="exportOptions">
												<input class="" type="radio" name="exportOption" value="all" id="export_page" checked="true"> {$texts.THIS_PAGE}
												<input class="" type="radio" name="exportOption" value="selection" id="export_selection""> {$texts.YOUR_SELECTION}
		                                    </div>

											<div class="actions">
                                                <input type="button" class="submit" onclick="showhideLayers('megaBox')" value="{$texts.CANCEL}" name="cancel"/>
                                                <input type="button" class="submit" onclick="exportMode(exportForm.exportOption)" value="Exportar"/>
											</div>
										</form>
									</div>
								</div>
							</div>
						</div>
				</div>
    </div>
{/if}

<div class="resultSet">
    {if $fmt eq ''}
        {include file="result-doc.tpl"}
    {else}
        {include file="result-doc-$fmt.tpl"}
    {/if}

    {include file="result-navigation.tpl"}
</div>


<script language="JavaScript" type="text/javascript">recoverBookmarks();</script>
</div>

{/if}
