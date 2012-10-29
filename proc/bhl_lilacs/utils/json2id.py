# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime


class JSON2IDFile:
    """
    Class which creates an ID file from JSON (ISIS) document
    """
    def __init__(self, filename, report, convert2iso = False, encoding = 'iso-8859-1'):
        """
        Arguments: 
        filename -- path and file name for ID file
        report   -- object Report
        """
        self.convert2iso = convert2iso
        self.encoding = encoding
        self.filename = filename
        self.report = report
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        
        
    def format_and_save_document_data(self, json_data):
        """
        Arguments: 
        records_order -- list of dictionary keys of json data that are related to each record
        json_data   -- data in json format
        """
        record_number = 0

        f = open(self.filename, 'w')
        f.close()
        
        
        if type([]) == type(json_data):
            # is a list of record of same type
            for rec_occ in json_data:
                record_number += 1
                self.save_record_number(record_number)
                self.save_document_data(rec_occ)
        else:
            if type({}) == type(json_data):            
                record_number += 1
                self.save_record_number(record_number)
                self.save_document_data(json_data)
                
    
                
    def save_record_number(self, record_number):
        record_id = '000000' + str(record_number)
        record_id = record_id[-6:]
        self.__write__('!ID ' + record_id + "\n")
        
    
    
    def save_document_data(self, fields_info):
        if type(fields_info) == type({}):
            #print(fields_info.keys())
            tag_list = [ int(tag) for tag in fields_info.keys() if tag.isdigit()]
            

            tag_list.sort()
            #print(tag_list)
            for t in tag_list:
                
                tag = str(t)
                field_occs = fields_info[tag]
                if type(field_occs) == type([]):
                    for field_occ in field_occs:
                        self.format_field_occ(tag, field_occ)
                else:
                    self.format_field_occ(tag, field_occs)            
        
    def format_field_occ(self, t, field_occ):
        """
        field_occ -- str (string) or [] (repetitive field (with/without subf) or {} (field with subfields)
        """ 
        if type(field_occ) == type({}):
            tagged = ''
            for subf_label, subf_occs in field_occ.items():
                # subf_content = str or []
                if type(subf_occs) == type([]):
                    # campo repetitivo 
                    for subf_occ in subf_occs:
                        s = self._convert_value_(subf_occ)
                        s = self.format_subfield(subf_label, s, '')
                        s = self.tag_it(t, s)
                        self.__write__(s)
                else:
                    # campo com varios subcampos
                    s = self._convert_value_(subf_occs)
                    tagged = self.format_subfield(subf_label, s, tagged)
            if len(tagged)>0:
                s = self.tag_it(t, tagged)
                self.__write__(s)
        else:
            if type(field_occ) == type([]):  
                for tagged in field_occ:
                    self.format_field_occ(t, tagged)
            else:    
                if type(field_occ) == type(''):
                    s = self._convert_value_(field_occ)
                    s = self.tag_it(t, s)
                    self.__write__(s)
        
    def format_subfield(self, subf_label, subf_content, content):
        if subf_label == '_':
            content = subf_content + content
        else:
            content += '^' + subf_label + subf_content
            
        return content
        
    def tag_it(self, tag, content):
        
        tag = '000' + tag
        return '!v' + tag[-3:] + '!' + content + "\n"
            
    def _convert_value_(self, value):
        if self.convert2iso:
            r = self.utf8_2_iso(value)
        else:
            r = value
        return r

    def utf8_2_iso(self, utf8):
        utf8 = utf8.replace('\ufeff','')
        
        try:
            print('try 1')
            b = utf8.encode('iso-8859-1')
            iso = b.decode('iso-8859-1')
        except:
            print('except 1')

            if ' ' in utf8:
                words = utf8.split(' ')
                sep = ' '
            else:
                words = utf8 
                sep = ''
            new = []
            for w in words:
                if len(w)==1:
                    print('char')
                    try: 
                        print('try ord')
                        n = ord(w)
                        i = w 
                    except:
                        print('except ord')
                        try:
                            print('try num ent')
                            n = 256*ord(w[0]) + ord(w[1])

                            i = '&#' + str(hex(n)) + ';'
                        except:
                            print('except num ent')
                            i = '?'
                else:
                    print('word')
                    i = self.utf8_2_iso(w)
                
                    
                new.append(i)
            iso = sep.join(new)
        
        
        return iso

      
    
                        
    def __write__(self, content):
        
        try:
            f = open(self.filename, 'a+')
            f.write(content)
            f.close()

        except:
            try:
                self.report.write('Writing as binary ' + self.filename)
            
                f = open(self.filename, 'a+b')
                f.write(content.encode(self.encoding))
                f.close()

            except:
                self.report.write('Unable to write content in id filename ' + self.filename + ' ' + content , False, True)
            
        
