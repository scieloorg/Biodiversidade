<?PHP
	require_once("config.php");	
	require_once("./classes/Dia.php");
	require_once("./classes/Page.php");
	require_once("./classes/Log.php");
	require_once('./classes/smarty/Smarty.class.php');

	$col = $_REQUEST["col"];
	$site = $_REQUEST["site"];
	$printMode = $_REQUEST["printMode"];

	if ( !isset($col) ){
		$col = $defaultCollection; 				// valor default criada no script de configuracao do sistema
	}
	if ( !isset($site) ){	
		$site= $defaultSite;					// valor default criada no script de configuracao do sistema
	}

	$from= ( isset($_REQUEST["from"]) && $_REQUEST["from"] != ''? $_REQUEST["from"] : 0 );
	
	$q  = stripslashes($_REQUEST["q"]);			//query
	
	if ($q == $texts['ENTER_WORDS']){
		$q = "";
	}	
	
	$qt = $_REQUEST["qt"];						//query type
	$index= $_REQUEST["index"];

	if (isset($_REQUEST['sort']) && $_REQUEST['sort'] != ""){
		$sort = getSortValue($colectionData,$_REQUEST["sort"]);		//get sort field to apply
	}else{
		$sort = getDefaultSort($colectionData, $q);		//get default sort
	}
	$output = ( isset($_REQUEST["output"]) && $_REQUEST["output"] != '' ? $_REQUEST["output"] : "json" );
    $callback = $_REQUEST['callback'];          // append callback function to json output

    $media =  $_REQUEST["media"];               // media template: screen (default) or mobile
		
	$filter = $_REQUEST["filter"];         		//initial filter to apply
	$filterLabel = $_REQUEST["filterLabel"];	//initial filter label
	
	$filter_chain = $_REQUEST["filter_chain"];	//user filter sequence (history)
	$addFilter = $_REQUEST["addfilter"];   		//new filter to apply
	$backFilter= $_REQUEST["backfilter"];  		//back to filter position

	$where = $_REQUEST["where"];							//select where search
	$whereFilter = getWhereFilter($colectionData,$where);	//select where search
	$count = ( isset($_REQUEST["count"]) ? $_REQUEST["count"] : $config->documents_per_page );
    
    $fmt = $_REQUEST["fmt"];                                //display format

    // create a array for CSA (custom search appearance) parameters
    $csa['bvs_logo'] = $_REQUEST["bvs_logo"];
    $csa['bvs_link'] = $_REQUEST["bvs_link"];
    $csa['banner_image'] = $_REQUEST["banner_image"];
    $csa['banner_text'] = $_REQUEST["banner_text"];
    $csa['home_text'] = $_REQUEST["home_text"]; 
    $csa['home_url'] = $_REQUEST["home_url"];
    $csa['css'] = $_REQUEST["css"];
    $csa['display_banner'] = $_REQUEST["display_banner"];

	//cluster parameters
	$fl = $colectionData->cluster_items_limit;
	$fb = $_REQUEST["fb"];									// facet browse

	if ( $addFilter != "" ){
		$filter_chain[] = $addFilter;
	}
	if (isset($backFilter) && $backFilter != ""){
		if ($backFilter == -1)	{  		//delete filter history
			$filter_chain = null;
		}else{
			if ($backFilter == -2)	{  	//delete filter history and query
				$filter_chain = null;
				$q = null;
			}else{
				$reduceFilter = array_slice($filter_chain,0,$backFilter+1);		//delete filter history to position
				$filter_chain = $reduceFilter;
			}
		}	
	}

	$debug = $_REQUEST['debug'];
	$detail = $_REQUEST['detail'];

	//DIA server connection object
	$dia = new Dia($site, $col, $count, $output, $lang);	
	$page= new Page();

	$initial_restricion = html_entity_decode($colectionData->restriction);
	// filtro de pesquisa = restricao inicial  E filtro where  E filtro externo E filtro(s) selecionados
	$filterSearch = array_merge((array)$initial_restricion,(array)$whereFilter, (array)$filter,(array)$filter_chain);

	// set additiona parameters
	$dia->setParam('fb',$fb);
	$dia->setParam('fl',$fl);
	$dia->setParam('qt',$qt);
	$dia->setParam('sort',$sort);

	$diaResponse = $dia->search($q, $index, $filterSearch, $from);
	$result = json_decode($diaResponse);

	if ($output == "xml" || $output == "sol"){
		header("Content-type: text/xml; charset=UTF-8");
		print $diaResponse;
	}else if($output == "rss"){
		header("Content-type: text/xml; charset=UTF-8");
		$page->RSS();
	}else if($output == "ris"){
		header("Content-type: application/x-Research-Info-Systems; charset=UTF-8");
        header('Content-Disposition: attachment; filename="citation.ris"');
		$page->RIS();
	}else if($output == "metasearch"){
		header("Content-type: text/xml; charset=UTF-8");
		$page->MetaSearch();
    }else if($output == "js"){
        header("Content-type: text/plain; charset=UTF-8");
        if (isset($callback) && ereg("^[a-z_]{1,25}$", $callback)){
            echo $callback . "(" . $diaResponse . ");";
        }else{
            echo $diaResponse;
        }
	}else{		
		// html output
		$page->show();
	}

	flush();
	// log de pesquisas realizadas
	$log = new Log();
	$log->fields['ip']   = $_SERVER["REMOTE_ADDR"];
	$log->fields['lang'] = $lang;
	$log->fields['col']  = $col;
	$log->fields['site'] = $site;
	$log->fields['query']= ($q != ''? $q : "*");
	$log->fields['index']= ($index != ''? $index : "*");
	$log->fields['where']= ($_REQUEST['where'] != ''? $_REQUEST['where'] : "*");
	$log->fields['filter'] = $dia->getFilterParam();
	$page = (($from-1)/$count) + 1;
	$log->fields['from'] = (strval($page) < 1? "1": $page);

	$log->writeLog();

?>
