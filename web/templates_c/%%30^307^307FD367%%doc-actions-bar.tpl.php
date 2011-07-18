<?php /* Smarty version 2.6.19, created on 2010-11-25 14:25:02
         compiled from doc-actions-bar.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'iahlinks', 'doc-actions-bar.tpl', 11, false),array('function', 'occ', 'doc-actions-bar.tpl', 45, false),array('modifier', 'count', 'doc-actions-bar.tpl', 22, false),array('modifier', 'contains', 'doc-actions-bar.tpl', 75, false),)), $this); ?>

<?php if ($this->_tpl_vars['doc']->db == 'DECS'): ?>
    <div class="text_abstract">
        <a href="#" onclick="javascript:refineByIndex('<?php echo $this->_tpl_vars['doc']->ti_pt[0]; ?>
','mh')"><img src="./image/common/viewFullText.gif"/></a>
        <a href="#" onclick="javascript:refineByIndex('<?php echo $this->_tpl_vars['doc']->ti_pt[0]; ?>
','mh')"><?php echo $this->_tpl_vars['texts']['SEARCH_USING_TERMINOLOGY']; ?>
</a>
    </div>

<?php else: ?>

    <?php ob_start(); ?>
         <?php echo smarty_function_iahlinks(array('scielo' => $this->_tpl_vars['links']->response->docs,'document' => $this->_tpl_vars['doc']->ur,'id' => $this->_tpl_vars['doc']->id,'lang' => $this->_tpl_vars['lang'],'la_text' => $this->_tpl_vars['doc']->la,'la_abstract' => $this->_tpl_vars['doc']->la_ab), $this);?>

    <?php $this->_smarty_vars['capture']['fulltextlinks'] = ob_get_contents(); ob_end_clean(); ?>

    <div style="display: none;" class="linkBox boxContent" id="linkBox_<?php echo $this->_tpl_vars['doc']->id; ?>
">
        <div class="showBox">
            <?php echo $this->_smarty_vars['capture']['fulltextlinks']; ?>

        </div>
        <span class="arrowBox"></span>
    </div>

        <?php if (count($this->_tpl_vars['scieloLinkList']) > 0): ?>
        <div class="text_abstract">
            <?php if (count($this->_tpl_vars['scieloLinkList']) > 1): ?>
                <a href="#" onclick="showhideLayers('linkBox_<?php echo $this->_tpl_vars['doc']->id; ?>
'); return false;">
                    <img src="./image/common/icon_scielo.gif"/>
                </a>
            <?php else: ?>
                <a href="<?php echo $this->_tpl_vars['scieloLinkList'][0]; ?>
" target="_blank">
                    <img src="./image/common/icon_scielo.gif"/>
		Scielo Link
                </a>
            <?php endif; ?>
        </div>
    <?php endif; ?>

        <?php if (count($this->_tpl_vars['scieloLinkList']) == 0 && ( count($this->_tpl_vars['doc']->ab) > 0 || count($this->_tpl_vars['fulltextLinkList']) > 0 )): ?>
        <div class="text_abstract">
            <a name="abs"><img src="./image/common/viewFullText.gif"/></a>
            <?php if (count($this->_tpl_vars['doc']->ab) > 0): ?>
                <span>
                    <a href="resources/<?php echo $this->_tpl_vars['doc']->id; ?>
"><?php echo $this->_tpl_vars['texts']['ABSTRACT_IN']; ?>

                    <?php if ($this->_tpl_vars['doc']->la_ab != ''): ?>
                        <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->la_ab,'translation' => $this->_tpl_vars['texts'],'suffix' => 'LANG_','separator' => "|",'text_transform' => 'lowercase'), $this);?>
</a>
                    <?php else: ?>
                        <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->la,'translation' => $this->_tpl_vars['texts'],'suffix' => 'LANG_','separator' => "|",'text_transform' => 'lowercase'), $this);?>
</a>
                    <?php endif; ?>
                </span>
            <?php endif; ?>
            <?php if (count($this->_tpl_vars['fulltextLinkList']) > 1): ?>
                <span>
                    <a href="#" onclick="showhideLayers('linkBox_<?php echo $this->_tpl_vars['doc']->id; ?>
'); return false;">
                        &#160;<?php echo $this->_tpl_vars['texts']['FULLTEXT_IN']; ?>

                        <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->la,'translation' => $this->_tpl_vars['texts'],'suffix' => 'LANG_','separator' => "|",'text_transform' => 'lowercase'), $this);?>

                    </a>
                </span>
            <?php elseif (count($this->_tpl_vars['fulltextLinkList']) > 0): ?>
                <span>
                    <a href="<?php echo $this->_tpl_vars['fulltextLinkList'][0]; ?>
" target="_blank">
                    &#160;<?php echo $this->_tpl_vars['texts']['FULLTEXT_IN']; ?>

                        <?php echo smarty_function_occ(array('element' => $this->_tpl_vars['doc']->la,'translation' => $this->_tpl_vars['texts'],'suffix' => 'LANG_','separator' => "|",'text_transform' => 'lowercase'), $this);?>

                    </a>
                </span>
            <?php endif; ?>
        </div>
    <?php endif; ?>

    <div class="print">
        <a href="index.php?q=%2Bid:(%22<?php echo $this->_tpl_vars['doc']->id; ?>
%22)&amp;lang=<?php echo $this->_tpl_vars['lang']; ?>
&amp;printMode=true">
            <img src="./image/common/icon_print.gif"/>
            &#160;<span><?php echo $this->_tpl_vars['texts']['PRINT']; ?>
</span>
        </a>
    </div>
    <?php if (((is_array($_tmp=$this->_tpl_vars['doc']->db)) ? $this->_run_mod_handler('contains', true, $_tmp, 'MEDLINE') : smarty_modifier_contains($_tmp, 'MEDLINE')) || smarty_modifier_contains($this->_tpl_vars['doc']->services, 'SCAD')): ?>
        <div class="scad">
            <a href="<?php echo $this->_tpl_vars['config']->photocopy_url; ?>
&lang=<?php echo $this->_tpl_vars['lang']; ?>
&db=<?php echo $this->_tpl_vars['doc']->db; ?>
&ident=<?php echo $this->_tpl_vars['refID']; ?>
">
                <img src="./image/common/icon_scad.gif"/>
                &#160;<span><?php echo $this->_tpl_vars['texts']['PHOTOCOPY']; ?>
</span>
            </a>
        </div>
    <?php endif; ?>

    <?php if (isset ( $_COOKIE['userTK'] )): ?>
        <div class="scielo">
                <a href="#">
                    <img src="./image/common/icon_addToFolder.gif"/>
                    &#160;<span><?php echo $this->_tpl_vars['texts']['ADD_TO_COLLECTION']; ?>
</span>
                </a>
        </div>
    <?php endif; ?>

<?php endif; ?>