<?php /* Smarty version 2.6.19, created on 2010-11-29 13:19:28
         compiled from email-body.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'occ', 'email-body.tpl', 11, false),)), $this); ?>

<div class="results">
	<div class="resultSet">
	<?php $_from = $this->_tpl_vars['result']->response->docs; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['doc']):
?>
			<table width="90%">
				<tr valign="top">
					<td colspan="2">
						<br/>
						<font size="4" color="#0068CF">
							<a href="<?php echo $this->_tpl_vars['url']; ?>
resources/<?php echo $this->_tpl_vars['doc']->id; ?>
">
								<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ti,'separator' => "/"), $this);?>

							</a>
						</font>
					</td>
				</tr>
				<tr valign="top">
					<td width="15%">
						<b>
							<?php echo $this->_tpl_vars['texts']['LABEL_AUTHOR']; ?>

						</b>
					</td>
					<td>
						<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->au,'separator' => ";"), $this);?>

					</td>
				</tr>
				<tr valign="top">
					<td>
						<b>
							<?php echo $this->_tpl_vars['texts']['LABEL_SOURCE']; ?>

						</b>
					</td>
					<td>
						<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->fo,'separator' => ";"), $this);?>

					</td>
				</tr>
				<?php if (isset ( $this->_tpl_vars['doc']->ab )): ?>
				<tr valign="top">
					<td>
						<b>
							<?php echo $this->_tpl_vars['texts']['LABEL_ABSTRACT']; ?>

						</b>
					</td>
					<td>
						<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->ab,'separator' => "<hr>"), $this);?>

					</td>
				</tr>
				<?php endif; ?>
				<tr valign="top">
					<td>
						<b>
							<?php echo $this->_tpl_vars['texts']['LABEL_SUBJECT']; ?>

						</b>
					</td>
					<td>
						<?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->mh,'separator' => ";"), $this);?>

					</td>
				</tr>
			</table>
	<?php endforeach; endif; unset($_from); ?>
	</div>
</div>