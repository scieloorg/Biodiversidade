<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Smarty substring_before modifier plugin
 *
 * Type:     modifier<br>
 * Name:     strip<br>
 * Purpose:  Return substring after a text.
 * Example:  {$var|substring_before:"hello"} 
 * Date:     May 30, 2008
 * @author   Vinicius Andrade
 * @version  1.0
 * @param string
 * @param string
 * @return string
 */
function smarty_modifier_substring_before($text, $needle = '-')
{
    if (strpos($text, $needle) !== false){
        return substr($text, 0,strpos($text, $needle));
    }else{
        return "";
    }
}

?>
