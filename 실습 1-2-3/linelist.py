import re
from ArrayList import ArrayList

# 배열구조의 리스트를 이용한 라인 편집기 프로그램
list = ArrayList(1000)
while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, m-딕셔너리 생성, q-종료=> ")

    if command == 'i' :
        pos = int( input("  입력행 번호: ") )
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd' :
        pos = int( input("  삭제행 번호: ") )
        list.delete(pos)

    elif command == 'r' :
        pos = int( input("  변경행 번호: ") )
        str = input("  변경행 내용: ");
        list.replace(pos, str)

    elif command == 'p' :
        print('Line Editor')
        for line in range (list.size) :
            print('[%2d] '%line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l' :
        # filename = input("  읽어들일 파일 이름: ")
        filename = 'test.txt'
        infile = open(filename , "r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's' :
        # filename = input("  저장할 파일 이름: ")
        filename = 'test.txt'
        outfile = open(filename , "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()

    elif command == 'm' :
        dic={}
        cnt=0
        cleaned_sentence = re.sub(r'[^\w\s가-힣]', '', input('문장입력 : '))
        m_list= cleaned_sentence.split()
        
        for i in range(0,len(m_list)):
            cnt = m_list.count(m_list[i])
            print('%s : %d'%(m_list[i],cnt))
            dic[m_list[i]]=cnt

        filename = 'dic.txt'
        with open(filename, 'w') as f:
            for key, value in dic.items():
                f.write(f'{key}: {value}\n')