<?php

class IAHx
{
    //TODO
	var $IAHXSERVER = "";
	var $param = array();
	
	function IAHx($site, $collection, $count, $output, $lang ){
		global $config;

		$this->param["site"]  = $site;
		$this->param["col"]   = $collection;
		$this->param["count"] = $count;
		$this->param["output"]= $output;
		$this->param["lang"]  = $lang;
		$this->setIAHxServer( $config->search_server );
		
		return;
	}


	function setIAHxServer($server){
		$this->IAHXSERVER = $server;
		return;
	}
	
	function setParam($param, $value){
		if ($value != null && $value != ""){
			$this->param[$param] = $value;
		}
		return;
	}

	function search($query, $index, $filter,  $from){
		$this->param["op"] = "search";
		$this->param["q"] = $query;
		$this->param["index"] = $index;

		if ($from != "" && $from > 0){
			$this->param["start"] = ($from - 1);
		}
		
		if ( isset($filter) ){			
			$this->mountFilterParam($filter);
		}
		
		$searchUrl = $this->requestUrl();

		$result = $this->documentPost( $searchUrl );
		return trim($result);
	}	

	function mountFilterParam($filter){		
		$filter = $this->cleanArray($filter);		//remove valores vazios do array
		$fq = join(" AND ",$filter);
				
		$this->param["fq"] = stripslashes($fq);
		
		return;
	}


	function requestUrl()	{
		$urlParam = "";		
		reset($this->param);
		while (list($key, $value) = each($this->param))	{
			if ($value != ""){
				$urlParam .= "&" . $key . "=" . urlencode($value);
			}
		}
		$requestUrl = "http://" . $this->IAHXSERVER . "/iahx-controller/?" . substr($urlParam,1);
		//print $requestUrl;
		return $requestUrl;
	}
	
	function documentPost( $url )
	{ 
		global $debug;
		// Strip URL  
		$url_parts = parse_url($url);
		$host = $url_parts["host"];
		$port = ($url_parts["port"] ? $url_parts["port"] : "80");
		$path = $url_parts["path"];
		$query = $url_parts["query"];
		$result = "";
		$timeout = 10;
		$contentLength = strlen($query);

		if (isset($debug)){
			print "<b>iahx request:</b> " . $url . "<br/>";
		}
		// Generate the request header 
    	$ReqHeader =  
      		"POST $path HTTP/1.0\r\n". 
      		"Host: $host\r\n". 
      		"User-Agent: PostIt\r\n". 
      		"Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\n". 
      		"Content-Length: $contentLength\r\n\r\n". 
      		"$query\n"; 
		// Open the connection to the host 
		$fp = fsockopen($host, $port, $errno, $errstr, $timeout);
	
		fputs( $fp, $ReqHeader ); 
		if ($fp) {
			while (!feof($fp)){
				$result .= fgets($fp, 4096);
			}
		}

    	return substr($result,strpos($result,"\r\n\r\n")); 
	}

	function cleanArray($array) {
    	foreach ($array as $index => $value) {
        	if (empty($value)) unset($array[$index]);
    	}
    	return $array;
	}

	function getFilterParam(){
		return $this->param["fq"];
	}

}

?>