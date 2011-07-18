<?php
// Turn off all error reporting
error_reporting(0);

$lang = 'pt';
if(isset($_REQUEST['lang'])){
	if(preg_match("/en|pt|es/",$_REQUEST['lang'])){
		$lang = $_REQUEST['lang'];
	}
}else if(isset($_COOKIE['clientLanguage'])){
	if(preg_match("/en|pt|es/",$_COOKIE['clientLanguage'])){
		$lang = $_COOKIE['clientLanguage'];
	}
}

$trans = parse_ini_file("languages/$lang/texts.ini");

if ($lang == 'pt'){
	$langOneLetter = "p";
}else if ($lang == 'es'){
	$langOneLetter = "e";
}else{
	$langOneLetter = "i";
}


$bool = array( "101", // Termo autorizado
			  	"102", // Sinônimo
			  	"104"  // Termo histórico
			);

/*
 * Extrai conceito de um descritor
 */
$term = $_REQUEST['term'];
$term = stripcslashes($term);
$term = strtoupper($term);
$term = urlencode($term);

$concept = 0;
for( $i = 0; !$concept && ($i < sizeof($bool)); $i = $i + 1 ){
	$query = "http://decs.bvsalud.org/cgi-bin/mx/cgi=@vmx/decs/?bool=".$bool[$i]."%20$term&lang=$lang";
	$decs = @simplexml_load_file($query);
	if ($decs){
		$concept = (String) $decs->decsws_response->record_list->record->definition->occ['n'];
	}
}
$i = $i-1;

/*
 * Link para a página do DeCS
 */

$href = "http://decs.bvsalud.org/cgi-bin/wxis1660.exe/decsserver/".
"?IsisScript=../cgi-bin/decsserver/decsserver.xis".
"&search_language=".$langOneLetter.
"&interface_language=".$langOneLetter.
"&previous_page=homepage&task=exact_term&search_exp=".$term;

header("Content-Type: text/plain Charset=UTF-8");
if(isset($_GET['debug'])){
	print($query."\n");
	print_r($decs);
}else{
	if(!$concept){
		print "<em>".$trans['DescNF']."</em>";
	}else{
		print $concept;
	}
}

?>
<!-- <?=$bool[$i]?> -->
<div id="logo-decs">
	<?=$trans['source']?>: <a href="<?=$href?>" target="_blank">DeCS - <?=$trans['DeCS']?> <img src="./image/common/logodecs.gif" alt="DeCS"></img></a>
</div>