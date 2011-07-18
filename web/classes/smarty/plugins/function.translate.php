<?php
/**
 * Smarty plugin
 * @package Smarty
 * @subpackage plugins
 */

/**
 * Smarty {translate} function plugin
 *
 * Type:     function<br>
 * Name:     translate<br>
 * Date:     Feb 17, 2003<br>
 * Purpose:  return a <br>
 * Input:<br>
 *         - text
 *         - suffix
 *         - translation
 *
 * Examples:
 * <pre>
 * {translate text=MEDLINE suffix=DB_ translation=$texts}
 * </pre>
 * @author   Vinicius Andrade <viniciusdeandrade at gmail dot com>
 * @version  0.1
 * @param array
 * @param Smarty
 * @return string
 */
function smarty_function_translate($params, &$smarty)
{
	$output = "";
	$find = "";
    if (!isset($params['text'])) {
        return;
    }
    $text_to_find = (string) $params['text'];

    $text_to_find = preg_replace ('/ +/', ' ', $text_to_find);
    $text_to_find = preg_replace('/[ ,\-]/','_', $text_to_find);
    $text_to_find = preg_replace('/_+/','_', $text_to_find);

   // print '[[' . $text_to_find . ']]';

	if ( isset($params['suffix']) ){
		$find .= $params['suffix'];
	}
	$find .= $text_to_find;


	$output = $params['translation'][$find];

	return $output;

}
?>
