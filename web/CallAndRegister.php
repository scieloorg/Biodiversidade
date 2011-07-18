<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
    
    
    class SciELOLogRegister {
        function SciELOLogRegister($log_script){
            $this->_script = $log_script; // http://scielo-log.bireme.br/scielolog/updateLog02.php
        }
        function getScript(){
            return $this->_script;
        }
        function setParameters($app, $page, $pid, $lang, $tlng){
            $this->_p['app']  = $app;
            $this->_p['page'] = $page;
            $this->_p['pid']  = $pid;
            $this->_p['lang'] = $lang;
            $this->_p['tlng'] = $tlng;
        }
        function getParameters(){

            foreach ($this->_p as $key => $value) {
                $parameters .= $key . '=' . $value . '&';
            }
            return  $parameters;
        }
        function registerLog(){
            $strReturn = file_get_contents($this->getScript().'?'.$this->getParameters());
        }
    }

    class CallAndRegister {
        function CallAndRegister(){

        }
        function execute_callandregister($logRegister, $call){
            if ($logRegister) $logRegister->registerLog();

            
            header('Location: '.$call);
        }
    }

    class SciELO_CallAndRegister {
        function SciELO_CallAndRegister(){
        }
        function execute_callandregister($log_script, $app, $page, $pid, $lang, $tlng, $call){
            if ($log_script){
                $logRegister = new SciELOLogRegister($log_script);
                $logRegister->setParameters($app, $page, $pid, $lang, $tlng);
            }
            $s = new CallAndRegister();
            $s->execute_callandregister($logRegister, $call);
        }
    }
?>
