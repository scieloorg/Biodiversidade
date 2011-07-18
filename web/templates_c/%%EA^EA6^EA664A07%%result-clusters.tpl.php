<?php /* Smarty version 2.6.19, created on 2010-11-19 15:49:03
         compiled from result-clusters.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'substring_before', 'result-clusters.tpl', 1, false),array('modifier', 'count', 'result-clusters.tpl', 9, false),array('function', 'translate', 'result-clusters.tpl', 29, false),)), $this); ?>
<?php $this->assign('facetBrowse', ((is_array($_tmp=$_POST['fb'])) ? $this->_run_mod_handler('substring_before', true, $_tmp, ":") : smarty_modifier_substring_before($_tmp, ":"))); ?>

<div class="bContent" id="refine_facet">
<?php $_from = $this->_tpl_vars['result']->facet_counts; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['cluster']):
?>

  <?php $_from = $this->_tpl_vars['cluster']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['key'] => $this->_tpl_vars['item']):
?>

	<?php $this->assign('label', "REFINE_".($this->_tpl_vars['key'])); ?>
	<?php $this->assign('totalItems', count($this->_tpl_vars['item'])); ?>

	<?php if ($this->_tpl_vars['totalItems'] > 0): ?>
                <?php if ($this->_tpl_vars['facetBrowse'] == $this->_tpl_vars['key']): ?>
        	<div id="<?php echo $this->_tpl_vars['key']; ?>
">
        <?php else: ?>
            <div id="<?php echo $this->_tpl_vars['key']; ?>
" class="closed">
        <?php endif; ?>
		<?php if ($this->_tpl_vars['key'] == 'fulltext'): ?>
			<strong onclick="showHideBox('<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_tpl_vars['texts'][$this->_tpl_vars['label']]; ?>
</strong>
			(<a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['item'][0][0]; ?>
','fulltext')"><?php echo $this->_tpl_vars['item'][0][1]; ?>
</a>)

		<?php else: ?>
			<strong onclick="showHideBox('<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_tpl_vars['texts'][$this->_tpl_vars['label']]; ?>
</strong>
			<a href="#" onclick="showChart(this,'<?php echo $this->_tpl_vars['texts'][$this->_tpl_vars['label']]; ?>
','<?php echo $this->_tpl_vars['key']; ?>
')" class="thickbox"><img src="image/common/chart.gif"></a>
			<ul id="<?php echo $this->_tpl_vars['key']; ?>
_set">
			<?php if ($this->_tpl_vars['key'] == 'type'): ?>
				<?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>

					<?php ob_start(); ?><?php echo smarty_function_translate(array('text' => $this->_tpl_vars['clusterItem'][0],'suffix' => 'TYPE_','translation' => $this->_tpl_vars['texts']), $this);?>
<?php $this->_smarty_vars['capture']['type'] = ob_get_contents(); ob_end_clean(); ?>
					<?php if ($this->_smarty_vars['capture']['type'] != ''): ?>
						<li>
							<a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_smarty_vars['capture']['type']; ?>
</a> (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
						</li>
					<?php endif; ?>
				<?php endforeach; endif; unset($_from); ?>

			<?php elseif ($this->_tpl_vars['key'] == 'mh_cluster'): ?>

				<?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>
					<li>
						<a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','mj')"><?php echo $this->_tpl_vars['clusterItem'][0]; ?>
</a> (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
					</li>
				<?php endforeach; endif; unset($_from); ?>

			<?php elseif ($this->_tpl_vars['key'] == 'limit'): ?>

                <?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>
                    <?php ob_start(); ?><?php echo smarty_function_translate(array('text' => $this->_tpl_vars['clusterItem'][0],'suffix' => 'LIMIT_','translation' => $this->_tpl_vars['texts']), $this);?>
<?php $this->_smarty_vars['capture']['limit'] = ob_get_contents(); ob_end_clean(); ?>
                    <?php if ($this->_smarty_vars['capture']['limit'] != ''): ?>
                        <li>
                            <a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_smarty_vars['capture']['limit']; ?>
</a> (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
                        </li>
                    <?php endif; ?>
                <?php endforeach; endif; unset($_from); ?>

			<?php elseif ($this->_tpl_vars['key'] == 'type_of_study'): ?>

				<?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>
                    <?php ob_start(); ?><?php echo smarty_function_translate(array('text' => $this->_tpl_vars['clusterItem'][0],'suffix' => 'STUDY_','translation' => $this->_tpl_vars['texts']), $this);?>
<?php $this->_smarty_vars['capture']['study'] = ob_get_contents(); ob_end_clean(); ?>

                    <?php if ($this->_smarty_vars['capture']['study'] != ''): ?>
    					<li>
	    					<a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','type_of_study')"><?php echo $this->_smarty_vars['capture']['study']; ?>
</a>    (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
					    </li>
                    <?php endif; ?>
				<?php endforeach; endif; unset($_from); ?>

			<?php elseif ($this->_tpl_vars['key'] == 'la'): ?>

				<?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>

					<?php ob_start(); ?><?php echo smarty_function_translate(array('text' => $this->_tpl_vars['clusterItem'][0],'suffix' => 'LANG_','translation' => $this->_tpl_vars['texts']), $this);?>
<?php $this->_smarty_vars['capture']['lang'] = ob_get_contents(); ob_end_clean(); ?>
					<?php if ($this->_smarty_vars['capture']['lang'] != ''): ?>
						<li>
							<a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_smarty_vars['capture']['lang']; ?>
</a> (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
						</li>
					<?php endif; ?>
				<?php endforeach; endif; unset($_from); ?>

            <?php elseif ($this->_tpl_vars['key'] == 'clinical_aspect'): ?>

                <?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>

                    <?php ob_start(); ?><?php echo smarty_function_translate(array('text' => $this->_tpl_vars['clusterItem'][0],'suffix' => 'ASPECT_','translation' => $this->_tpl_vars['texts']), $this);?>
<?php $this->_smarty_vars['capture']['lang'] = ob_get_contents(); ob_end_clean(); ?>
                    <?php if ($this->_smarty_vars['capture']['lang'] != ''): ?>
                        <li>
                            <a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_smarty_vars['capture']['lang']; ?>
</a> (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
                        </li>
                    <?php endif; ?>
                <?php endforeach; endif; unset($_from); ?>

			<?php else: ?>
				<?php $_from = $this->_tpl_vars['item']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['clusterKey'] => $this->_tpl_vars['clusterItem']):
?>
					<li>
						<a href="#" onclick="javascript:applyFilter('<?php echo $this->_tpl_vars['clusterItem'][0]; ?>
','<?php echo $this->_tpl_vars['key']; ?>
')"><?php echo $this->_tpl_vars['clusterItem'][0]; ?>
</a> (<?php echo $this->_tpl_vars['clusterItem'][1]; ?>
)
					</li>
				<?php endforeach; endif; unset($_from); ?>
			<?php endif; ?>
		<?php endif; ?>

		<?php if ($this->_tpl_vars['totalItems'] > 0 && $this->_tpl_vars['totalItems']%$this->_tpl_vars['colectionData']->cluster_items_limit == 0): ?>
			<li><a href="#" onclick="javascript:showMoreClusterItems('<?php echo $this->_tpl_vars['key']; ?>
','<?php echo $this->_tpl_vars['totalItems']+$this->_tpl_vars['colectionData']->cluster_items_limit; ?>
'); return false"><b><?php echo $this->_tpl_vars['texts']['SHOW_MORE_ITEMS']; ?>
...</b></a></li>
		<?php endif; ?>
		</ul>
	</div>

	<?php endif; ?>
  <?php endforeach; endif; unset($_from); ?>
<?php endforeach; endif; unset($_from); ?>
</div>