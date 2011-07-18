<?php
/**
 * Smarty shared plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Function: smarty_contains
 * Purpose:  Used to find a string in a string
 * Example: contains( 'Jason was here', 'here' ) returns true
 * Example2: contains( 'Jason was here', 'ason' ) returns false
 * @param string
 * @return string
 */
function smarty_modifier_contains($string, $find)
{
	$result = false;

	if (is_array($string)){

		foreach($string as $str) {
			$pos = strpos($str, $find);
			if ($pos !== false){
				$result = true;
				break;
			}
		}

	}else{

		$pos = strpos($string, $find);
		if ($pos !== false) {
			$result = true;
		}

	}
	return $result;
}

/* vim: set expandtab: */

?>