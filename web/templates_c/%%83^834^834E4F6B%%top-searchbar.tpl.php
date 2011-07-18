<?php /* Smarty version 2.6.19, created on 2010-11-10 07:43:43
         compiled from top-searchbar.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'count', 'top-searchbar.tpl', 39, false),array('modifier', 'upper', 'top-searchbar.tpl', 47, false),array('modifier', 'replace', 'top-searchbar.tpl', 68, false),)), $this); ?>
		<div class="resultsFor">
			<a href="<?php echo $this->_tpl_vars['config']->home_url; ?>
?lang=<?php echo $this->_tpl_vars['lang']; ?>
"><?php echo $this->_tpl_vars['texts']['BVS_HOME']; ?>
</a> >
			<a href="<?php echo $_SERVER['PHP_SELF']; ?>
?lang=<?php echo $this->_tpl_vars['lang']; ?>
"><?php echo $this->_tpl_vars['texts']['SEARCH_HOME']; ?>
</a>

		<?php 
			global $q, $filter, $filter_chain, $filterLabel, $texts;

			// caso tenha filtro inicial e foi informado label mostra na barra de navegacao
			if ($filter != '' && $filterLabel != ''){
				print "> <a href=\"#\" onclick=\"javascript:backHistoryFilter('-2')\">" . $filterLabel . "</a> ";
				if ($q != '') print " > ";
			}
			if ($q != '' && $filterLabel == ''){
				$q = preg_replace("/\+id:.*?$/",$texts['YOUR_SELECTION'],$q);
                $q = str_replace("\\\"","&quot;",$q);

				print "> <a href=\"#\" onclick=\"javascript:backHistoryFilter('-1')\">" . $q . "</a>";
			}

			for($f = 0; $f < count($filter_chain); $f++ ){
				$filterHistory = $filter_chain[$f];
				if ($filterHistory != ""){
					$filterHistorySplit = split(":", $filterHistory);
					$filterHistoryLabel = stripslashes($filterHistorySplit[1]);
					$filterHistoryLabel = ereg_replace("\"","", $filterHistoryLabel);

					if ($f == ( count($filter_chain)-1) ){
						print " > " . $filterHistoryLabel;
					}else{
						print " > <a href=\"#\" onclick=\"javascript:backHistoryFilter('" . $f . "')\">" . $filterHistoryLabel . "</a>";
					}
				}
			}
		 ?>
		</div>

		<div class="search">
			<form name="searchForm" action="<?php echo $_SERVER['PHP_SELF']; ?>
" method="post">
 				<?php if (count($this->_tpl_vars['config']->search_collection_list->collection) > 1): ?>
				  <div class="informationTypes">
					<?php $_from = $this->_tpl_vars['config']->search_collection_list->collection; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }$this->_foreach['colIterator'] = array('total' => count($_from), 'iteration' => 0);
if ($this->_foreach['colIterator']['total'] > 0):
    foreach ($_from as $this->_tpl_vars['collection']):
        $this->_foreach['colIterator']['iteration']++;
?>
						<?php $this->assign('colName', $this->_tpl_vars['collection']->name); ?>
						<?php $this->assign('colSite', $this->_tpl_vars['collection']->site); ?>

						<?php if ($this->_tpl_vars['colSite'] == ''): ?>
							<?php $this->assign('colSite', $this->_tpl_vars['config']->site); ?>
							<?php $this->assign('colId', ((is_array($_tmp=$this->_tpl_vars['colName'])) ? $this->_run_mod_handler('upper', true, $_tmp) : smarty_modifier_upper($_tmp))); ?>
						<?php else: ?>
							<?php $this->assign('colId', ((is_array($_tmp=($this->_tpl_vars['colName'])."-".($this->_tpl_vars['colSite']))) ? $this->_run_mod_handler('upper', true, $_tmp) : smarty_modifier_upper($_tmp))); ?>
						<?php endif; ?>

						<?php if (( $this->_tpl_vars['col'] == $this->_tpl_vars['colName'] && $this->_tpl_vars['site'] == $this->_tpl_vars['colSite'] )): ?>
							<?php $this->assign('selectColPos', ($this->_foreach['colIterator']['iteration']-1)); ?>

							<a href="#" onclick="changeCollection('<?php echo $this->_tpl_vars['colName']; ?>
','<?php echo $this->_tpl_vars['colSite']; ?>
')" class="selected"><?php echo $this->_tpl_vars['texts']['COLLECTIONS'][$this->_tpl_vars['colId']]; ?>
</a>
						<?php else: ?>
							<a href="#" onclick="changeCollection('<?php echo $this->_tpl_vars['colName']; ?>
','<?php echo $this->_tpl_vars['colSite']; ?>
')"><?php echo $this->_tpl_vars['texts']['COLLECTIONS'][$this->_tpl_vars['colId']]; ?>
</a>
						<?php endif; ?>
					<?php endforeach; endif; unset($_from); ?>
				  </div>
				<?php endif; ?>

				<div class="searchForm">
						<input type="hidden" name="lang" value="<?php echo $this->_tpl_vars['lang']; ?>
"/>
						<input type="hidden" name="col" value="<?php echo $this->_tpl_vars['col']; ?>
"/>
						<input type="hidden" name="site" value="<?php echo $this->_tpl_vars['site']; ?>
"/>
						<input type="hidden" name="count" value="<?php echo $this->_tpl_vars['config']->documents_per_page; ?>
"/>
						<input type="hidden" name="filter" value="<?php echo ((is_array($_tmp=$this->_tpl_vars['filter'])) ? $this->_run_mod_handler('replace', true, $_tmp, "\\\"", "&quot;") : smarty_modifier_replace($_tmp, "\\\"", "&quot;")); ?>
"/>
						<input type="hidden" name="filterLabel" value="<?php echo $this->_tpl_vars['filterLabel']; ?>
"/>
						<input type="hidden" name="qt" value="standard"/>
                        <input type="hidden" name="fmt" value="<?php echo $this->_tpl_vars['fmt']; ?>
"/>
                        <input type="hidden" name="sort" value="<?php echo $_REQUEST['sort']; ?>
"/>

						<!-- fields used by javascript functions -->
						<input type="hidden" name="pageFrom" value="<?php echo $this->_tpl_vars['from']; ?>
"/>
						<input type="hidden" name="from" value=""/>
						<input type="hidden" name="addfilter" value=""/>
						<input type="hidden" name="backfilter" value=""/>
						<input type="hidden" name="printMode" value=""/>
						<input type="hidden" name="output" value=""/>
						<input type="hidden" name="fb" value=""/>


						<?php if (isset ( $_REQUEST['debug'] )): ?>
							<input type="hidden" name="debug" value="1"/>
						<?php endif; ?>

						<?php $_from = $this->_tpl_vars['filter_chain']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['filterValue']):
?>
							<?php $this->assign('fvalue', ((is_array($_tmp=$this->_tpl_vars['filterValue'])) ? $this->_run_mod_handler('replace', true, $_tmp, "\\\"", "&quot;") : smarty_modifier_replace($_tmp, "\\\"", "&quot;"))); ?>
							<input type="hidden" name="filter_chain[]" value="<?php echo $this->_tpl_vars['fvalue']; ?>
">
						<?php endforeach; endif; unset($_from); ?>
						<!--span><?php echo $this->_tpl_vars['texts']['SEARCH_WORDS']; ?>
</span-->

						<input type="text" name="q" value="<?php if ($this->_tpl_vars['q_escaped'] == ''): ?><?php echo $this->_tpl_vars['texts']['ENTER_WORDS']; ?>
<?php else: ?><?php echo $this->_tpl_vars['q_escaped']; ?>
<?php endif; ?>" class="inputText defaultValue" onKeyDown="if(event.keyCode==13) newSearch();" onblur="clearDefault('textEntry1', 'inputText defaultValue'); this.value= (this.value=='')? 'Entre uma ou mais palavras' : this.value" onfocus="clearDefault('textEntry1', 'inputText'); this.value= (this.value=='Entre uma ou mais palavras')? '' : this.value"  id="textEntry1"/>

						<select name="index" class="inputText">
							<?php $_from = $this->_tpl_vars['colectionData']->index_list->index; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['availableIndex']):
?>
								<?php $this->assign('indexKey', ((is_array($_tmp=$this->_tpl_vars['availableIndex']->name)) ? $this->_run_mod_handler('upper', true, $_tmp) : smarty_modifier_upper($_tmp))); ?>
								<?php $this->assign('indexPrefix', $this->_tpl_vars['availableIndex']->prefix); ?>

								<?php if ($this->_tpl_vars['indexKey'] != ''): ?>
									<?php if ($this->_tpl_vars['indexPrefix'] == $this->_tpl_vars['index']): ?>
										<option value="<?php echo $this->_tpl_vars['indexPrefix']; ?>
" selected="1"><?php echo $this->_tpl_vars['texts']['INDEXES'][$this->_tpl_vars['indexKey']]; ?>
</option>
									<?php else: ?>
										<option value="<?php echo $this->_tpl_vars['indexPrefix']; ?>
"><?php echo $this->_tpl_vars['texts']['INDEXES'][$this->_tpl_vars['indexKey']]; ?>
</option>
									<?php endif; ?>
								<?php endif; ?>
							<?php endforeach; endif; unset($_from); ?>
						</select>

						<?php if (count($this->_tpl_vars['colectionData']->where_list->where) > 0): ?>
							<?php echo $this->_tpl_vars['texts']['WHERE_FILTER']; ?>
:
							<select name="where" class="inputText">
								<?php $_from = $this->_tpl_vars['colectionData']->where_list->where; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['where']):
?>
									<?php echo ''; ?><?php $this->assign('whereName', ((is_array($_tmp=$this->_tpl_vars['where']->name)) ? $this->_run_mod_handler('upper', true, $_tmp) : smarty_modifier_upper($_tmp))); ?><?php echo ''; ?><?php $this->assign('whereFilter', $this->_tpl_vars['where']->filter); ?><?php echo ''; ?><?php $this->assign('whereLevel', $this->_tpl_vars['where']->level); ?><?php echo ''; ?><?php if ($this->_tpl_vars['texts']['WHERE'][$this->_tpl_vars['whereName']] != ''): ?><?php echo ''; ?><?php $this->assign('whereLabel', $this->_tpl_vars['texts']['WHERE'][$this->_tpl_vars['whereName']]); ?><?php echo ''; ?><?php else: ?><?php echo ''; ?><?php $this->assign('whereLabel', $this->_tpl_vars['whereName']); ?><?php echo ''; ?><?php endif; ?><?php echo ''; ?><?php if ($this->_tpl_vars['whereLevel'] != ''): ?><?php echo ''; ?><?php $this->assign('ident', '&nbsp;&nbsp;&nbsp;&nbsp;'); ?><?php echo ''; ?><?php else: ?><?php echo ''; ?><?php $this->assign('ident', ''); ?><?php echo ''; ?><?php endif; ?><?php echo ''; ?><?php if ($this->_tpl_vars['whereName'] != ''): ?><?php echo ''; ?><?php if ($this->_tpl_vars['whereName'] == $_REQUEST['where']): ?><?php echo '<option value="'; ?><?php echo $this->_tpl_vars['whereName']; ?><?php echo '" selected="1">'; ?><?php echo $this->_tpl_vars['ident']; ?><?php echo ''; ?><?php echo $this->_tpl_vars['whereLabel']; ?><?php echo '</option>'; ?><?php else: ?><?php echo '<option value="'; ?><?php echo $this->_tpl_vars['whereName']; ?><?php echo '">'; ?><?php echo $this->_tpl_vars['ident']; ?><?php echo ''; ?><?php echo $this->_tpl_vars['whereLabel']; ?><?php echo '</option>'; ?><?php endif; ?><?php echo ''; ?><?php endif; ?><?php echo ''; ?>

								<?php endforeach; endif; unset($_from); ?>
							</select>
						<?php endif; ?>

						<input type="button" name="go" value="<?php echo $this->_tpl_vars['texts']['SEARCH_SUBMIT']; ?>
" class="submit" onclick="javascript:newSearch()" />
						<!--
						&#160;
						<a href="#"><?php echo '<?='; ?>
$texts['SEARCH_ADVANCED']<?php echo '?>'; ?>
</a>
						-->
				</div>

				<div id="bookmark_button">
					<!--img src="./image/common/star_selected.gif" onclick="showBookmarks()";/-->
				</div>
			</form>
		</div>