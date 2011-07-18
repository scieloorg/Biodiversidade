<?php

/**
 * Smarty {json} plugin
 *
 * Type:     function
 * Name:     json
 * Purpose:  fetch json file and  assign result as a template variable (array) 
 * @param url (url to fetch)
 * @param assign (element to assign to)
 * @return array|null if the assign parameter is passed, Smarty assigns the
 *                     result to a template variable
 */
function smarty_function_json($params, &$smarty)
{	
    if (empty($params['url'])) {
        $smarty->_trigger_fatal_error("[json] parameter 'url' cannot be empty");
        return;
    }  
    
    $content = array();
    $data = file_get_contents($params['url']);
    if(empty($data)) return false;
        
    if(!is_callable('json_decode')) {
    	require_once 'JSON.php'; 
	 	$json = new Services_JSON();	
	 	$content = $json->decode( trim(file_get_contents($params['url'])) ); 
    } else {
    	$content = json_decode(trim(file_get_contents($params['url'])));
    }
    
    if($params['debug']===true) {
    	echo "<pre>"; 
    	print_r($content);
    	echo "</pre>";
    }

    if (!empty($params['assign'])) {
        $smarty->assign($params['assign'],$content);
    } else {
        return $content;
    }
}
?>
