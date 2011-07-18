<?php /* Smarty version 2.6.19, created on 2010-11-10 12:23:06
         compiled from result-navigation.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'number_format', 'result-navigation.tpl', 4, false),array('function', 'math', 'result-navigation.tpl', 12, false),)), $this); ?>
<div class="infoBar">
	<div class="totalResults">
		<?php echo $this->_tpl_vars['texts']['RESULTS']; ?>
&#160;
		<strong><?php echo $this->_tpl_vars['pagination']['from']; ?>
-<?php echo $this->_tpl_vars['pagination']['to']; ?>
</strong> de <strong><?php echo ((is_array($_tmp=$this->_tpl_vars['pagination']['total'])) ? $this->_run_mod_handler('number_format', true, $_tmp, 0, ",", ".") : number_format($_tmp, 0, ",", ".")); ?>
</strong>
	</div>

	<?php if ($this->_tpl_vars['pagination']['last'] > 1): ?>
		<div class="pagination">
	
			<?php if ($this->_tpl_vars['pagination']['page'] > 1): ?>

				<?php echo smarty_function_math(array('assign' => 'previous','equation' => "(((current - 1) * count) - count) + 1",'current' => $this->_tpl_vars['pagination']['page'],'count' => $this->_tpl_vars['pagination']['count']), $this);?>


				<span>&lt;&lt; <a href="javascript:changeFormParameter('from','1')"><?php echo $this->_tpl_vars['texts']['FIRST_PAGE']; ?>
</a></span>
				<span>&lt; <a href="javascript:changeFormParameter('from','<?php echo $this->_tpl_vars['previous']; ?>
')"><?php echo $this->_tpl_vars['texts']['PREVIOUS_PAGE']; ?>
</a></span>
			<?php else: ?>
				<span>&lt;&lt; <?php echo $this->_tpl_vars['texts']['FIRST_PAGE']; ?>
</span>
				<span>&lt; <?php echo $this->_tpl_vars['texts']['PREVIOUS_PAGE']; ?>
</span>
			<?php endif; ?>
			
			<?php $_from = $this->_tpl_vars['pagination']['pages']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['iPage']):
?>
			
				<?php echo smarty_function_math(array('assign' => 'nextFrom','equation' => "((current - 1) * count) + 1",'current' => $this->_tpl_vars['iPage'],'count' => $this->_tpl_vars['pagination']['count']), $this);?>

			
				<?php if ($this->_tpl_vars['iPage'] == $this->_tpl_vars['pagination']['page']): ?>	
					<span><?php echo $this->_tpl_vars['iPage']; ?>
</span>	
				<?php else: ?>
					<span><a href="javascript:changeFormParameter('from','<?php echo $this->_tpl_vars['nextFrom']; ?>
')" ><?php echo $this->_tpl_vars['iPage']; ?>
</a></span>	
				<?php endif; ?>
				
			<?php endforeach; endif; unset($_from); ?>
	
			<?php if ($this->_tpl_vars['pagination']['page'] == $this->_tpl_vars['pagination']['last']): ?>	
				<span><?php echo $this->_tpl_vars['texts']['NEXT_PAGE']; ?>
 &gt;</span>
			<?php else: ?>
				<?php echo smarty_function_math(array('assign' => 'nextFrom','equation' => "( ((current - 1) * count) + count) + 1",'current' => $this->_tpl_vars['pagination']['page'],'count' => $this->_tpl_vars['pagination']['count']), $this);?>

	
				<span><a href="javascript:changeFormParameter('from','<?php echo $this->_tpl_vars['nextFrom']; ?>
')"><?php echo $this->_tpl_vars['texts']['NEXT_PAGE']; ?>
</a> &gt;</span>
			<?php endif; ?>
	
		</div>
	<?php endif; ?>
</div>