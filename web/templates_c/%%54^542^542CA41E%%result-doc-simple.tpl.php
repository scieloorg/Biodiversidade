<?php /* Smarty version 2.6.19, created on 2010-11-29 12:19:22
         compiled from result-doc-simple.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'debug', 'result-doc-simple.tpl', 2, false),array('function', 'occ', 'result-doc-simple.tpl', 26, false),array('function', 'translate', 'result-doc-simple.tpl', 75, false),array('modifier', 'substring_after', 'result-doc-simple.tpl', 8, false),array('modifier', 'contains', 'result-doc-simple.tpl', 36, false),array('modifier', 'count', 'result-doc-simple.tpl', 54, false),array('modifier', 'substring_before', 'result-doc-simple.tpl', 55, false),array('modifier', 'noaccent', 'result-doc-simple.tpl', 59, false),array('modifier', 'count_characters', 'result-doc-simple.tpl', 122, false),array('modifier', 'substr', 'result-doc-simple.tpl', 123, false),)), $this); ?>
<?php if (isset ( $_REQUEST['debug'] )): ?>
	<?php echo smarty_function_debug(array(), $this);?>

<?php endif; ?>

<?php $_from = $this->_tpl_vars['result']->response->docs; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }$this->_foreach['doclist'] = array('total' => count($_from), 'iteration' => 0);
if ($this->_foreach['doclist']['total'] > 0):
    foreach ($_from as $this->_tpl_vars['doc']):
        $this->_foreach['doclist']['iteration']++;
?>

		<?php $this->assign('refID', ((is_array($_tmp=$this->_tpl_vars['doc']->id)) ? $this->_run_mod_handler('substring_after', true, $_tmp, "-") : smarty_modifier_substring_after($_tmp, "-"))); ?>

<div id="<?php echo $this->_tpl_vars['doc']->id; ?>
" class="record">

	<div class="yourSelectionCheck">
		<a onclick="markUnmark(this.firstChild,'<?php echo $this->_tpl_vars['doc']->id; ?>
');"><img src="./image/common/box_unselected.gif" state="u" alt="<?php echo $this->_tpl_vars['texts']['MARK_DOCUMENT']; ?>
" title="<?php echo $this->_tpl_vars['texts']['MARK_DOCUMENT']; ?>
" /></a>
	</div>
	<div class="position">
		<?php echo ($this->_foreach['doclist']['iteration']-1)+$this->_tpl_vars['pagination']['from']; ?>
.
	</div>
	<div class="data">

		<!-- title -->
		<h3>
		<?php if ($this->_tpl_vars['doc']->db == 'LIS'): ?>
			<?php $this->assign('url', $this->_tpl_vars['doc']->ur[0]); ?>

			<a href="<?php echo $this->_tpl_vars['url']; ?>
" target="_blank">
				<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ti,'separator' => "/"), $this);?>

			</a>
        <?php elseif ($this->_tpl_vars['doc']->db == 'DECS'): ?>
            <?php $this->assign('ti', "ti_".($_REQUEST['lang'])); ?>

			<a href="decs_detail.php?term=<?php echo $this->_tpl_vars['doc']->{(($_var=$this->_tpl_vars['ti']) && substr($_var,0,2)!='__') ? $_var : $this->trigger_error("cannot access property \"$_var\"")}[0]; ?>
&lang=<?php echo $_REQUEST['lang']; ?>
" target="_blank">
				<?php echo $this->_tpl_vars['doc']->{(($_var=$this->_tpl_vars['ti']) && substr($_var,0,2)!='__') ? $_var : $this->trigger_error("cannot access property \"$_var\"")}[0]; ?>

			</a>

		<?php else: ?>
			<?php if (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, 'COCHRANE') : smarty_modifier_contains($_tmp, 'COCHRANE'))): ?>
				<a href="#" onclick="javascript:show_cochrane(this,'<?php echo $this->_tpl_vars['doc']->db; ?>
','<?php echo $this->_tpl_vars['doc']->id; ?>
')" target="_blank">
					<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ti,'separator' => "/"), $this);?>

				</a>
			<?php else: ?>
				<a href="resources/<?php echo $this->_tpl_vars['doc']->id; ?>
">
					<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ti,'separator' => "/"), $this);?>

				</a>
			<?php endif; ?>

		<?php endif; ?>
		</h3>
		<!-- author -->
		<?php echo smarty_function_occ(array('label' => $this->_tpl_vars['texts']['LABEL_AUTHOR'],'element' => $this->_tpl_vars['doc']->au,'separator' => ";",'class' => 'author'), $this);?>

		<!-- source -->
		<?php if (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, 'COCHRANE') : smarty_modifier_contains($_tmp, 'COCHRANE'))): ?>
			<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->db,'separator' => ";",'class' => 'source','suffix' => 'SOURCE_','translation' => $this->_tpl_vars['texts']), $this);?>

		<?php else: ?>
			<?php if (((is_array($_tmp=$this->_tpl_vars['doc']->fo[0])) ? $this->_run_mod_handler('count', true, $_tmp) : count($_tmp)) > 0): ?>
				<?php $this->assign('journal', ((is_array($_tmp=$this->_tpl_vars['doc']->fo[0])) ? $this->_run_mod_handler('substring_before', true, $_tmp, ";") : smarty_modifier_substring_before($_tmp, ";"))); ?>

				<?php if ($this->_tpl_vars['doc']->type == 'article' && ((is_array($_tmp=$this->_tpl_vars['journal'])) ? $this->_run_mod_handler('count', true, $_tmp) : count($_tmp)) > 0): ?>
					<div class="source">
						<a href="http://portal.revistas.bvs.br/transf.php?xsl=xsl/titles.xsl&xml=http://catserver.bireme.br/cgi-bin/wxis1660.exe/?IsisScript=../cgi-bin/catrevistas/catrevistas.xis|database_name=TITLES|list_type=title|cat_name=ALL|from=1|count=50&lang=pt&comefrom=home&home=false&task=show_magazines&request_made_adv_search=false&lang=pt&show_adv_search=false&help_file=/help_pt.htm&connector=ET&search_exp=<?php echo ((is_array($_tmp=$this->_tpl_vars['journal'])) ? $this->_run_mod_handler('noaccent', true, $_tmp) : smarty_modifier_noaccent($_tmp)); ?>
" target="_blank"><span><?php echo $this->_tpl_vars['journal']; ?>
</span></a>;
						<?php echo ((is_array($_tmp=$this->_tpl_vars['doc']->fo[0])) ? $this->_run_mod_handler('substring_after', true, $_tmp, ";") : smarty_modifier_substring_after($_tmp, ";")); ?>

					</div>
				<?php else: ?>
					<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->fo,'separator' => ";",'class' => 'source'), $this);?>

				<?php endif; ?>
			<?php endif; ?>
		<?php endif; ?>
		<!-- database -->
		<div class="database">
		</div>

		<!-- type -->
		<div class="source">
			<span class="type">
				<img src="image/common/type_<?php echo $this->_tpl_vars['doc']->type; ?>
.gif"/>
				<span><?php echo smarty_function_translate(array('text' => $this->_tpl_vars['doc']->type,'suffix' => 'TYPE_','translation' => $this->_tpl_vars['texts']), $this);?>
</span>
			</span>

            [<?php echo smarty_function_translate(array('text' => $this->_tpl_vars['doc']->db,'suffix' => 'DB_','translation' => $this->_tpl_vars['texts']), $this);?>

			<?php if (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, 'MEDLINE') : smarty_modifier_contains($_tmp, 'MEDLINE'))): ?>
				<span>PMID:</span> <?php echo ((is_array($_tmp=$this->_tpl_vars['doc']->id)) ? $this->_run_mod_handler('substring_after', true, $_tmp, "-") : smarty_modifier_substring_after($_tmp, "-")); ?>

            <?php elseif (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, 'COCHRANE') : smarty_modifier_contains($_tmp, 'COCHRANE'))): ?>
                 <span>ID:</span> <?php echo $this->_tpl_vars['doc']->id; ?>

            <?php elseif (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, "-") : smarty_modifier_contains($_tmp, "-"))): ?>
                <span>ID:</span> <?php echo ((is_array($_tmp=$this->_tpl_vars['doc']->id)) ? $this->_run_mod_handler('substring_after', true, $_tmp, "-") : smarty_modifier_substring_after($_tmp, "-")); ?>

            <?php elseif (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, 'campusvirtualsp') : smarty_modifier_contains($_tmp, 'campusvirtualsp'))): ?>
			<?php else: ?>
				<span>ID:</span> <?php echo $this->_tpl_vars['doc']->id; ?>

			<?php endif; ?>]
			
            <?php if (smarty_modifier_contains($this->_tpl_vars['doc']->services, 'LXP')): ?>
                <a onclick="LLXP(this,'<?php echo $this->_tpl_vars['lang']; ?>
')" title="LILACS Express" class="thickbox">
                    <span><img src="./image/common/icon_lilacs.gif"/></span>
                    &#160;LILACS Express
                </a>
            <?php endif; ?>

			<?php echo smarty_function_occ(array('label' => $this->_tpl_vars['texts']['LABEL_LANG'],'element' => $this->_tpl_vars['doc']->la,'separator' => ";",'translation' => $this->_tpl_vars['texts'],'suffix' => 'LANG_'), $this);?>

		</div>
		<!-- [pt] publication type -->
		<?php if (count($this->_tpl_vars['doc']->pt) > 0): ?>
			<div class="tags">
				<?php echo $this->_tpl_vars['texts']['LABEL_PUBLICATION']; ?>
:
				<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->pt,'separator' => ";"), $this);?>

			</div>
		<?php endif; ?>

		<!-- abstract -->
		<?php if (count($this->_tpl_vars['doc']->ab) > 0 || count($this->_tpl_vars['doc']->ab_pt) > 0 || count($this->_tpl_vars['doc']->ab_es) > 0 || count($this->_tpl_vars['doc']->ab_en) > 0): ?>
			<div class="description">

                <?php if ($this->_tpl_vars['doc']->db == 'DECS'): ?>
                    <?php $this->assign('ab', "ab_".($_REQUEST['lang'])); ?>
                    <?php ob_start(); ?>
                        <?php echo $this->_tpl_vars['doc']->{(($_var=$this->_tpl_vars['ab']) && substr($_var,0,2)!='__') ? $_var : $this->trigger_error("cannot access property \"$_var\"")}[0]; ?>

                    <?php $this->_smarty_vars['capture']['abstract'] = ob_get_contents(); ob_end_clean(); ?>
                <?php else: ?>
                    <?php ob_start(); ?>
                        <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ab,'separator' => "<hr/>"), $this);?>

                    <?php $this->_smarty_vars['capture']['abstract'] = ob_get_contents(); ob_end_clean(); ?>
                <?php endif; ?>

				<?php if (((is_array($_tmp=$this->_smarty_vars['capture']['abstract'])) ? $this->_run_mod_handler('count_characters', true, $_tmp) : smarty_modifier_count_characters($_tmp)) > 800 && $this->_tpl_vars['printMode'] != 'true'): ?>
					<?php $this->assign('ab1', ((is_array($_tmp=$this->_smarty_vars['capture']['abstract'])) ? $this->_run_mod_handler('substr', true, $_tmp, 0, 800) : substr($_tmp, 0, 800))); ?>
					<?php $this->assign('ab2', ((is_array($_tmp=$this->_smarty_vars['capture']['abstract'])) ? $this->_run_mod_handler('substr', true, $_tmp, 800) : substr($_tmp, 800))); ?>
					<span>
						<?php echo $this->_tpl_vars['ab1']; ?>

						<a href="#" onclick="$('#ab_<?php echo $this->_tpl_vars['doc']->id; ?>
').fadeIn('slow');$(this).css('display','none');return false">(<?php echo $this->_tpl_vars['texts']['MORE']; ?>
)</a>
						<span id="ab_<?php echo $this->_tpl_vars['doc']->id; ?>
" style="display:none;">
							<?php echo $this->_tpl_vars['ab2']; ?>

						</span>
					</span>
				<?php else: ?>
					<span>
						<?php echo $this->_smarty_vars['capture']['abstract']; ?>

					</span>
				<?php endif; ?>
			</div>
		<?php endif; ?>

		<!-- subject -->
		<?php if (count($this->_tpl_vars['doc']->mh) > 0): ?>
			<div class="tags">
				<?php echo $this->_tpl_vars['texts']['LABEL_SUBJECT']; ?>
:
				<?php $_from = $this->_tpl_vars['doc']->mh; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['mhKey'] => $this->_tpl_vars['mh']):
?>
					<a href="#" onclick="javascript:refineByIndex('<?php echo $this->_tpl_vars['mh']; ?>
','mh')"><?php echo $this->_tpl_vars['mh']; ?>
</a>
				<?php endforeach; endif; unset($_from); ?>
			</div>
		<?php endif; ?>

	</div>
	<div class="spacer"></div>

    <div class="user-actions">
         <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "doc-actions-bar.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    </div>

</div>
<?php endforeach; endif; unset($_from); ?>