<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */


/**
 * Smarty {occ} function plugin
 *
 * Type:     function<br>
 * Name:     occ<br>
 * Date:     Feb 17, 2003<br>
 * Purpose:  return a <br>
 * Input:<br>
 *         - label
 *         - element 
 *         - separator 
 *         - class
 *
 * Examples:
 * <pre>
 * {occ label=AUTOR element=$doc->au separator=; class=author}
 * </pre>
 * @version  0.1
 * @param array
 * @param Smarty
 * @return string
 */
function smarty_function_date_format($params, &$smarty)
{
	$output = "";
    if (!isset($params['element'])) {
        return;
    }

	$element = $params['element'];

	$acron = array('01' => 'Jan.','02' => 'Feb.','03' => 'Mar.','04' => 'Apr.','05' => 'May.','06' => 'Jun.','07' => 'Jul.','08' => 'Aug.','09' => 'Sep.','10' => 'Oct.','11' => 'Nov.','12' => 'Dec.');
	
	if ($element){

		$sub_year = substr($element,0,4);

		$output = $sub_year;

		$sub_month = substr($element,4,2);

		foreach($acron as $key => $elem){
			
			if($key == $sub_month){
				$output .= " ". $elem;
			}
		}

	}	

      return $output;
}


?>
