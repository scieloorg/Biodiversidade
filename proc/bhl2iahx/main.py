#! /usr/bin/python3

# To change this template, choose Tools | Templates
# and open the template in the editor.

# -*- conding: utf-8 -*-

__author__="jamil"
__date__ ="$Jun 22, 2011 9:00:16 AM$"

from urllib.request import *
import configparser
import shutil
import json
import sys
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
    
    #Options
    #Caso seja uma atualização deve ser informado o param -withup
    #Nesse caso o arquivo que informa novos ids seram baixados
    if (len(sys.argv) > 1):
        if(sys.argv[1] == '-withup'):
            #Request the list of have subject="Brazil"
            print('Get the list of Titles')
            content = urlopen(config.get('methods', 'TitleSearchSimple'))

            #Save the list of subject="Brazil"
            print('Save list of Titles: ' + config.get('path', 'json_subjectTitles'))
            f = open(config.get('path', 'json_subjectTitles'), 'wb')
            f.write(content.read())
            f.close()
    
#----------------------------Step 2---------------------------------------------

    print('Get the id List from file: ' + config.get('path', 'json_subjectTitles'))
    
    #Transform json file in python dictonary
    dictTitles = json.loads(open(config.get('path', 'json_subjectTitles'),
        mode='r').read())
    
    #Loop to the dictionary generate (list)
    for i in dictTitles['Result']:
        #Deve ser avaliado se o ID ja existe
        #Opcao usar a diferenca entre duas listas Exemplos: list(set(List1-List2))
        if not os.path.exists(config.get('path', 'json_titlesMetadata',
                vars={'titleId': i['TitleID']})):
            listID.append(i['TitleID'])

    #Loop to the listID
    for j in range(len(listID)):
        content = urlopen(config.get('methods', 'GetTitleMetadata',
            vars = {'titleId':  listID[j]}))

        print("Request to: " + config.get('methods', 'GetTitleMetadata',
            vars = {'titleId':  listID[j]}))
        print('Save file metadata: ' + config.get('path', 'json_titlesMetadata',
            vars = {'titleId':  listID[j]}))
        f = open(config.get('path', 'json_titlesMetadata',
            vars = {'titleId':  listID[j]}), 'wb')
        f.write(content.read())
        f.close()

#----------------------------Step 3---------------------------------------------


    content = '<?xml version="1.0" encoding="UTF-8"?>'
    content += '<add>'

    f = open(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
    f.write(content)
    f.close()

    count = 1
    flagBG = False

    for i in dictTitles['Result']:
        print(count)
        print(config.get('path', 'json_titlesMetadata', vars = {'titleId': i['TitleID']}))
        content = ''
        try:
            if  os.path.exists(config.get('path', 'json_titlesMetadata',
                    vars={'titleId': i['TitleID']})):

                dictTitlesIahx = json.loads(open(config.get('path', 'json_titlesMetadata', vars = {'titleId': i['TitleID']})).read())

                content += '<doc>'
                content += '<field name="id">' + str(dictTitlesIahx['Result']['TitleID'])  + '</field>'

                for m in range(len(dictTitlesIahx['Result']['Subjects'])):
                    if (str(dictTitlesIahx['Result']['Subjects'][m]['SubjectText'])=='Brazil'):
                       flagBG = True

                if(flagBG == True):
                    content += '<field name="db">bhlb</field>'
                else:
                    content += '<field name="db">bhlg</field>'

                content += '<field name="cc">BR1.1</field>'
                content += '<field name="lo">' + replaceEntities(str(dictTitlesIahx['Result']['CallNumber'])) + '</field>'
                content += '<field name="bvs">biodiversidade</field>'

                if dictTitlesIahx['Result']['BibliographicLevel'] == 'Serial':
                    type = 'article'
                else:
                    type = 'book'

                content += '<field name="type">' + type + '</field>'
                content += '<field name="ur">' + replaceEntities(str(dictTitlesIahx['Result']['TitleUrl'])) + '</field>'

                for l in range(len(dictTitlesIahx['Result']['Authors'])):
                    content += '<field name="au">' + replaceEntities(str(dictTitlesIahx['Result']['Authors'][l]['Name'])) + '</field>'

                content += '<field name="ti">' + replaceEntities(str(dictTitlesIahx['Result']['FullTitle'])) + '</field>'

                for m in range(len(dictTitlesIahx['Result']['Subjects'])):
                    content += '<field name="kw">' + replaceEntities(str(dictTitlesIahx['Result']['Subjects'][m]['SubjectText'])) + '</field>'

                for n in range(len(dictTitlesIahx['Result']['Items'])):
                    content += '<field name="volume">' + replaceEntities(str(dictTitlesIahx['Result']['Items'][n]['Volume'])) + '</field>'
                    content += '<field name="item">' + replaceEntities(str(dictTitlesIahx['Result']['Items'][n]['ItemUrl'])) + '</field>'
                    content += '<field name="thumb">'+ replaceEntities(str(dictTitlesIahx['Result']['Items'][n]['ItemThumbUrl'])) +'</field>'

                for p in range(len(dictTitlesIahx['Result']['Items'])):
                    if 'Language' in dictTitlesIahx['Result']['Items'][p]:
                        if dictTitlesIahx['Result']['Items'][p]['Language'] != '':
                            content += '<field name="la">' + replaceEntities(str(dictTitlesIahx['Result']['Items'][p]['Language'])[0].upper() + str(dictTitlesIahx['Result']['Items'][p]['Language'])[1]) + '</field>'
                    break;
                        
                #if 'Year' in dictTitlesIahx['Result']['Items']:
                #    content += '<field name="da">' + replaceEntities(str(dictTitlesIahx['Result']['Items'][0]['Year'])) + '</field>'
                    
                content += '<field name="dp">' + replaceEntities(str(dictTitlesIahx['Result']['PublicationDate'])) + '</field>'
                content += '<field name="cp">' + replaceEntities(str(dictTitlesIahx['Result']['PublisherPlace'])) + '</field>'
                content += '<field name="ta">'+ replaceEntities(str(dictTitlesIahx['Result']['PublisherName'])) +'</field>'
                content += '<field name="entry_date">' + replaceEntities(str(time.localtime()[0] + time.localtime()[1] + time.localtime()[2])) + '</field>'
                content += '</doc>'
                
                #Counter
                count += 1
            #Save file to iahx
            f = open(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
            f.write(str(content))
            f.close()
        except Exception as err:
            print('Error: ' + config.get('path', 'json_titlesMetadata', vars = {'titleId': i['TitleID']}) . str(err))
            error = open(config.get('log', 'error', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
            error.write('Erro: ' + config.get('path', 'json_titlesMetadata', vars = {'titleId': i['TitleID']}) + '')
            error.close()

    f = open(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), 'a')
    f.write('</add>')
    f.close()

    if (len(sys.argv) > 1):
        if(sys.argv[2] == '-copy'):
         print('Copy from: ' + config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}) + ' To: ' + config.get('path', 'path_copy') + config.get('app', 'acron') + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.xml')
         shutil.copy(config.get('path', 'xml_iahx', vars = {'date': str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2])}), config.get('path', 'path_copy') + config.get('app', 'acron') + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.xml')
