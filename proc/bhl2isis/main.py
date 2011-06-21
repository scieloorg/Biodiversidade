from bhl_xml import APIBHLXML
from bhl import APIBHL
from doc import Doc
from doc2isis import Doc2ISIS
#import chardet

access_key="b64e048b-e947-44c2-b5e3-b9ba4e47fce0"
xml_path = '../xml_path/'


title_file = xml_path + 'bhl_titles.xml'


apibhl = APIBHL(access_key)
doc2isis = Doc2ISIS()

if not os.path.exists(title_file):
    print('downloading ' + title_file)
    apibhl.query_title_list_and_save(title_file, 'xml')

print('loading ' + title_file)
apixml = APIBHLXML(title_file)
titleid_list = apixml.get_titleid_list()    


i = 0
i_iso = 0
i_utf8 = 0
f = open(output_path + 'records_iso.id','wb')
f2 = open(output_path + 'records_utf8.id','wb')

for id in titleid_list:
    if not os.path.exists(xml_path + id + '.xml'):
        print('downloading ' + id + '.xml')
        apibhl.query_title_and_save(xml_path + id + '.xml', 'xml', id)

    print('generating ' + id)
    apixml_title = APIBHLXML(xml_path + id + '.xml')
    records = doc2isis.generate_records(apixml_title.get_title_data())
    for r in records:
        i += 1
        #mfn = '000000' + str(i)
        #mfn = mfn[-6:]
        #isisrecord = '!ID ' + mfn + "\n" + r
        print(i)
        try:
            test = r.encode('iso-8859-1')
            i_iso += 1
            mfn = '000000' + str(i_iso)
            mfn = mfn[-6:]
            isisrecord = '!ID ' + mfn + "\n" + r
            e = bytes(isisrecord,'iso-8859-1')
            f.write(e)
        except:
            i_utf8 += 1
            mfn = '000000' + str(i_utf8)
            mfn = mfn[-6:]
            isisrecord = '!ID ' + mfn + "\n" + r
            e = bytes(isisrecord,'utf-8')                
            f2.write(e)
f.close()
f2.close()