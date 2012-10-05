import xml.etree.ElementTree as etree
import os

class XMLManager:

    root = {}
    debug = True

    def __init__(self, xml_filename, report):
        self.root = None
        self.report = report
        if os.path.exists(xml_filename):
            
            self.ns = ''
            try:
                self.root = etree.parse(xml_filename).getroot()
                if '{' in self.root.tag:
                    self.ns = self.root.tag[0:self.root.tag.find('}')+1]
                else:
                    self.ns = ''
            except:

                self.report.write('Unable to load ' + xml_filename, False, True)
                
        else:
            self.report.write('Missing XML file:' + xml_filename, False, True)
            
    def get_text(self, element_name, first = False):
        
        nodes = self.return_nodes('.//' + element_name)
        print(nodes)
        if first:
            text = ''
            if len(nodes)>0:
                text = nodes[0].text
        else:
            text = []
            text = [ n.text for n in nodes ]
               
        return text

    def return_nodes(self, xpath = '', current_node = None):
        r = []
        n = current_node
        if n == None:
            n = self.root

        if n != None:
            if xpath != '':
                if len(self.ns) == 0:
                    p =  xpath
                else:
                    if xpath.startswith('.//'):
                        p = './/' + self.ns  + xpath[3:]
                    elif xpath.startswith('./'):
                        p = './' + self.ns + xpath[2:]
                    else:
                        p = xpath
                print(p)
                try:
                    r = n.findall(p)
                except:
                    self.report.write('Invalid xpath: ' + p, False, True)
            else:
                p = '.'
                r.append(n)
            n_str = ''
            if len(n)>0:
                n_str = etree.tostring(n)
        return r

    def return_node_value(self, node):
        r = '' 
        s = ''
        if node != None:
            
            try:
                children = node.iter()
                s = self.return_node_value_iter(node, children)
            except:
                if node.text != None:
                    s = node.text
                
          
        return s
    
    def return_node_value_iter(self, node, children):
        
        for child in children:
            n +=1
        if n == 1:
            r = node.text
        if n > 1:
            r = etree.tostring(node)
            
            r = r[r.find('>')+1:]
            r = r[0:r.rfind('</')]
        try:
            s = r.strip()
        except:
            s = ''
            self.report.log_event('Empty element')
            self.report.display_data('node', node)
            self.report.display_data('n', n)
            self.report.display_data('r', r)        
        return s   
    
    def return_node_attr_value(self, node, attr_name):
        attr = '' 
        if node != None:
            if len(node.attrib)>0:
                if ':' in attr_name:
                    aname = attr_name[attr_name.find(':')+1:]
                    for k,a in node.attrib.items():
                        if aname == k[k.find('}')+1:]:
                            attr = a 
                else:
                    if attr_name[0:1] == '@':
                        attr_name = attr_name[1:]
                    try:
                        attr = node.attrib[attr_name]
                    except:
                        attr = ''
            
        return attr  
 
    
   
