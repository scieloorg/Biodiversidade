#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

# -*- conding: utf-8 -*-

__author__="jamil"
__date__ ="$Jun 22, 2011 9:00:16 AM$"

from urllib.request import *
import configparser
import json
import html


#Fixme log the process of this script

if __name__ == "__main__":

    def replaceEntities(str):
        return str.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')

#---------------------------Step 1----------------------------------------------
    listID = []
    
    #Get config file
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    listIssn = config.get('app', 'issns').split(',')

    if (len(sys.argv) > 1):
        if(sys.argv[1] == '--withup'):
            print('Get metadada from: ' + config.get('urls', 'url'))

            for i in range(len(listIssn)):
                print(config.get('urls', 'url') + config.get('view', 'article_id', vars = {'startkey':listIssn[i], 'endkey':listIssn[i] + 'ZZZZ'}))
                content = urlopen(config.get('urls', 'url') + config.get('view', 'article_id', vars = {'startkey':listIssn[i], 'endkey':listIssn[i] + 'ZZZZ'}))
                f = open(config.get('path', 'json_metadata', vars={'id': listIssn[i]}), 'wb')
                f.write(content.read())
                f.close()
    
#----------------------------Step 2---------------------------------------------

    content = '<?xml version="1.0" encoding="ISO-8859-1"?>'
    content += '<add>'

    f = open(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
    f.write(content)
    f.close()

    flagBG = False
    content = ''

    for i in range(len(listIssn)):

        print(config.get('path', 'json_metadata', vars = {'id': listIssn[i]}))

        try:
            if  os.path.exists(config.get('path', 'json_metadata',
                    vars = {'id': listIssn[i]})):

                dictIahx = json.loads(open(config.get('path', 'json_metadata', vars = {'id': listIssn[i]})).read())

                for j in dictIahx['rows']:
                    content += '<doc>'
                    content += '<field name="id">' + replaceEntities('scl-' + str([j][0]['doc']['v880'][0]['_']))  + '</field>'
                    content += '<field name="db">bhlb</field>'
                    content += '<field name="cc">BR1.1</field>'
                    content += '<field name="bvs">biodiversidade</field>'
                    content += '<field name="type">article</field>'
                    content += '<field name="ur">' + replaceEntities(config.get('urls', 'scielo', vars = {'pid': [j][0]['doc']['v880'][0]['_'], 'la': str([j][0]['doc']['v40'][0]['_'])})) + '</field>'
                    
                    if 'v10' in [j][0]['doc']:
                        for h in [j][0]['doc']['v10']:
                            if('n' in h and 's' in h ):
                               content += '<field name="au">' + replaceEntities(str(h['n']) + ' ' + str(h['s'])) + '</field>'
                               
                    if 'v12' in [j][0]['doc']:
                        content += '<field name="ti">' + replaceEntities(str([j][0]['doc']['v12'][0]['_'])) + '</field>'

                    if 'v85' in [j][0]['doc']:
                        for m in [j][0]['doc']['v85']:
                            if('k' in m):
                                content += '<field name="kw">' + replaceEntities(str(m['k'])) + '</field>'
                                
                    if 'v65' in [j][0]['doc']:
                        content += '<field name="dp">' + replaceEntities(str([j][0]['doc']['v65'][0]['_'])[0:4]) + '</field>'
                        
                    if 'v66' in [j][0]['doc'] or 'v67' in [j][0]['doc']:
                        content += '<field name="cp">' + replaceEntities(str([j][0]['doc']['v66'][0]['_']) + str([j][0]['doc']['v67'][0]['_'])) + '</field>'

                    if 'v40' in [j][0]['doc']:
                        content += '<field name="la">' + replaceEntities(str([j][0]['doc']['v40'][0]['_'][0].upper() + [j][0]['doc']['v40'][0]['_'][1])) + '</field>'

                    if 'v30' in [j][0]['doc']:
                        content += '<field name="ta">' + replaceEntities(str([j][0]['doc']['v30'][0]['_'])) + '</field>'
                    content += '</doc>'
                    
                #Save file to iahx
                f = open(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
                f.write(str(content))
                f.close()
        except Exception as err:
            print('Error: ' + config.get('path', 'json_metadata', vars = {'id': listIssn[i]}) + str(err))
            error = open(config.get('log', 'error', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
            error.write('Erro: ' + config.get('path', 'json_metadata', vars = {'id': listIssn[i]}) + '')
            error.close()

    f = open(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
    f.write('</add>')
    f.close()


















