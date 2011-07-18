<?php
	// funcao retirada da pagina http://www.php.net/utf8_encode 
	function isUTF8($string){
    	if (is_array($string)) {
        	$enc = implode('', $string);
        	return @!((ord($enc[0]) != 239) && (ord($enc[1]) != 187) && (ord($enc[2]) != 191));
    	}else{
        	return (utf8_encode(utf8_decode($string)) == $string);
    	}
	}

	function getWhereFilter($colectionData, $where){
		$whereFilter = "";
		if (isset($colectionData->where_list)){
			foreach($colectionData->where_list->where as $whereOpt  ){
				if ($whereOpt->name == $where){
					$whereFilter = $whereOpt->filter;
					break;
				}
			}
		}
		return html_entity_decode($whereFilter);
	}

	function getSortValue($colectionData, $sort){
		$whereFilter = "";
        if ( isset($colectionData->sort_list) ){
            foreach( $colectionData->sort_list->sort as $sortItem  ){
                if ($sortItem->name == $sort || $sortItem->value == $sort){
                    $sortValue = $sortItem->value;
                    break;
                }
            }
        }
		return urlencode($sortValue);
	}

    function getDefaultSort($colectionData, $q){
		$sortValue = "";
		$count = 0;
        if ( isset($colectionData->sort_list) ){
            foreach( $colectionData->sort_list->sort as $sortItem  ){
            	// seleciona primeito item do config como default
            	if ( $count == 0){
            		$sortValue = $sortItem->value;            	
            	}
            	// caso a query esteja vazia verifica se o item possue default_for_empty_query	
                if ( $q == '' && isset($sortItem->default_for_empty_query) ){
    				$sortValue = $sortItem->value;
        		}
        		$count++;
            }
        }
		return urlencode($sortValue);
	}
    // function to work when PHP directive magic_quotes_gpc is OFF
    function addslashes_array($a){
        if(is_array($a)){
            foreach($a as $n=>$v){
                $b[$n]=addslashes_array($v);
            }
            return $b;
        }else{
            if ($a != ''){
                return addslashes($a);
            }
        }
    }
	
	//=========================================================================================================

	$lang = "";
    $tag = "1.2";
	$rev = "-rev$Rev.186";
	// define constants
	define("VERSION", $tag . $rev);
	define("USE_SERVER_PATH", true);

	if (USE_SERVER_PATH == true){
		$PATH = dirname($_SERVER["PATH_TRANSLATED"]);
	}else{
		$PATH = dirname(__FILE__).'/';
	}		
	
	$PATH_DATA = substr($PATH,strlen($_SERVER["DOCUMENT_ROOT"]));
	$PATH_DATA = str_replace('\\','/',$PATH_DATA);

	$config = simplexml_load_file('config/dia-config.xml');

	//idioma da interface
	if(!isset($_REQUEST["lang"])) {
		$_REQUEST["lang"] = $config->default_lang;
	}	
	$lang = $_REQUEST["lang"];
	
	$defaultCollectionData = $config->search_collection_list->collection[0];

	// verifica se existe apenas uma colecao definida no config.xml
	if ( !is_array($defaultCollectionData) ){
		$defaultCollectionData = $config->search_collection_list->collection;	
	}	
	$defaultCollection = $defaultCollectionData->name;
	$defaultSite = $defaultCollectionData->site;

	if ($defaultSite == ""){
		$defaultSite = $config->site;
	}

	//security check
	if (!ereg("^[a-zA-Z\-]{2,5}",$lang))
		die("invalid parameter lang" . $lang);

	$texts = parse_ini_file("./languages/" . $lang . "/texts.ini", true);					// interface texts
	$logDir = ( isset( $config->log_dir ) ? $config->log_dir : "logs/");

	//environment variables
	$config["PATH_DATA"] = $PATH_DATA;
	$config["DOCUMENT_ROOT"] = $_SERVER["DOCUMENT_ROOT"];
	$config["SERVERNAME"] = $_SERVER["HTTP_HOST"];

	define("SERVERNAME", $config["SERVERNAME"]);
	define("PATH_DATA" , $config["PATH_DATA"]);
	define("DOCUMENT_ROOT", $config["DOCUMENT_ROOT"]);
	define("APP_PATH", $config["DOCUMENT_ROOT"] . $config["PATH_DATA"]);

	define('LOG_DIR', $logDir);
	define('LOG_FILE',"log" . date('Ymd') . "_search.txt");

	// verifica se exitem acentos codificados em ISO nos parâmetros de entrada (q, filter e filterLabel)
	if (!isUTF8($_REQUEST["q"])){
		$_REQUEST["q"] = utf8_encode($_REQUEST["q"]);
	}
	if (!isUTF8($_REQUEST["filter"])){
		$_REQUEST["filter"] = utf8_encode($_REQUEST["filter"]);
	}
	if (!isUTF8($_REQUEST["filterLabel"])){
		$_REQUEST["filterLabel"] = utf8_encode($_REQUEST["filterLabel"]);
	}

	// seta variavel colectionData com a configuracao da colecao atual
	if ($_REQUEST['col'] != ''){
		for ($c = 0; $c < count($config->search_collection_list->collection); $c++){
			$colName = $config->search_collection_list->collection[$c]->name;
			$colSite = $config->search_collection_list->collection[$c]->site;
			if (!isset($colSite) || $colSite == ''){
				$colSite = $defaultSite;
			}
			if ($_REQUEST['col'] == $colName ){
				if ( isset($_REQUEST['site']) ) {
					if ($_REQUEST['site'] == $colSite ){
						$colectionData = $config->search_collection_list->collection[$c];
						break;
					}
				}else if ($colSite == $defaultSite){
					$colectionData = $config->search_collection_list->collection[$c];
					break;
				}
			}
		}
	}
	if (!isset($colectionData)){
		$colectionData = $defaultCollectionData;
	}
?>
