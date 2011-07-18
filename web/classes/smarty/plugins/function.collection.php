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
 * @param array
 * @param Smarty
 * @return string
 */
function smarty_function_collection($params, &$smarty)
{
	$output = "";
    if (!isset($params['element'])) {
        return;
    }

	$element = $params['element'];

	$acron = array('scl' => 'SciELO Brasil','arg' => 'SciELO Argentina','chl' => 'SciELO Chile','cub' => 'SciELO Cuba','esp' => 'SciELO Espanha','mex' => 'SciELO México','prt' => 'SciELO Portugal','ven' => 'SciELO Venezuela','spa' => 'SciELO Saúde Pública','sss' => 'SciELO Social Sciences');
	
	if ($element){
		foreach($acron as $key => $elem){
			
			if($key == $element){
				$output = $elem;
			}
		}

	}	
      return $output;
}
?>
