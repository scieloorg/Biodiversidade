// DIA-client javascript functions

function showhideLayers(divId)
{ //v1.0
	var v,divObj;

	if ((divObj=MM_findObj(divId))!=null) {
      v=divObj.style.display;

      if (v == 'none' )	{
        disp = 'block';
      }else {
        disp = 'none';
     }
     divObj.style.display = disp;
 }

}

function showLayer(divId)
{ //v1.0
	var v,divObj;

	if ((divObj=MM_findObj(divId))!=null) {
    	v=divObj.style.display;
		disp = 'block';
    	divObj.style.display = disp;
 	}
}

function hideLayer(divId)
{ //v1.0
	var v,divObj;

	if ((divObj=MM_findObj(divId))!=null) {
    	v=divObj.style.display;
		disp = 'none';
    	divObj.style.display = disp;
 	}
}

function showHideBox(divId)
{
	var box = document.getElementById(divId);
	if (box.className.indexOf("closed") == -1){
		box.className = box.className + " closed";
	}else{
		box.className = box.className.replace("closed","");
	}
	return false;
}

function showHideAbstract(nodeId) {
  var divShort, divFull;

  divShort = 'short-' + nodeId;
  divFull  = 'full-' + nodeId;
  showhideLayers(divShort);
  showhideLayers(divFull);

}

function MM_findObj(n, d)
{ //v4.01
        var p,i,x; if(!d) d=document;
        if((p=n.indexOf("?"))>0&&parent.frames.length)
        {
                d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);
        }
        if(!(x=d[n])&&d.all)
                x=d.all[n];
        for (i=0;!x&&i<d.forms.length;i++)
                x=d.forms[i][n];
                for(i=0;!x&&d.layers&&i<d.layers.length;i++)
                        x=MM_findObj(n,d.layers[i].document);
                if(!x && d.getElementById)
                        x=d.getElementById(n);
        return x;
}

function openWindow ( url, params ){
	var d = new Date();
	var winId = d.getDate() + d.getHours() + d.getMinutes() + d.getSeconds();

	newWindow = window.open(url, winId , params);
	newWindow.focus();
	return;
}

function postHref ( href, target){
	var hrefAction = href.substring(0,href.indexOf('?'));
	var hrefParameters = href.substring(href.indexOf('?')+1);
	var splitedHref = hrefParameters.split("&");
	var qtt = splitedHref.length;
	var splitedHidden = new Array();
	var hiddenName = "";
	var hiddenValue = "";
	var submitForm = document.formHref;

	if ( target == '' || !target ){
		target = 'postHref';
	}

	submitForm.action = hrefAction;
	submitForm.target = target;

	for ( var i = 0; i < qtt; i++ )
	{
		splitedHidden = splitedHref[i].split("=");
		hiddenName = splitedHidden[0];
		splitedHidden[0] = "";
		hiddenValue = splitedHidden.join("=");
		hiddenValue = hiddenValue.replace(/%20/g,' ');
		hiddenValue = hiddenValue.replace(/%2F/g,'/');
		hiddenValue = hiddenValue.replace(/\+/g,' ');

		submitForm.elements[i].name = hiddenName;
		submitForm.elements[i].value = hiddenValue.substring(1);
	}

	//resultWindow = window.open('about:blank',target);
	//resultWindow.focus();

	submitForm.submit();
	// realizar testes de compatibilidade do codigo abaixo
	resultWindow = window.open('',target);
	resultWindow.focus();
}


function openDeCS(){

	lang = document.metasearch.lang.value;
	if (lang == "pt"){ decsLang = "p"; }
	if (lang == "es"){ decsLang = "e"; }
	if (lang == "en"){ decsLang = "i"; }

	decsUrl = "http://decs.bvs.br/cgi-bin/wxis1660.exe/decsserver/?IsisScript=../cgi-bin/decsserver/decsserver.xis&interface_language=" + decsLang + "&previous_page=homepage&previous_task=NULL&task=start";
	decsWindow = window.open(decsUrl, "decs", "height=550,width=750,menubar=yes,toolbar=yes,location=no,resizable=yes,scrollbars=yes,status=no");
	decsWindow.focus();

	return;

}

function showDeCSTerm( id ){

	lang = document.formSearch.lang.value;
	if (lang == "pt"){ decsLang = "p"; }
	if (lang == "es"){ decsLang = "e"; }
	if (lang == "en"){ decsLang = "i"; }

	decsUrl = "http://decs.bvs.br/cgi-bin/wxis1660.exe/decsserver/?IsisScript=../cgi-bin/decsserver/decsserver.xis&interface_language=" + decsLang + "&search_language=" + decsLang + "&previous_page=homepage&task=exact_term&search_exp=mfn=" + id + "#RegisterTop";
	decsWindow = window.open(decsUrl, "decsTerm", "height=450,width=630,menubar=yes,toolbar=yes,location=no,resizable=yes,scrollbars=yes,status=no");
	decsWindow.focus();

	return;
}

function changeLang(lang ){
	form = document.formMain;
	form.lang.value = lang;
	if (home == "true"){
		form.task.value = 'init';
	}
	form.submit();
	return;
}

function changeUrlParameter( parName, parValue ){
	var url = document.URL;
	var parPos = url.indexOf( parName + "=" )

	if( parPos == -1 ) return null;

	var section = url.substring( parPos );
	var eop = section.indexOf("&");

	if( eop == -1 ){
		url = url.replace( section, parName+"="+parValue );
	} else {
		section = section.substring( 0, eop);
		url = url.replace( section, parName+"="+parValue );
	}
	return url;
}

function changeFormParameter( parName, parValue ){

	var form = document.forms[0];
	form.elements[parName].value = parValue;

    form.submit();
}

function applyFilter( query, index ){
	var form = document.forms[0];
	var filter = form.addfilter;

	filter.value = index + ":\"" + query + "\"";
	form.submit();
}

function newSearch( ){
	var form = document.forms[0];
	var backfilter = form.backfilter;
	//clear filter
	backfilter.value = "-1";

	// don't add blank queries
	if( !form.q.value.match(/^\s*$/) )
		addSearchToHistory( form.q.value );

	form.submit();
}

function changeCollection( _col, _site  ){
	var form = document.forms[0];

	form.col.value = _col;
	form.site.value = _site;
	form.backfilter.value = "-1";

	form.submit();
}


function refineByIndex( query, index){
	var form = document.forms[0];

	var formQuery = form.q;
	var formIndex = form.index;
        var formWhere = form.where;
	var backfilter = form.backfilter;

	// set the new query expression
	formQuery.value = "\"" + query + "\"";

	// set the new index
        if (formIndex != null){
            for ( i = 0; i < formIndex.length; i++ ) {
		currentIndex = formIndex[i];
		if (currentIndex.value == index){
			currentIndex.selected = true;
		}
            }
        }
	// clear history filter
	backfilter.value = "-1";
        
        // set where (source) parameter to all
        if (formWhere != null ){
            if ( isArray(formWhere) ){
                formWhere[0].selected = true;
            }else{
                formWhere.value = "";
            }
        }
	form.submit();
}

function detail(id){
	var form = document.forms[0];

	var formQuery = form.q;
	var backfilter = form.backfilter;

	// set the new query expression
	formQuery.value = "detail:" + id;
	// clear history filter
	backfilter.value = "-1";
	form.submit();
}


function backHistoryFilter( pos ){
	var form = document.forms[0];
	var backfilter = form.backfilter;

	backfilter.value = pos;

	form.submit();
}

/* Funções para marcação de ocorrências favoritas (estrelas) */
var xmlhttp = createAjax();

/**
 * Cria instância do XMLHttpRequest
 * @return XMLHttpRequest;
 */
function createAjax(){
	var xmlhttp = null;
	if (window.XMLHttpRequest){
		xmlhttp=new XMLHttpRequest();
	}else if (window.ActiveXObject){
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	return xmlhttp;
}

/**
 * Faz POST através do AJAX e retorna
 * a reposta do processo caso a resposta
 * exista
 * @param {String} page
 * @param {String} vars
 * @return {String} responseText
 */
function postVars(page,vars){
	if(!xmlhttp){
		xmlhttp = createAjax();
	}
	xmlhttp.open('POST',page,false);
	xmlhttp.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
	xmlhttp.send(vars);
	return xmlhttp.responseText;
}

/**
 * Adiciona ou remove ocorrência dos favoritos
 * @param {Node} element
 * @param {String} id
 */
function markUnmark(element,id){
  var state = element.getAttribute('state');
  var link = document.getElementsByTagName('a')[1];

  if(state == "u"){
    element.src = "./image/common/box_selected.gif";
    element.setAttribute('state','s');
	postVars("bookmark.php","action=a&id="+id);
  }else if(state == "s"){
    element.src = "./image/common/box_unselected.gif";
    element.setAttribute('state','u');
	postVars("bookmark.php","action=r&id="+id);
  }
	refreshElements();
}

function markAll(){
	var ids = '';
	$('div.record').each(
		function(){
			ids += this.id + '|';
			$('div.yourSelectionCheck img',this).each(
				function(){
					this.src = './image/common/box_selected.gif';
					this.state = 's';
				}
			)
		});
	postVars("bookmark.php","action=a&id="+ids);
	refreshElements();
}

function unmarkAll(){
	var ids = '';
	$('div.record').each(
		function(){
			ids += this.id + '|';
			$('div.yourSelectionCheck img',this).each(
				function(){
					this.src = './image/common/box_unselected.gif';
					this.state = 'u';
				}
			)
		});
	postVars("bookmark.php","action=r&id="+ids);
	refreshElements();
}

/**
 * Altera elementos conforme o usuário
 * seleciona documento.
 */
function refreshElements(){
	window.listSize = parseInt( postVars("bookmark.php","action=s") );
	var selectionListOptions = document.getElementById('yourSelection').getElementsByTagName('ul')[0];

	if( listSize == 0 ){
		selectionListOptions.style.display = "none";
	}else{
		selectionListOptions.style.display = "block";
	}
	countBookmarksTo("sizeOfBookmarks_0",listSize);
	countBookmarksTo("sizeOfBookmarks_1",listSize);
	countBookmarksTo("sizeOfBookmarks_2",listSize);
}

/**
 * Lê os favoritos de uma sessão PHP e
 * "acende" as respectivas estrelas
 */
function recoverBookmarks(){
	var bookmarks = postVars("bookmark.php","action=l");
	bookmarks = bookmarks.split(';');

	for(var i = 0; i < bookmarks.length; i++){
		var register = document.getElementById(bookmarks[i]);
		if(register){
			var divs = register.getElementsByTagName('div');
			for(var j = 0; j < divs.length; j++){
				if( divs[j].className == "yourSelectionCheck" ){
					var image = divs[j].getElementsByTagName('img')[0];
					image.src = "./image/common/box_selected.gif";
					image.setAttribute('state','s');
				}
			}
		}
	}
	refreshElements();
}

/**
 * Faz uma pesquisa usando os ids dos
 * favoritos da sessão PHP e mostra o
 * resultado para o usuário.
 */
function showBookmarks(){
	var form = document.forms[0];
	var input = form.getElementsByTagName('input');
	var query = form.q;
	var bookmarks = postVars("bookmark.php","action=l");
	var searchStrategy = "";
	bookmarks = bookmarks.split(';');

	// remove filtros de outras pesquisas
	for( var i = 0; i < input.length; i++){
		if( input[i].name.search('filter') != -1 ){
			input[i].value = "";
		}
	}

	if(bookmarks){
		searchStrategy = "\""+bookmarks[0]+"\"";
		for(i = 1; i < bookmarks.length; i++){
			searchStrategy += " OR \""+ bookmarks[i]+"\"";
		}

		query.value = "+id:(" + searchStrategy + ")";
		form.submit();
        query.value = "";
	}
}

function clearBookmarks(){
	postVars("bookmark.php","action=c");
}

function countBookmarksTo(id,listSize){
	var element = document.getElementById(id);
	element.innerHTML = listSize;
}

function cookiesEnabled(){
	document.cookie = "CookieTest=Enabled";
	var allcookies = document.cookie;
	var pos = allcookies.indexOf("CookieTest=");
	if (pos != -1) {
		var start = pos + 11;
		var end = allcookies.indexOf(";", start);
		if (end == -1) end = allcookies.length;
		var value = allcookies.substring(start,end);
		value = unescape(value);

		return value == "Enabled";
	}
	return false;
}

/**
 * Esconde elementos de uma determinada classe
 * @param {String} tagName
 * @param {String} className
 */
function hideClass(tagName,className){
	var elements = document.getElementsByTagName(tagName);

	for(var i = 0; i < elements.length; i++){
		if( elements[i].className == className ){
			elements[i].style.display = "none";
		}
	}
}

/**
 * Notifica o usuário sobre a impossibilidade
 * de se trabalhar com "Bookmarks"
 */
function alertBookmarkUnavailable(){
	var bb = document.getElementById('bookmark_button');
	var text = document.createTextNode("Cookies desabilitados!");
	bb.appendChild(text);
	bb.style.border = "1px solid #FF0000";
	bb.style.backgroundColor = "#FFEEEE";
	bb.style.textAlign = "center";
}

/* Funções para o searchHistory */

/**
 * Adiciona termo pesquisado
 * lista de termos presente na
 * sessão
 * @param {String} term
 */
function addSearchToHistory(term){
	term = escape(term);
	postVars("searchHistory.php","action=a&term="+term);
}

function removeSearchTerm(term,node){
	var shl = document.getElementById('searchHistoryList');
	var counter = document.getElementById('sizeOfHistorySearch');
	postVars("searchHistory.php","action=r&term="+term);
	shl.removeChild(node);
	counter.innerHTML = parseInt(counter.innerHTML) - 1;
	if(counter.innerHTML == "0"){
		shl.innerHTML = postVars("searchHistory.php","action=l");
	}
}

function eventPosition(e){
	var coord = [];

	if (!e) e = window.event;

	if (e.pageX || e.pageY){
		coord[0] = e.pageX;
		coord[1] = e.pageY;
	}else if (e.clientX || e.clientY){
		coord[0] = e.clientX + document.body.scrollLeft
			+ document.documentElement.scrollLeft;
		coord[1] = e.clientY + document.body.scrollTop
			+ document.documentElement.scrollTop;
	}
	return coord;
}

function chooseOperatorToSearch(sTerm,e){
	sTerm = unescape(sTerm);
	var coord;
	var form = document.forms[0];
	var operatorBox = document.getElementById("searchHistoryOperators");

	coord = eventPosition(e);
	if( form.q.value == "" ){
		form.q.value = sTerm;
	}else{
		operatorBox.style.left = coord[0]+"px";
		operatorBox.style.top = coord[1]+"px";
		operatorBox.style.display = "block";
		operatorBox.term = sTerm;
	}
}

/**
 * Adiciona um termo do histórico
 * de pesquisa no formulário de
 * pesquisa.
 * @param {String} operator
 */
function addTermToSearch(operator){
	var term = document.getElementById('searchHistoryOperators').term;
	var form = document.forms[0];

	// enclose term from history with parenthesis
	if(term.search(" ") > -1 )
		if(!term.match(/\)$/))
			term = "(" + term + ")";

	// enclose term from input with parenthesis
	if(form.q.value.search(" ") > -1)
		if(!form.q.value.match(/\)$/))
			if(!form.q.value.match(/\s+(AND|OR)\s+/))
				form.q.value = "(" + form.q.value + ")";

	// add to input field
	form.q.value = form.q.value + " " + operator + " " + term;
	document.getElementById('searchHistoryOperators').style.display = "none";
}

function searchFromHistory(term){
	var form = document.forms[0];
	form.q.value = term;
	form.submit();
}

function enableDisableForm(form){
	if( !window.listSize && !form.q.value && !document.searchForm['filter_chain[]']){
		for(var i=0;i<form.length;i++){
			form[i].disabled = true;
		}
	}else{
		for(i=0;i<form.length;i++){
			form[i].disabled = false;
		}
        if(!window.listSize){
            form.option[0].disabled = true;
            form.option[1].checked = true;
        }
        if(!form.q.value && !document.searchForm['filter_chain[]']){
            form.option[1].disabled = true;
            form.option[2].disabled = true;
            form.option[1].checked = false;
            form.option[2].checked = false;
        }
	}
}

function sendMail(form){
	var sendingMail = document.getElementById('sendingMail');
	var mailSent = document.getElementById('mailSent');
	var mailError = document.getElementById('mailError');

	var error = false;
	var vars = '';
	for(var i=0;i<form.length;i++){
		if (form[i].type == 'radio') {
            if(form[i].checked == true)
                vars += '&'+form[i].name+'='+ form[i].value;
		} else if(form[i].type == 'text'){
			vars += '&'+form[i].name+'=';
			if (form[i].value) {
				vars += form[i].value;
				form[i].style.backgroundColor = '#FFF';
			}else {
				error = true;
				form[i].style.backgroundColor = '#FAA';
			}
		} else {
            vars += '&'+form[i].name+'='+form[i].value;
        }
	}
    // add filter_chain to query 
    if(document.searchForm['filter_chain[]'] != null){
        if(document.searchForm['filter_chain[]'].length == undefined){
            vars += '&filter_chain[]=' + document.searchForm['filter_chain[]'].value;
        }else{
            for(i=0;document.searchForm['filter_chain[]'].length;i++){
                vars += '&filter_chain[]=' + document.searchForm['filter_chain[]'][i].value;
            }
        }
    }
    
    //alert(vars);
    
	if (!error) {
		mailSent.style.display = 'none';
		mailError.style.display = 'none';
		sendingMail.style.display = 'block';

		setTimeout(function(){
			var status = postVars('mail.php', vars);
			sendingMail.style.display = 'none';
			if (status.substring(0, 5) == "Error")
				mailError.style.display = 'block';
			else{
                setTimeout(function(){
                    mailSent.style.display = 'none';
                    sendingMail.style.display = 'none';
                } ,5000);
                mailSent.style.display = 'block';
            }
		}, 1000);
		//return true;
	}
	return false;
}

/**
 * Recupera o histórico de pesquisa
 * contido da sessão do usuário.
 */
function retrieveSearchTerms(){
	var searchHistoryList = document.getElementById("searchHistoryList");
	var sizeOfHistorySearch = document.getElementById("sizeOfHistorySearch");
	searchHistoryList.innerHTML = postVars("searchHistory.php","action=l");
	sizeOfHistorySearch.innerHTML = postVars("searchHistory.php","action=s");
}

function expandRetractResults(action){
	var refine_facet = document.getElementById('refine_facet');
	var box;
	if(action == "expand"){
		for( var i = 0; i < refine_facet.childNodes.length; i++){
			box = refine_facet.childNodes[i];
			if(box.tagName == "DIV"){
				if (box.className.indexOf("closed") > -1){
					box.className = box.className.replace("closed","");
				}
			}
		}
	}else if(action == "retract"){
		for( i = 0; i < refine_facet.childNodes.length; i++){
			box = refine_facet.childNodes[i];
			if(box.tagName == "DIV"){
				if (box.className.indexOf("closed") == -1){
					box.className = box.className + " closed";
				}
			}
		}
	}
}

function showInfo(msg,node,e){
	msg = unescape(msg);
	var coord = eventPosition(e);
	var div = document.createElement("DIV");

	coord[0] -= 10;
	coord[1] -= 10;

	div.innerHTML = msg;
	div.className = "popup altpopup";
	div.style.left = coord[0]+"px";
	div.style.top = coord[1]+"px";
	div.onmouseout = function(){
		var parent = this.parentNode;
		parent.removeChild(this);
	};

	node.appendChild(div);
}

function showPrintDialog(){
	var version = Math.round(parseFloat(navigator.appVersion) * 1000);
	if (version >= 4000){
		setTimeout("window.print()",1000);
	}
}

function printMode(printOption){
	var form = document.searchForm;
	var printMode = form.printMode;
	var from = form.from;
    var count = form.count;

	printMode.value = "true";
	from.value = form.pageFrom.value;
    if (printOption){
        for( i = 0; i < printOption.length; i++ ){
            if( printOption[i].checked == true ){
               var printValue = printOption[i].value;
            }
        }
        if (printValue == 'selection'){
            showBookmarks();
        }else if( printValue == 'all_references'){
            from.value = "1";
            count.value = "300";
        }
    }

	form.submit();

	//reset form values
	printMode.value = "";
	from.value = "";
}

function exportMode(exportOption){
	var form = document.searchForm;
	var exportMode = form.output;
	var from = form.from;
    var count = form.count;

    exportMode.value = "ris";
	from.value = form.pageFrom.value;
    if (exportOption){
        for( i = 0; i < exportOption.length; i++ ){
            if( exportOption[i].checked == true ){
               var exportValue = exportOption[i].value;
            }
        }
        if (exportValue == 'selection'){
            showBookmarks();
        }else if( exportValue == 'all_references'){
            from.value = "1";
            count.value = "300";
        }
    }

	form.submit();

	//reset form values
	exportMode.value = "";
	from.value = "";
}

function showMoreClusterItems(field, limit){
	var form = document.searchForm;
	form.action = form.action + "#" + field;
	var fb = form.fb;

	fb.value = field + ":" + limit;
	form.submit();

	//reset form values
	fb.value = "";
}

function changeOrderBy(field){
    var form = document.searchForm;
    var sort = form.sort;

    var fieldIndex = field.selectedIndex;


    sort.value = field[fieldIndex].value;
    form.submit();

    //reset form value
    sort.value = "";
}

function changeDisplayFormat(field){
    var form = document.searchForm;
    var fmt = form.fmt;

    var fieldIndex = field.selectedIndex;

    fmt.value = field[fieldIndex].value;
    form.submit();

    //reset form value
    fmt.value = "";
}


/**
 * Mostra janela com grafico do cluster selecionado
 * @param {Node} obj
 * @param {String} titulo
 * @param {String} id
 */
function showChart(obj, titulo, id){
	var regex = /\(\d+\)/;
	var params= "";

	var grupo = document.getElementById(id +'_set');
	var lista = grupo.getElementsByTagName('li');

	for (i = 0; i < lista.length; i++){
		cluster = lista[i].innerHTML;
		clusterLabel = lista[i].getElementsByTagName('a')[0].innerHTML;

		ma = regex.exec(cluster);
		if (ma != null) {
			clusterTotal = ma[0].replace(/[()]/g,'');
			params += "&l[]=" + clusterLabel + "&d[]=" + clusterTotal;
		}
	}
	// caso seja o cluster de ano passa parametro para realizar sort
	if (id == 'year_cluster'){
		params += "&sort=true";
	}
	url = "chart.php?title=" + titulo + params + "&KeepThis=true&TB_iframe=true&height=480&width=650";
	obj.href = url;
}

function clearDefault(id, newclass) {
	identity=document.getElementById(id);
	identity.className=newclass;
}

function isArray(o){
        return(typeof(o.length)=="undefined")?false:true;
}