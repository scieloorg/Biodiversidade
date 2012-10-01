from utils.xml_manager import XMLManager
from utils.xml2json_table import XML2JSONTable
import json

class XML2JSONConverter:

    def __init__(self, xml2json_table_filename, debug_report, debug = False):
        self.conversion_table = XML2JSONTable(xml2json_table_filename)
        self.debug_report = debug_report
        self.debug = debug
        

    def convert(self, xml_filename):
        self.dict = {}
        self.xml_manager = XMLManager(xml_filename, self.debug_report)
        converted = self.__convert__(self.conversion_table.start, None, None)
        self.debug_report.display_data('converted', converted)  
        return converted 

    def pretty(self, json_data):
        return json.dumps(json_data, sort_keys=True, indent=4)
        
    def pretty_print(self, json_data):
        print(self.pretty(json_data))
        


    def __convert__(self, table_node, xml_parent_node, parent_xml_parent_node, num = 1):
        t = False
        #t = (table_node.xpath.startswith( 'xref' ))
        #self.debug = True
        test = False
        if self.debug:
            self.debug_report.display_data('__convert__ ', table_node.xpath)
        #print(' -- --- --')
        #print(table_node.xpath)
        #xpath, table_node.xpath = self.__return_new_xpath_and_table_xpath__(table_node)
        #print(xpath)
        #print(table_node.xpath)
        xml_nodes = self.xml_manager.return_nodes(table_node.xpath, xml_parent_node)
        #print(xml_nodes)
        if test:
            print(xpath)
            print(xml_nodes)
            print(table_node.xpath)
            test = False

        if len(table_node.children) == 0:
            if t: print('leaf')
            result = self.return_leaf_content(table_node, xml_nodes, num, t)

        else:
            if t: print('branch')
            result = self.return_branch_content(table_node, xml_nodes, xml_parent_node, num, t)
    
        if t:
            print(result)
        if self.debug:
            self.debug_report.display_data('result', result)  
        
        return result

    def return_leaf_content(self, table_node, xml_nodes, num, debug = False):
        a = []
        for xml_node in xml_nodes:
            
            if table_node.attr != '':
                v = self.xml_manager.return_node_attr_value(xml_node, table_node.attr[1:])
                
            else:
                v = self.xml_manager.return_node_value(xml_node)
            
            if v == '' or v == None:
                v = table_node.default
                
            if v != '':
                a.append(self._convert_value_(v))
            if debug:
                print('return_leaf_content')
                print(a)
        a = self.__format__(table_node, a)
        if debug:
            print(a)
        return a

    def return_branch_content(self, table_node, xml_nodes, xml_parent_node, num, debug = False):
        occs = []
        number = 0
        for xml_node in xml_nodes:
            # FIXME pode haver mais de uma instancia d{12}
            occ = {}
            number += 1
            for child in table_node.children:
                if debug: print(table_node.xpath + '=>' + child.xpath)
                v = self.__convert__(child, xml_node, xml_parent_node, number)
                if len(v)>0:
                    if child.to == '' or child.to == '_':
                        occ['_'] = v
                    else:
                        occ[child.to] = v
            if occ != {}:
                occs.append(occ)        
        if debug: print(occs)
        return self.__format__(table_node, occs, num)  

    def __format__(self, table_node, result, num = None):
        self.debugging('__format__', result)
        if len(result) == 0:
            r = ''
        else:
            r = result
            if type(result) == type([]) and len(result) == 1:
                r = result[0]
            if num != None:
                r = self.__control_occ__(table_node, num, r)
        self.debugging('__format__ result', result)
        return r

    def __control_occ__(self, table_node, num, result):
        self.debugging('__control_occ__', result)
        key = table_node.parent.to + '_' +  str(num) + '_' + table_node.to
        
        if key in self.dict.keys():
            if type(self.dict[key]) != type([]):
                s = self.dict[key]
                self.dict[key] = []
                self.dict[key].append(s)
                
            
            self.dict[key].append(result)
            result = self.dict[key]
            
        else:
            self.dict[key] = result
        self.debugging('__control_occ__ result', result)
        return result


    def x_convert_value_(self, value):
         return value
         
    def _convert_value_(self, value):
        self.debugging('_convert_value_', value)
        enc = 'utf-8'
        if value != '':
            try:
                test = value.encode(enc)
            except:
                test = self.convert_chr(value)
            if type(test) == type(''):
                value = test

        self.debugging('_convert_value_ result', value)
        return value

    def convert_chr(self, value):
        self.debugging('convert_chr', value)
        v = ''
        for c in value:
            try:
                v += c.encode('utf-8')
            except:
                try: 
                    n = ord(c)
                    
                except:

                    n = 256*ord(c[0]) + ord(c[1])
                    

                v += '&#' + str(hex(n)) + ';'
        self.debugging('convert_chr result', v)
        return v
    
    def debugging(self, label, value):
        if self.debug:
            print(label)
            print(value) 
    