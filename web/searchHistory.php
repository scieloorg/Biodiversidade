<?php
require("classes/Bookmark.php");
$lang = 'pt';
$translation = parse_ini_file("languages/$lang/texts.ini");

$action = $_POST['action'];
$term = stripslashes($_POST['term']);

session_start();
if( !isset($_SESSION["searchHistory"])){
	$sh = new ArrayList();
	$_SESSION["searchHistory"] = serialize($sh);
}

$history = unserialize($_SESSION["searchHistory"]);
//$bookmark = new Bookmark();

switch($action){
	case '*': print_r($history->list);
			  break;
	case 'a': $history->addElement($term);
			  break;
	case 'c': $history->removeAll();
			  break;
	case 'r': $history->removeElement($term);
			  print("$term removed");
			  break;
	case 'l': if(sizeOf($history->list) == 0){
				//print("<li><a>".$translation['EMPTY'].".</a></li>");
				break;
			  }
			  foreach($history->list as $term){
				printSearchItem($term);
			  }
			  break;
	case 's': print(sizeOf($history->list));
			  break;
}
$_SESSION["searchHistory"] = serialize($history);

/**
 * Imprime item de lista para o box
 * de id "searchHistory"
 * 
 * chooseOperatorToSearch('$term',e);
 */
function printSearchItem($term){
	$term_escaped = urlencode($term);
	$term_escaped = str_replace("+","%20",$term_escaped);
	$term = utf8_encode($term);
	$offset = 20;
print"
	<li>
";
	if(strlen($term) > $offset){
		print("		<a onclick=\"searchFromHistory('$term')\" onmouseover=\"showInfo('$term_escaped',this.parentNode.parentNode,event)\">". substr($term,0,$offset)." ...</a>");		
	}else{
		print("		<a onclick=\"searchFromHistory('$term')\">$term</a>");
	}
print"

		<a class=\"remExpr\" onclick=\"removeSearchTerm('$term_escaped',this.parentNode)\">
			<img title=\"remover expressão do histórico\" alt=\"remover expressão do histórico\" src=\"./image/common/delete.gif\"/>
		</a>
		<a class=\"addExpr\">
			<img title=\"adicionar expressão a esta pesquisa\" alt=\"adicionar expressão a esta pesquisa\" src=\"./image/common/icon_searchHistory.gif\" onclick=\"chooseOperatorToSearch('$term_escaped',event);\"/>
		</a>
	</li>";
}

?>