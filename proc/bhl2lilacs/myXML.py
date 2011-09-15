import xml.etree.ElementTree as etree


class MyXML:
    root = {}
    def __init__(self, xml_file, xml_content, debug=False):
        if xml_file=='':
            xml_file = 'xml'
            f = open(xml_file,'w')
            f.write(xml_content)
            f.close()
        self.root = etree.parse(xml_file).getroot()
        if debug:
            print('root')
            print(self.root)
            print('root attributes')
            print(self.root.tag)
        if '{' in self.root.tag:
            self.ns = self.root.tag[0:self.root.tag.find('}')+1]
        else:
            self.ns = ''
        self.debug = debug

    def get_nodes(self, xpath, current_node = None):
        #'//{http://www.w3.org/2005/Atom}link'
        r = []
        n = current_node
        if n == None:
            n = self.root

        if n:
            p = './/' + self.ns + xpath
            #p = xpath
            if self.debug:
                print('---- DEBUG get_nodes')
                print('xml of current node:')
                print(etree.tostring(n))
                print('xpath:' + p)

            r = n.findall(p)

            if self.debug:
                print('resultado:')
                print(r)
                print('---- FIM DEBUG get_nodes')
        return r

    def get_text(self, xpath, current_node = None):
        #'//{http://www.w3.org/2005/Atom}link'
        n = current_node
        if n == None:
            n = self.root

        r =[]
        if n:
            if self.debug:
                print('---- DEBUG get_text')
                print('xml of current node:')
                print(etree.tostring(n))
                print('xpath:' + xpath)

            entries = self.get_nodes(xpath, n)

            for e in entries:
                test = e.text
                if test == None:
                    test = ''
                r.append(test)
            if entries == None:
                r.append('')

            if self.debug:
                print('resultado:')
                print(r)

                print('---- FIM DEBUG get_text')
        return r

    
