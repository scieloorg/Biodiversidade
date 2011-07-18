<?php /* Smarty version 2.6.19, created on 2010-11-10 07:43:43
         compiled from top-banner.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'lower', 'top-banner.tpl', 13, false),)), $this); ?>

	<div class="parent">
		<a href="<?php echo $this->_tpl_vars['config']->bvs_url; ?>
">
			<img src="./image/<?php echo $this->_tpl_vars['lang']; ?>
/logo_bvs.gif" alt="<?php echo $this->_tpl_vars['texts']['vhl_alternate']; ?>
" title="<?php echo $this->_tpl_vars['texts']['vhl_alternate']; ?>
" />
		</a>
	</div>
	<div class="identification">
		<h2><?php echo $this->_tpl_vars['texts']['BVS_TITLE']; ?>
</h2>
		<h1><?php echo $this->_tpl_vars['texts']['TITLE']; ?>
</h1>
	</div>
	<div class="otherVersions">
		<?php $_from = $this->_tpl_vars['texts']['AVAILABLE_LANGUAGES']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['langcode'] => $this->_tpl_vars['language']):
?>
			<?php if (((is_array($_tmp=$this->_tpl_vars['langcode'])) ? $this->_run_mod_handler('lower', true, $_tmp) : smarty_modifier_lower($_tmp)) == $this->_tpl_vars['lang']): ?>
				<?php $this->assign('class', " class='selected'"); ?>
			<?php else: ?>
				<?php $this->assign('class', ""); ?>
			<?php endif; ?>
			<a href="#" onclick="searchForm.q.value='';changeFormParameter('lang','<?php echo ((is_array($_tmp=$this->_tpl_vars['langcode'])) ? $this->_run_mod_handler('lower', true, $_tmp) : smarty_modifier_lower($_tmp)); ?>
');" <?php echo $this->_tpl_vars['class']; ?>
><?php echo $this->_tpl_vars['language']; ?>
</a>
		<?php endforeach; endif; unset($_from); ?>
	</div>
	<div class="spacer">&#160;</div>