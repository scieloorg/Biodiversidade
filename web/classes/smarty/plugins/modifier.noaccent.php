<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Smarty {noaccent} modifier plugin
 *
 * Type:     modifier<br>
 * Name:     noaccent<br>
 * Date:     Feb 17, 2003<br>
 * Purpose:  return a no accent string<br>
 * Input:<br>
 *         - text
 *
 * Examples:
 * <pre>
 *  coração:noaccent   ---->  coracao
 * </pre>
 * @author   Vinicius Andrade <viniciusdeandrade at gmail dot com>
 * @version  0.1
 * @param array
 * @param Smarty
 * @return string
 */
function smarty_modifier_noaccent($string)
{

    $search = explode(",","ç,æ,œ,á,é,í,ó,ú,à,è,ì,ò,ù,ä,ë,ï,ö,ü,ÿ,â,ê,î,ô,û,å,e,i,ø,u,Á,É,Í,Ó,Ú,À,È,Ã");
    $replace = explode(",","c,ae,oe,a,e,i,o,u,a,e,i,o,u,a,e,i,o,u,y,a,e,i,o,u,a,e,i,o,u,A,E,I,O,U,A,E,A");

    $output = str_replace($search, $replace, $string);


	return $output;

}
?>