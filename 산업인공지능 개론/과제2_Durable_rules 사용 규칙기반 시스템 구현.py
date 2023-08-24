from durable.lang import *
#01. IF 단계 == ‘체계’ & 판단=‘정의＇ THEN "체계는 탑재중량200kg 수송드론 체계이다“
#02. IF 단계 == ‘체계’ & 판단=‘구성＇ THEN "체계는 탑재중량200kg 체계는 지상체, 비행체, UAM 실증진흥센터로 구성되어야 한다.”
#03. IF 단계 == ‘시스템’ & 판단=‘운용＇ THEN "탑재중량200kg 수송드론 운용은 조종기방식, 자동항법방식(경로점 기반, Knob방식, 점항법방식)으로 운용한다.
#04. IF 단계 == ‘시스템’ & 판단=‘성능＇ THEN " 탑재중량200kg 수송드론 비행체의 체공시간은 1시간 이상이어야 한다(탑재중량 200kg, 수소연료 100%, 배터리 완충, AGL 600m이하(MSL 800m 이하), 국제 표준대기 기준)..
#05. IF 단계 == ‘부체계’ & 판단=‘정의＇ THEN “부체계는 지상체이다“
#06. IF 단계 == ‘부체계’ & 판단=‘구성＇ THEN "지상체는 지상통제장비, 연동처리장비, 지상데이터링크, 지상체 차량으로 구성되어야 한다.”
#07. IF 단계 == ‘부체계’ & 판단=‘통제＇ THEN " 지상체는 조종기방식, 노브(Knob)방식, 점항법방식 및 자동항법방식으로 비행체를 통제한다.”
#08. IF 단계 == ‘장비’ & 판단=‘정의＇ THEN 장비는 지상통제장비이다“
#09. IF 단계 == ‘장비’ & 판단=‘구성＇ THEN "지상통제장비는 주/보조통제장치, VME(TBD), SAR 신호처리기,유무선 공유기, 무정전전원공급장치, 외부조종기, HMD, 노브조립체로 구성되어야 한다..”
#10. IF 단계 == ‘장치’ & 판단=‘정의＇ THEN 장치는 주/보조통제장치이다“
#11. IF 단계 == ‘장치’ & 판단=‘구성‘  & 옵션=‘세부적인 내용＇ THEN " 주/보조통제장치는 주통제컴퓨터, 부통제컴퓨터, 모니터, '운용테이블, 조종장치(Knob, 외부조종기), 키보드/마우스, 노브조립체로 구성하여야 한다.
#12. IF 단계 == ‘장치’ & 판단=‘운용＇ THEN "주/보조통제장치는 외부조종기를 통해 비행체의 이/착륙 운용되어야 한다"
#13. IF 단계 == ‘장치’ & 판단=‘조종＇ THEN "주/보조통제장치는 노브(knob)방식으로 비행체의 고도, 속도, 헤딩/뱅크/코스를 조종하여야 한다.”
#14. IF 단계 == ‘장치’ & 판단=‘조종＇ THEN "주/보조통제장치는 점항법방식으로 비행체의 고도, 속도, 위치를 조종하여야 한다.”
#15. IF 단계 == ‘장치’ & 판단=‘조종혼합＇ THEN "주/보조통제장치는 점항법방식에서 노브를 통해 비행체 속도/고도를 조종가능하여야 한다.”
#16. IF 단계 == ‘장치’ & 판단=‘연동＇ THEN "~는 ~ 간에/와 연동하여야 한다.”
#17. IF 단계 == ‘장치’ & 판단=‘설계＇ THEN "~는 ~을 설계하여야 한다"
#18. IF 단계 == ‘장치’ & 판단=‘가능＇ THEN "~는 ~을 가능하여야 한다"
#19. IF 단계 == ‘장치’ & 판단=‘전송＇ THEN "~는 ~을 전송하여야 한다"
#20. IF 단계 == ‘장치’ & 판단=‘도시＇ & AI='' & 목적어=‘데이터링크의 상태정보＇ THEN “SRS(SW 요구사항): ~는 ~도시 할 수 있어야 한다'  
#21. IF 단계 == ‘장치’ & 판단=‘도시＇ & AI=‘SDD＇ & 목적어=‘데이터링크의 상태정보＇ THEN “(SW 상세설계): : ~ 기능은 ~세부기능을 ~를 화면에 도시 한다'  
#22. IF 단계 == ‘장치’ & 판단=‘도시＇ & AI=‘STP＇ & 목적어=‘데이터링크의 상태정보＇ THEN “(SW 시험계획서): ~ 기능은 ~세부기능을 ~를 화면을 선택하고 상태데이터를 확인 시험을 계획한다'  
#23. IF 단계 == ‘장치’ & 판단=‘도시＇ & AI=‘STD＇ & 목적어=‘데이터링크의 상태정보＇ THEN “(SW 시험절차서): : ~ 기능은 ~세부기능을 ~를 화면을 선택하고 상태데이터를 확인한다'  
#24. IF 단계 == ‘장치’ & 판단=‘도시＇ & AI=‘STR＇ & 목적어=‘데이터링크의 상태정보＇ THEN “(SW 시험결과서): : ~ 기능은 ~세부기능을 ~를 화면을 선택하고 상태데이터를 확인하고 결과를 입력한다'  

with ruleset('Requirement'):
    @when_all((m.step =='system') & (m.action == '정의'))
    def output(c):
        print('============={0} {1} {2}============='.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='system') & (m.action == '구성'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='system') & (m.action == '운용'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='system') & (m.action == '성능'))
    def output(c):
        print('{0}는 {1}{2}{3}'.format(c.m.subject, c.m.object, c.m.condition, c.m.predicate))
        for i in c.m.option:
            print('{0}'.format(i))
        print('조건 옵션 추가\n') 

    @when_all((m.step =='subsystem') & (m.action == '정의'))
    def output(c):
        print('\n============={0} {1} {2}============='.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='subsystem') & (m.action == '구성'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='subsystem') & (m.action == '통제'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate))

    @when_all((m.step =='Equipment') & (m.action == '정의'))
    def output(c):
        print('\n============={0} {1} {2}============='.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Equipment') & (m.action == '구성'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '정의'))
    def output(c):
        print('\n============={0} {1} {2}============='.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '구성'))
    def output(c):
        print('{0}는 {1} {2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '구성') & (+m.option))
    def output(c):
        for i in c.m.option:
            print('{0}'.format(i))
        print('구성 옵션 추가\n') 

    @when_all((m.step =='Device') & (m.action == '운용'))
    def output(c):
        print('{0}는 {1} {2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '조종'))
    def output(c):
        print('{0}는 {1}{2}{3}'.format(c.m.subject, c.m.tool, c.m.object, c.m.predicate))

    @when_all((m.step =='Device') & (m.action == '조종혼합'))
    def output(c):
        print('{0}는 {1}에서 {2}를 통해 {3}를 {4}'.format(c.m.subject, c.m.tool, c.m.tool_condition, c.m.object, c.m.predicate))

    @when_all((m.step =='Device') & (m.action == '연동'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '설계'))
    def output(c):
        print('{0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '가능'))
    def output(c):
        print('{0}는 {1}로 {2} {3}'.format(c.m.subject, c.m.object, c.m.complement, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '전송'))
    def output(c):
        print('{0}는 {1}을 비행체로 {2}'.format(c.m.subject, c.m.object, c.m.predicate)) 

    @when_all((m.step =='Device') & (m.action == '도시'))
    def output(c):
        if(('데이터링크의 상태정보' in c.m.subject) | ('데이터링크의 상태정보' in c.m.object)):
            if(c.m.AI==''):
                print('SRS(SW 요구사항): {0}는 {1}{2}'.format(c.m.subject, c.m.object, c.m.predicate))
                c.assert_fact({'AI':'SDD','step': 'Device','subject': '주/보조통제장치 데이터링크의 상태정보 기능', 'object' : ['통신개설', '지상안테나', '통신상태','암호화장비 상태'], 'predicate' :'를 화면에 도시 한다.', 'action':'도시'})
            if(c.m.AI=='SDD'):
                print('{0}(SW 상세설계): {1}는 {2}{3}'.format(c.m.AI, c.m.subject, c.m.object, c.m.predicate))
                c.assert_fact({'AI':'STP','step': 'Device','subject': '주/보조통제장치 데이터링크의 상태정보 기능', 'object' : ['통신개설', '지상안테나', '통신상태','암호화장비 상태'], 'predicate' :'를 화면을 선택하고 상태데이터를 확인 시험을 계획한다.', 'action':'도시'})
            if(c.m.AI=='STP'):
                print('{0}(SW 시험계획서): {1}는 {2}{3}'.format(c.m.AI, c.m.subject, c.m.object, c.m.predicate))
                c.assert_fact({'AI':'STD','step': 'Device','subject': '주/보조통제장치 데이터링크의 상태정보 기능', 'object' : ['통신개설', '지상안테나', '통신상태','암호화장비 상태'], 'predicate' :'를 화면을 선택하고 상태데이터를 확인한다.', 'action':'도시'})
            if(c.m.AI=='STD'):
                print('{0}(SW 시험절차서): {1}는 {2}{3}'.format(c.m.AI, c.m.subject, c.m.object, c.m.predicate))
                c.assert_fact({'AI':'STR','step': 'Device','subject': '주/보조통제장치 데이터링크의 상태정보 기능', 'object' : ['통신개설', '지상안테나', '통신상태','암호화장비 상태'], 'predicate' :'를 화면을 선택하고 상태데이터를 확인하고 결과를 입력한다', 'action':'도시'})
            if(c.m.AI=='STR'):
                print('{0}(SW 시험결과서): {1}는 {2}{3}\n'.format(c.m.AI, c.m.subject, c.m.object, c.m.predicate))



assert_fact('Requirement', {'AI':'','step': 'system','subject': '체계는', 'object' : ['탑재중량200kg 수송드론 체계'], 'predicate' :'이다', 'action':'정의'})
assert_fact('Requirement', {'AI':'','step': 'system','subject': '탑재중량200kg 수송드론 체계', 'object' : ['지상체','비행체','UAM 실증진흥센터'], 'predicate' :'로 구성되어야 한다.', 'action':'구성'})
assert_fact('Requirement', {'AI':'','step': 'system','subject': '탑재중량200kg 수송드론 체계', 'object' : ['조종기방식', '자동항법방식(경로점 기반, Knob방식, 점항법방식)'], 
                            'predicate' :'으로 비행체를 운용할 수 있어야 한다.', 'action':'운용'})
assert_fact('Requirement', {'AI':'','step': 'system','subject': '탑재중량200kg 수송드론 체계', 'object' : ['비행체의 체공시간은 '], 'condition' :'1시간 이상', 'predicate' :'이어야 한다', 
                            'action':'성능', 'option':['-탑재중량 200kg', '-수소연료 100%', '-배터리 완충', '-AGL 600m이하(MSL 800m 이하)', '-국제 표준대기 기준']})

assert_fact('Requirement', {'AI':'','step': 'subsystem','subject': '부체계는', 'object' : ['지상체'], 'predicate' :'이다', 'action':'정의'})
assert_fact('Requirement', {'AI':'','step': 'subsystem','subject': '지상체', 'object' : ['지상통제장비', '연동처리장비', '지상데이터링크', '지상체 차량'], 'predicate' :'로 구성되어야 한다.',
                            'action':'구성'})
assert_fact('Requirement', {'AI':'','step': 'subsystem','subject': '지상체', 'object' : ['조종기방식', '노브(Knob)방식', '점항법방식 및 자동항법방식'], 'predicate' :'으로 비행체를 통제할 수 있어야 한다.','action':'통제'})

assert_fact('Requirement', {'AI':'','step': 'subsystem','subject': '장비는', 'object' : ['지상통제장비'], 'predicate' :'이다', 'action':'정의'})
assert_fact('Requirement', {'AI':'','step': 'Equipment','subject': '지상통제장비', 'object' : ['주/보조통제장치', 'VME(TBD)', 'SAR 신호처리기','유무선 공유기', '무정전전원공급장치', '외부조종기', 
                                                                                         'HMD', '노브조립체'], 'predicate' :'로 구성되어야 한다.','action':'구성'})

assert_fact('Requirement', {'AI':'','step': 'Device','subject': '장치는', 'object' : ['주/보조통제장치'], 'predicate' :'이다', 'action':'정의'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['주통제컴퓨터','부통제컴퓨터','모니터','운용테이블','조종장치(Knob, 외부조종기)','키보드/마우스',
                                                                                        '노브조립체'], 'predicate' :'로 구성하여야 한다. ', 'action':'구성'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : '이중화를 위해 다음과 같이 동일한 하드웨어 각 1세트씩 총 2세트를', 'predicate' :' 구성하여야 한다. ', 
                            'action':'구성', 'option':['-주통제컴퓨터 1대','-부통제컴퓨터 1대','-모니터 2대','-주/보조통제용 운용테이블 1개','-조종장치(Knob, 외부조종기) 각 1개','-키보드/마우스 1세트',
                                                     '-노브조립체 1세트']})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'tool' : ['노브방식'],'object' : ['비행체의 고도', '속도', '헤딩/뱅크/코스'], 'predicate' :'를 조종하여야 한다.', 
                            'action':'조종'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'tool' : ['점항법방식'],'object' : ['비행체의 고도', '속도', '위치'], 'predicate' :'를 조종하여야 한다.', 
                            'action':'조종'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'tool' : ['점항법방식'],'tool_condition' : ['노브방식'],'object' : ['비행체의 고도', '속도'], 
                            'predicate' :'를 조종하여야 한다.', 'action':'조종혼합'})

assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['연동-데이터베이스 관리장치, SAR 신호처리기, 엣지컴퓨팅 서버'], 'predicate' :'와 연동해야 한다. ', 
                            'action':'연동'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['주통제장치', '보조통제장치'], 'predicate' :'간 연동해야 한다. ', 'action':'연동'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['외부조종기', '노브조립체','EO/IR조종기'], 'predicate' :'와 연동해야 한다. ', 'action':'연동'})

assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['반실시간(Part-time) 항목 도시','비행상황 확인'], 'predicate' :'UI를 설계하여야 한다.', 'action':'설계'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['외부조종기'] ,'complement':['비행체의  이륙 운용'], 'predicate' :'이 가능하여야 한다.', 'action':'가능'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['서치라이트 ON/OFF 통제명령'], 'predicate' :'전송할수 있어야 한다.', 'action':'전송'})
assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['항법등', '충동발지등 ON/OF 통제명령'], 'predicate' :'전송할수 있어야 한다.', 'action':'전송'})

assert_fact('Requirement', {'AI':'','step': 'Device','subject': '주/보조통제장치', 'object' : ['데이터링크의 상태정보'], 'predicate' :'를 화면에 도시할 수 있어야 한다.', 'action':'도시'})