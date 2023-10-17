def chambai(testcase, bailam_f):
  assert 'output' in testcase, 'MUST HAVE :output in testcase to score :bailam ^^'
  o_TESTCASE = testcase.get('output')

  assert callable(bailam_f), 'MUST HAVE bailam_f() method to score :bailam ^^'

  try:
    '''
    eg 
      testcase['input']: {'name':'Mom'}
    will run 
      bailam_f(name='Mom')
    '''
    o_BAILAM = bailam_f(**testcase['input'])  # aka input_DAPAN
  except:
    try:
      '''
      eg 
        testcase['input']: [1,2,3]
      will run 
        bailam_f(1,2,3)
      '''
      o_BAILAM = bailam_f(*testcase['input'])  # aka input_DAPAN
    except:
      o_BAILAM = None

  score01 = int(o_BAILAM == o_TESTCASE)
  return score01, o_BAILAM
