<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Smarty substring_after modifier plugin
 *
 * Type:     modifier<br>
 * Name:     strip<br>
 * Purpose:  Return substring after a text.
 * Example:  {$var|substring_after:"hello"} 
 * Date:     May 30, 2008
 * @author   Vinicius Andrade
 * @version  1.0
 * @param string
 * @param string
 * @return string
 */
function smarty_modifier_substring_after($text, $needle = '-')
{
    if (strpos($text, $needle) !== false){
        return substr($text, strpos($text, $needle)+strlen($needle));
    }else{
        return "";
    }
}

?>
