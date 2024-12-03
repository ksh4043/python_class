"""
1. 학생 정보 추가
2. 전체 성적 출력
3. 성적 검색
4. 성적 수정
5. 성적 삭제
6. 종료
선택: 1

학생 이름: 홍길동
학번: 2024001
과목: 파이썬
성적: 85

학생 정보가 추가되었습니다.

1. 학생 정보 추가
2. 전체 성적 출력
3. 성적 검색
4. 성적 수정
5. 성적 삭제
6. 종료
선택: 2

이름: 홍길동, 학번: 2024001, 과목: 파이썬, 성적: 85

1. 학생 정보 추가
2. 전체 성적 출력
3. 성적 검색
4. 성적 수정
5. 성적 삭제
6. 종료
선택: 3

학번: 2024001

홍길동, 파이썬, 85
"""
import os
import Student

def show_menu():
    menu_list = ["1. 학생 정보 추가", "2. 전체 성적 출력", "3. 성적 검색", "4. 성적 수정", "5. 성적 삭제", "6. 종료"]
    for menu in menu_list:
        print(menu)
    while True:
        try:
            select = int(input("선택 : "))
        except:
            print("잘못된 입력입니다.")
            continue

        if not select in [1, 2, 3, 4, 5, 6]:
            print("1~6 사이를 입력하여 주십시오.")
            continue

        return select


def insert_info(students_info):
    while True:
        name = input("학생 이름 : ")
        s_num = input("학번 : ")
        for student in students_info:
            if student.s_num == s_num:
                print("이미 등록된 학생입니다.")
                return False
        sub = input("과목 : ")
        try:
            score = int(input("점수 : "))
        except ValueError:
            print("잘못된 입력입니다.")
            return False
        students_info.append(Student.Student(name, s_num, sub, score))
        return True


def show_info(students_info):
    for student in students_info:
        print(f"이름 : {student.name}, 학번 : {student.s_num}, 과목 : {student.sub}, 성적 : {student.score}")


def search_info(students_info):
    if not students_info:
        print("학생 정보가 아무것도 없습니다.")
        return False
    else:
        select = input("검색할 학번 : ")
        for student in students_info:
            if student.s_num == select:
                print(f"{student.name}, {student.sub}, {student.score}")
                break
            else:
                print("검색한 학번이 없습니다.")
                return False


def modify_info(students_info):
    if not students_info:
        print("학생 정보가 아무것도 없습니다.")
        return False
    else:
        select = input("검색할 학번 : ")
        for student in students_info:
            if student.s_num == select:
                print("학번에 해당하는 학생을 찾았습니다.")
                while True:
                    try:
                        select2 = int(input("수정할 데이터 선택 [1. 과목 2. 성적] : "))
                    except:
                        print("잘못된 입력입니다.")
                        continue
                    if select2 == 1:
                        student.sub = input("과목 : ")
                        break
                    elif select2 == 2:
                        student.score = int(input("성적 : "))
                        break
                    break
            else:
                print("검색한 학번이 존재하지 않습니다.")
                return False
    return True


def delete_info(students_info):
    select = input("삭제할 학번 : ")
    for student in students_info:
        if student.s_num == select:
            info = student
            break
        else:
            print("검색한 학번이 존재하지 않습니다.")
            return False
    students_info.remove(info)
    print("해당 학번의 학생 데이터를 삭제했습니다.")
    return True


if __name__ == "__main__":
    students_info = []
    path = "c:\\202444091\\students_info"
    file = "student_info.txt"
    fullfile = os.path.join(path, file)

    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        if os.path.isfile(fullfile):
            print("기존 데이터를 복원합니다.")
            with open(fullfile, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    split_datas = line.strip().split("|")
                    students_info.append(Student.Student(split_datas[0], split_datas[1], split_datas[2], int(split_datas[3])))
    
    while True:
        select = show_menu()

        if select == 1:
            result = insert_info(students_info)
            if result == False:
                continue
        elif select == 2:
            result = show_info(students_info)
            if result == False:
                continue
        elif select == 3:
            result = search_info(students_info)
            if result == False:
                continue
        elif select == 4:
            result = modify_info(students_info)
            if result == False:
                continue
        elif select == 5:
            result = delete_info(students_info)
            if result == False:
                continue
        elif select == 6:
            print("현재까지의 데이터를 저장합니다.")
            with open(fullfile, 'w') as f:
                for info in students_info:
                    f.write(f"{info.name}|{info.s_num}|{info.sub}|{info.score}\n")
            print("프로그램을 종료합니다.")
            break
            

    
