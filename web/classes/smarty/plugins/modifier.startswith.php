<?php

/**
 * Function: smarty_startswith
 * Purpose:  Used to verifify if a string starts with other string
 * Example: startswith( 'Jason was here', 'Jason' ) returns true
 * Example2: startswith( 'Jason was here', 'ason' ) returns false
 * @param string
 * @return string
 */
function smarty_modifier_startswith($string, $find)
{
	$result = false;

    if (strpos($string, $find) === 0){
        $result = true;
    }

	return $result;
}

/* vim: set expandtab: */

?>