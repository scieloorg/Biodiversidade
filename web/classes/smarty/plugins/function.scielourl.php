<?php
/*
 * Smarty plugin
 * -------------------------------------------------------------
 * File:     function.iahlinks.php
 * Type:     function
 * Name:     iahlinks
 * Purpose:  outputs fulltext links
 * -------------------------------------------------------------
 */
function smarty_function_scielourl($params, &$smarty)
{

	$output = "";

	$scieloUrl['scl'] = "http://www.scielo.br/";
	$scieloUrl['chl'] = "http://www.scielo.cl/";
	$scieloUrl['spa'] = "http://www.scielosp.org/";
	$scieloUrl['arg'] = "http://www.scielo.org.ar/";
	$scieloUrl['cub'] = "http://scielo.sld.cu/";
	$scieloUrl['esp'] = "http://scielo.isciii.es/";
	$scieloUrl['col'] = "http://www.scielo.org.co/";
	$scieloUrl['mex'] = "http://www.scielo.org.mx/";
	$scieloUrl['ven'] = "http://www.scielo.org.ve/";
	$scieloUrl['prt'] = "http://www.scielo.oces.mctes.pt/";
	$scieloUrl['sss'] = "http://socialsciences.scielo.org/";

	$site = $params['site'];		//scielo collection
    $pid  = $params['pid'];         //scielo PID
    if ( eregi("\^c",$pid) ){
       $pid = substr($pid, 0, strpos($pid,"^c") );
    }
    if ( eregi("art-",$pid) ){
       $pid = substr($pid, strpos($pid,"art-")+4 );
    }

	$lang = $params['lang'];

    $output = $scieloUrl[$site] . "scielo.php?script=sci_arttext&pid=" . $pid . "&lang=" . $lang;

    return $output;
}
?>
