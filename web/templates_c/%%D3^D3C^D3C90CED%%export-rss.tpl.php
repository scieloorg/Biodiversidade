<?php /* Smarty version 2.6.19, created on 2010-11-24 15:41:00
         compiled from export-rss.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'iahlinks', 'export-rss.tpl', 14, false),array('function', 'occ', 'export-rss.tpl', 18, false),array('modifier', 'count', 'export-rss.tpl', 22, false),array('modifier', 'replace', 'export-rss.tpl', 23, false),)), $this); ?>
<?php echo '<?xml'; ?>
 version="1.0" encoding="UTF-8"<?php echo '?>'; ?>


<rss version="2.0">
	<channel>
		<title><?php echo $this->_tpl_vars['texts']['TITLE']; ?>
: <?php echo $_REQUEST['q']; ?>
</title>
		<link><?php echo $this->_tpl_vars['url']; ?>
</link>
		<description><?php echo $this->_tpl_vars['texts']['DESCRIPTION']; ?>
</description>

		<?php $_from = $this->_tpl_vars['result']->response->docs; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['doc']):
?>

			<?php ob_start(); ?>
				<?php echo smarty_function_iahlinks(array('scielo' => $this->_tpl_vars['links']->response->docs,'document' => $this->_tpl_vars['doc']->ur,'id' => $this->_tpl_vars['doc']->id,'lang' => $this->_tpl_vars['lang']), $this);?>

			<?php $this->_smarty_vars['capture']['scieloLinks'] = ob_get_contents(); ob_end_clean(); ?>

			<item>
				<title><![CDATA[<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ti,'separator' => "/"), $this);?>
]]></title>
				<author><![CDATA[<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->au,'separator' => ";"), $this);?>
]]></author>
            	<source><![CDATA[<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->fo,'separator' => ";"), $this);?>
]]></source>

				<?php if (count($this->_tpl_vars['scieloLinkList']) > 0): ?>
					<link><?php echo ((is_array($_tmp=$this->_tpl_vars['scieloLinkList'][0])) ? $this->_run_mod_handler('replace', true, $_tmp, "&", "&amp;") : smarty_modifier_replace($_tmp, "&", "&amp;")); ?>
</link>
				<?php elseif (count($this->_tpl_vars['doc']->ur) > 0): ?>
					<link><?php echo ((is_array($_tmp=$this->_tpl_vars['doc']->ur[0])) ? $this->_run_mod_handler('replace', true, $_tmp, "&", "&amp;") : smarty_modifier_replace($_tmp, "&", "&amp;")); ?>
</link>
				<?php else: ?>
					<link><?php echo $this->_tpl_vars['url']; ?>
?detail=1&amp;q=id:<?php echo $this->_tpl_vars['doc']->id; ?>
</link>
				<?php endif; ?>

				<description>
					<![CDATA[
                        <?php if (isset ( $this->_tpl_vars['doc']->au )): ?>
                            <?php echo $this->_tpl_vars['texts']['LABEL_AUTHOR']; ?>
: <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->au,'separator' => ";"), $this);?>

                        <?php endif; ?>
                        <?php if (isset ( $this->_tpl_vars['doc']->fo )): ?>
                            <p><?php echo $this->_tpl_vars['texts']['LABEL_SOURCE']; ?>
: <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->fo,'separator' => ";"), $this);?>
</p>
                        <?php endif; ?>
						<?php if (isset ( $this->_tpl_vars['doc']->ab )): ?>
							<span class="abstract"><p><?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ab,'separator' => "/"), $this);?>
</p></span>
						<?php endif; ?>
                        <?php if (isset ( $this->_tpl_vars['doc']->mh )): ?>
                            <p>
                                <?php echo $this->_tpl_vars['texts']['LABEL_SUBJECT']; ?>
:
                                <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->mh,'separator' => ";"), $this);?>

                            </p>
                        <?php endif; ?>
					]]>
				</description>
			</item>
		<?php endforeach; endif; unset($_from); ?>
	</channel>
</rss>