<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Smarty date_rss modifier plugin
 *
 * Type:     modifier
 * Name:     date_rss
 * Purpose:  convert string to DATE_RSS format
 * @param string
 * @return string
 */
function smarty_modifier_date_rss($string)
{
    if ( strpos($string,"-") === false ){
        $date_string = substr($string,0,4) . "-" . substr($string,4,2) . "-" . substr($string,6,2);
    }else{
        $date_string = $string;
    }        
          
    return date(DATE_RSS, strtotime($date_string));
}

?>
