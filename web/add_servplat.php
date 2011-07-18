<?php
require_once('/home/aplicacoes-bvs/regional/htdocs/apps/servicesplat/client/config.php');

$userTK = isset($_REQUEST['userTK'])?$_REQUEST['userTK']:false;

if($userTK){
    /* necessita adicionar em arquivo de configuracao */
    $objSoapClient = new SoapClient(null,array('location'=>SERVICES_PLATFORM_SERVER.'/DocsCollection.php',
                                               'uri'=>'http://test-uri/'));
                                               
$url = htmlspecialchars($_REQUEST['url']);
$source = htmlspecialchars($_REQUEST['source']);
$author = htmlspecialchars($_REQUEST['author']);
$title = htmlspecialchars($_REQUEST['title']);

                                               
$xmlDoc=<<<XML
<?xml version='1.0'?>
<docs>
	<doc>
        <field name="doc_id">{$_REQUEST['id']}</field>
        <field name="doc_url">{$url}</field>
        <field name="src_id">{$source}</field>
        <field name="au">{$author}</field>
        <field name="title">{$title}</field>
    </doc>
</docs>
XML;

    $retValue = $objSoapClient->addDoc($userTK,$xmlDoc);
    die($retValue);    
}
?>
