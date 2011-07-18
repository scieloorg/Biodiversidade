<?php /* Smarty version 2.6.19, created on 2010-11-10 07:43:43
         compiled from result.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'upper', 'result.tpl', 97, false),array('modifier', 'count', 'result.tpl', 111, false),array('modifier', 'strip', 'result.tpl', 117, false),)), $this); ?>
<?php if ($this->_tpl_vars['result'] == ''): ?>
	<div class="noResults">
		<?php echo $this->_tpl_vars['texts']['COLLECTION_UNAVAILABLE']; ?>

	</div>
<?php elseif (isset ( $this->_tpl_vars['result']->response->connection_problem )): ?>
	<div class="noResults">
		<?php echo $this->_tpl_vars['texts']['CONNECTION_ERROR']; ?>

	</div>
<?php elseif ($this->_tpl_vars['numFound'] == '0'): ?>
	<div class="noResults">
		<?php echo $this->_tpl_vars['texts']['NO_RESULTS']; ?>

	</div>
<?php else: ?>

<div class="results">

	<div class="resultServices">
		<div id="searchHistory" class="searchHistory closed">
		<h4>
			<a onclick="showHideBox('searchHistory');" title="<?php echo $this->_tpl_vars['texts']['SHOW_HIDE']; ?>
">
				<span><?php echo $this->_tpl_vars['texts']['HISTORY']; ?>
</span>&#160;
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
				<span><?php echo $this->_tpl_vars['texts']['OPERATORS']; ?>
</span>
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
			<a onclick="showHideBox('yourSelection')" title="<?php echo $this->_tpl_vars['texts']['SHOW_HIDE']; ?>
">
				<span><?php echo $this->_tpl_vars['texts']['YOUR_SELECTION']; ?>
</span>&#160;
				(<span id="sizeOfBookmarks_0"></span>)
			</a>
		</h4>
		<div class="selection bContent">
			<ul class="showBox">
			<p>
				<?php echo $this->_tpl_vars['texts']['SELECTION']['YOU_HAVE']; ?>
&#160;<span id="sizeOfBookmarks_1">0</span>&#160;<?php echo $this->_tpl_vars['texts']['SELECTION_REGISTERS']; ?>
.
			</p>
				<li><a onclick="showBookmarks()"><?php echo $this->_tpl_vars['texts']['SELECTION_LIST_REGISTERS']; ?>
</a></li>
				<li><a onclick="clearBookmarks()" href="index.php?"><?php echo $this->_tpl_vars['texts']['SELECTION_CLEAR_LIST']; ?>
</a></li>
			</ul>
			<span class="arrowBox"></span>
		</div>
	</div>

	<div class="refineSearch" id="refineSearch">
		<!--h4><a href="#" onclick="showHideBox('refineSearch')" title="<?php echo $this->_tpl_vars['texts']['SHOW_HIDE']; ?>
"><span><?php echo $this->_tpl_vars['texts']['REFINE']; ?>
</span></a></h4-->
		<div class="collapseAll" onclick="expandRetractResults('retract')">
			<img src="image/common/resultServices_minus_icon2.jpg" alt="Collapse All"/>
			&#160;<?php echo $this->_tpl_vars['texts']['RETRACT_ALL']; ?>

		</div>
		<div class="expandAll" onclick="expandRetractResults('expand')">
			<img src="image/common/resultServices_plus_icon2.jpg" alt="Expand All"/>
			&#160;<?php echo $this->_tpl_vars['texts']['EXPAND_ALL']; ?>

		</div>

		<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "result-clusters.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

	</div>
    <div></div>


</div>
<?php if ($this->_tpl_vars['numFound'] > 0): ?>
    <div class="resultOptions">
				<div class="resultNavigation"><?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "result-navigation.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?></div>
				<div class="resultsBar">
						<div class="selectAll" id="selectAll">
							<input type="button" value="<?php echo $this->_tpl_vars['texts']['SELECT_PAGE']; ?>
" onclick="markAll(); showhideLayers('selectAll');showhideLayers('clearAll')" />
						</div>
	                    <div class="clearAll" id="clearAll" style="display: none">
	                        <input type="button" value="<?php echo $this->_tpl_vars['texts']['UNSELECT_PAGE']; ?>
" onclick="unmarkAll();showhideLayers('clearAll');showhideLayers('selectAll')" />
	                    </div>
						<div class="orderBy">
							
							<select name="sortBy" class="inputText" onchange="javascript:changeOrderBy(this);">
								<option value=""><?php echo $this->_tpl_vars['texts']['SORT_OPTIONS']; ?>
</option>
								<?php $_from = $this->_tpl_vars['colectionData']->sort_list->sort; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['sortItem']):
?>
									<?php $this->assign('sortName', ((is_array($_tmp=$this->_tpl_vars['sortItem']->name)) ? $this->_run_mod_handler('upper', true, $_tmp) : smarty_modifier_upper($_tmp))); ?>
									<?php $this->assign('sortValue', $this->_tpl_vars['sortItem']->value); ?>
	
									<?php if ($this->_tpl_vars['sortName'] != ''): ?>
										<?php if ($this->_tpl_vars['sortName'] == $_REQUEST['sort']): ?>
											<option value="<?php echo $this->_tpl_vars['sortName']; ?>
" selected="1"><?php echo $this->_tpl_vars['texts']['SORT'][$this->_tpl_vars['sortName']]; ?>
</option>
										<?php else: ?>
											<option value="<?php echo $this->_tpl_vars['sortName']; ?>
"><?php echo $this->_tpl_vars['texts']['SORT'][$this->_tpl_vars['sortName']]; ?>
</option>
										<?php endif; ?>
									<?php endif; ?>
								<?php endforeach; endif; unset($_from); ?>
							</select>
						</div>
	
	                    <?php if (count($this->_tpl_vars['colectionData']->format_list->format) > 0): ?>
	                        <div class="format">
	                            
	                            <select name="fmt" class="inputText" onchange="javascript:changeDisplayFormat(this);">
									<option value=""><?php echo $this->_tpl_vars['texts']['FORMAT_OPTIONS']; ?>
</option>								
	                                <?php $_from = $this->_tpl_vars['colectionData']->format_list->format; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['formatItem']):
?>
	                                    <?php $this->assign('formatName', ((is_array($_tmp=$this->_tpl_vars['formatItem']->name)) ? $this->_run_mod_handler('strip', true, $_tmp) : smarty_modifier_strip($_tmp))); ?>
	                                    <?php $this->assign('textsDisplay', $this->_tpl_vars['texts']['DISPLAY']); ?>
	
	                                    <?php if ($this->_tpl_vars['formatName'] != ''): ?>
	                                        <?php if ($this->_tpl_vars['formatName'] == $_REQUEST['fmt']): ?>
	                                            <option value="<?php echo $this->_tpl_vars['formatName']; ?>
" selected="1"><?php echo $this->_tpl_vars['texts']['DISPLAY'][$this->_tpl_vars['formatName']]; ?>
</option>
	                                        <?php else: ?>
	                                            <option value="<?php echo $this->_tpl_vars['formatName']; ?>
"><?php echo $this->_tpl_vars['texts']['DISPLAY'][$this->_tpl_vars['formatName']]; ?>
</option>
	                                        <?php endif; ?>
	                                    <?php endif; ?>
	                                <?php endforeach; endif; unset($_from); ?>
	                            </select>
	                        </div>
	                    <?php endif; ?>
	
						<div class="feed">
							<a class="RSS" href="index.php?output=rss&site=<?php echo $this->_tpl_vars['site']; ?>
&col=<?php echo $this->_tpl_vars['col']; ?>
&lang=<?php echo $this->_tpl_vars['lang']; ?>
<?php echo $this->_tpl_vars['getParams']; ?>
"><span>RSS</span></a>
							<a class="XML" href="index.php?output=xml&site=<?php echo $this->_tpl_vars['site']; ?>
&col=<?php echo $this->_tpl_vars['col']; ?>
&lang=<?php echo $this->_tpl_vars['lang']; ?>
<?php echo $this->_tpl_vars['getParams']; ?>
"><span>XML</span></a>
						</div>
						<div class="export">
							<a href="#" onclick="showhideLayers('megaBox')"><?php echo $this->_tpl_vars['texts']['SEND_RESULT']; ?>
</a>
							<div id="megaBox" class="emailBox boxContent" style="display:none;">
								<div class="alphaBg"> </div>
								<div class="megaBox">
									<div class="identificationBar">
										<?php echo $this->_tpl_vars['texts']['SEND_RESULT_TO']; ?>
: <span onclick="showhideLayers('megaBox')">X</span>
									</div>
									
									<div class="optionEmail" id="option1" style="display:block;">
									<ul class="menu">
										<li class="active"><a href="#" onclick="showLayer('option1');hideLayer('option2');hideLayer('option3');"><?php echo $this->_tpl_vars['texts']['SEND_BY_EMAIL']; ?>
</a></li>
										<li><a href="#" onclick="hideLayer('option1');showLayer('option2');hideLayer('option3');"><?php echo $this->_tpl_vars['texts']['PRINT']; ?>
</a></li>
										<li><a href="#" onclick="hideLayer('option1');hideLayer('option2');showLayer('option3');">Exportar</a></li>
									</ul>
									<h3><?php echo $this->_tpl_vars['texts']['SEND_BY_EMAIL']; ?>
</h3>
										<form method="post" class="mailForm" action="mail.php" name="mailSend" onsubmit="return sendMail(this);">
		                                    <input type="hidden" name="lang" value="<?php echo $this->_tpl_vars['lang']; ?>
"/>
		                                    <input type="hidden" name="from" value="<?php echo $this->_tpl_vars['from']; ?>
"/>
		                                    <input type="hidden" name="count" value="<?php echo $this->_tpl_vars['config']->documents_per_page; ?>
"/>
		                                    <input type="hidden" name="q" value="<?php echo $this->_tpl_vars['q_escaped']; ?>
"/>
		                                    <input type="hidden" name="where" value="<?php echo $_REQUEST['where']; ?>
"/>
		                                    <input type="hidden" name="index" value="<?php echo $_REQUEST['index']; ?>
"/>
											
											<div class="radioOptions">
												<input class="" type="radio" name="option" value="from_to" checked="true"> <?php echo $this->_tpl_vars['texts']['THIS_PAGE']; ?>

												<input class="" type="radio" name="option" value="selected"> <?php echo $this->_tpl_vars['texts']['YOUR_SELECTION']; ?>

                                                (<span id="sizeOfBookmarks_2">0</span>)
                                            </div>
											<div class="formBox inputName" >
												<span><?php echo $this->_tpl_vars['texts']['MAIL_FROM_NAME']; ?>
</span>
												<input name="senderName" class="formEmail" type="text">
											</div>
											<div class="formBox inputEmail" >
												<span><?php echo $this->_tpl_vars['texts']['MAIL_FROM_EMAIL']; ?>
</span>
												<input name="senderMail" class="formEmail" type="text">
											</div>
											<div class="formBox inputFor" >
												<span><?php echo $this->_tpl_vars['texts']['MAIL_TO_EMAIL_LIST']; ?>
</span>
												<input name="recipientMail" class="formEmail" type="text">
											</div>
		                                    <div class="formBox inputFor" >
		                                        <span><?php echo $this->_tpl_vars['texts']['MAIL_SUBJECT']; ?>
</span>
		                                        <input name="subject" class="formEmail" type="text">
		                                    </div>
		
											<div class="formBox inputMessage" >
												<span><?php echo $this->_tpl_vars['texts']['MAIL_COMMENT']; ?>
</span>
												<textarea name="comments" class="formEmail" cols="48"></textarea>
											</div>
											<div class="actions">
												<input type="button" class="submit" onclick="showhideLayers('megaBox')" value="<?php echo $this->_tpl_vars['texts']['CANCEL']; ?>
" name="cancel"/>
												<input type="submit" class="submit" value="<?php echo $this->_tpl_vars['texts']['SEND']; ?>
" name="send"/>
		                                    </div>
		                                    <span id="sendingMail" class="transmission" style="display:none;"><?php echo $this->_tpl_vars['texts']['MAIL_SENDING']; ?>
</span>
		                                    <span id="mailSent" class="transmission" style="display:none;"><?php echo $this->_tpl_vars['texts']['MAIL_SENT']; ?>
</span>
		                                    <span id="mailError" class="transmission" style="display:none;"><?php echo $this->_tpl_vars['texts']['MAIL_ERROR']; ?>
</span>
										</form>
									</div>
									<div class="optionPrint" id="option2" style="display:none;">
									<ul class="menu">
										<li><a href="#" onclick="showLayer('option1');hideLayer('option2');hideLayer('option3');"><?php echo $this->_tpl_vars['texts']['SEND_BY_EMAIL']; ?>
</a></li>
										<li class="active"><a href="#" onclick="hideLayer('option1');showLayer('option2');hideLayer('option3');"><?php echo $this->_tpl_vars['texts']['PRINT']; ?>
</a></li>
										<li><a href="#" onclick="hideLayer('option1');hideLayer('option2');showLayer('option3');">Exportar</a></li>
									</ul>
										<h3><?php echo $this->_tpl_vars['texts']['PRINT']; ?>
</h3>
										<form name="printForm">
										    <div class="radioOptions">
												<input class="" type="radio" name="printOption" value="all" id="print_page" checked="true"> <?php echo $this->_tpl_vars['texts']['THIS_PAGE']; ?>

												<input class="" type="radio" name="printOption" value="selection" id="print_selection""> <?php echo $this->_tpl_vars['texts']['YOUR_SELECTION']; ?>

		                                    </div>
											<div class="actions">
												<input type="button" class="submit" onclick="showhideLayers('megaBox')" value="<?php echo $this->_tpl_vars['texts']['CANCEL']; ?>
" name="cancel"/>
												<input type="button" class="submit" onclick="printMode(printForm.printOption)" value="<?php echo $this->_tpl_vars['texts']['PRINT']; ?>
" name="go"/>
											</div>
		                                </form>
									</div>
									<div class="optionExport" id="option3" style="display:none;">
									<ul class="menu">
										<li><a href="#" onclick="showLayer('option1');hideLayer('option2');hideLayer('option3');"><?php echo $this->_tpl_vars['texts']['SEND_BY_EMAIL']; ?>
</a></li>
										<li><a href="#" onclick="hideLayer('option1');showLayer('option2');hideLayer('option3');"><?php echo $this->_tpl_vars['texts']['PRINT']; ?>
</a></li>
										<li class="active"><a href="#" onclick="hideLayer('option1');hideLayer('option2');showLayer('option3');">Exportar</a></li>
									</ul>
										<h3><?php echo $this->_tpl_vars['texts']['EXPORT_CITATIONS_RIS']; ?>
</h3>
										<form name="exportForm">
										    <div class="exportOptions">
												<input class="" type="radio" name="exportOption" value="all" id="export_page" checked="true"> <?php echo $this->_tpl_vars['texts']['THIS_PAGE']; ?>

												<input class="" type="radio" name="exportOption" value="selection" id="export_selection""> <?php echo $this->_tpl_vars['texts']['YOUR_SELECTION']; ?>

		                                    </div>

											<div class="actions">
                                                <input type="button" class="submit" onclick="showhideLayers('megaBox')" value="<?php echo $this->_tpl_vars['texts']['CANCEL']; ?>
" name="cancel"/>
                                                <input type="button" class="submit" onclick="exportMode(exportForm.exportOption)" value="Exportar"/>
											</div>
										</form>
									</div>
								</div>
							</div>
						</div>
				</div>
    </div>
<?php endif; ?>

<div class="resultSet">
    <?php if ($this->_tpl_vars['fmt'] == ''): ?>
        <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "result-doc.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <?php else: ?>
        <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "result-doc-".($this->_tpl_vars['fmt']).".tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    <?php endif; ?>

    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "result-navigation.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
</div>


<script language="JavaScript" type="text/javascript">recoverBookmarks();</script>
</div>

<?php endif; ?>