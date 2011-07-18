<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
//ini_set('display_errors','On');
    require("CallAndRegister.php");

//var_dump($_REQUEST);
    $call = $_REQUEST['pdf'];

    $server_script = $_REQUEST['log_script'];
    $app =  $_REQUEST['app'];
    $page = $_REQUEST['page'];
    $pid =  $_REQUEST['pid'];
    $lang = $_REQUEST['lang'];
    $tlng = $_REQUEST['tlng'];
    
    $x = new SciELO_CallAndRegister();

    
    $x->execute_callandregister($server_script,  $app, $page, $pid, $lang, $tlng, $call);
?>
