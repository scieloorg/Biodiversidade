from BHL2LILACS import BHL2LILACS

import os
import sys

#
#global_excludes_brasil = True

# local de geracao
#xml_path = '../xml_path/'
#id_path = '../db/'

# access key
access_key="b64e048b-e947-44c2-b5e3-b9ba4e47fce0"

whattodo = sys.argv[1]
xml_path = sys.argv[2]
processed_list = sys.argv[3]
id_filename = sys.argv[4]

if len(sys.argv)>5:
    start_date = sys.argv[5]
if len(sys.argv)>6:
    end_date = sys.argv[6]

display_usage = False
more_message = []
if whattodo in ['download_all','download_incr' ]:
    if not os.path.exists(xml_path):
        display_usage = True
        more_message.append('Invalid PARAM2. ' + xml_path + ' must be a directory.')
    if not os.path.exists(processed_list):
        display_usage = True
        more_message.append('Invalid PARAM3. ' + processed_list + ' is not a file.')
    if not id_filename:
        display_usage = True
        more_message.append('Invalid PARAM4. It will be a file.')

    if whattodo=='download_incr':
        if start_date=='':
            display_usage = True
            more_message.append('Invalid PARAM5. It must be the start date.')
        if end_date=='':
            display_usage = True
            more_message.append('Invalid PARAM6. It must be the end date.')

else:
    display_usage = True
    





if display_usage == True    :
    print('python3 call_bhl2lilacs.py PARAM1 PARAM2 PARAM3 PARAM4 PARAM5 PARAM6')
    print('==> To download all documents')
    print('  PARAM1=download_all')
    print('  PARAM2=xml_path')
    print('  PARAM3=processed_id.seq')
    print('  PARAM4=id_filename')
    print('  ')
    print('==> To download most recent documents')
    print('  PARAM1=download_incr')
    print('  PARAM2=xml_path')
    print('  PARAM3=processed_id.seq')
    print('  PARAM4=id_filename')
    print('  PARAM5=start_date')
    print('  PARAM6=end_date')
    print('  ')
    for text in more_message:
        print(text + "\n")
    print('  ')
else:
    print('Executing ' + whattodo)
    bhl2lilacs = BHL2LILACS(xml_path, id_filename, True)
    if whattodo=='download_all':
        bhl2lilacs.create_id_filename(processed_list)
    else:
        if whattodo=='download_incr':
            bhl2lilacs.create_id_filename(processed_list, start_date, end_date)
        

    print(whattodo + ' finished.')
    