#region import bailam_f
from s00_bailam import get_24hformat_hour as bailam_f
#endregion import bailam_f


#region chambai
from s02_chambai import chambai

#region testkey_list
testcase_list = [
  {'input': {'hour_str':'6am'}, 'output':'6',     'tc_name': 'tc00'},

  {'input': ['6am'],            'output':'6',     'tc_name': 'tc01'},
  {'input': ['7 am'],           'output':'7',     'tc_name': 'tc02'},
  {'input': ['8AM'],            'output':'8',     'tc_name': 'tc03'},
  {'input': ['9 AM'],           'output':'9',     'tc_name': 'tc04'},

  {'input': ['6pm'],            'output':'18',     'tc_name': 'tc05'},
  {'input': ['7 pm'],           'output':'19',     'tc_name': 'tc06'},
  {'input': ['8PM'],            'output':'20',     'tc_name': 'tc07'},
  {'input': ['9 PM'],           'output':'21',     'tc_name': 'tc08'},

  {'input': ['10 AM'],          'output':'10',     'tc_name': 'tc09'},
  {'input': ['11 AM'],          'output':'11',     'tc_name': 'tc10'},
  {'input': ['10 PM'],          'output':'22',     'tc_name': 'tc11'},
  {'input': ['11 PM'],          'output':'23',     'tc_name': 'tc12'},

]
#endregion testkey_list

ketqua_list = []
for tc in testcase_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)
  
  ketqua_list.append({
    'tc_name'    : tc['tc_name'],
    'tc_score'   : tc_score,  
    'o_TESTCASE' : tc['output'],    
    'o_BAILAM'   : o_BAILAM,  
  })
#endregion chambai

#region in ketqua
print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_TESTCASE = {kq['o_TESTCASE']}
o_BAILAM   = {kq['o_BAILAM']}
  '''.strip()+'\n')

print('\n---ketqua')
for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
#endregion in ketqua
