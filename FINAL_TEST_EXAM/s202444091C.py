import member
import os

mlt = []

def show_menu():
    menus = ["A. 기존자료복원", "B. 회원등록", "C. 정보수정", "D. 전체조회", "Q. 종료 및 회원정보 저장"]
    while True:
        print("#" * 40)
        for menu in menus:
            print(menu)
        print("#" * 40)

        select = input()
        if select not in ['A', 'B', 'C', 'D', 'Q', 'a', 'b', 'c', 'd', 'q']:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue
        return select.upper()
    

def add_member():
    while True:
        print("[회원 정보 등록]")
        id = input("아이디 : ")
        for m in mlt:
            if m.id == id:
                print("등록된 아이디가 있습니다.")
                return False
        gender = input("성별 (M남자 W여자) : ").upper()
        if gender not in ['M', 'W']:
            print("성별이 잘못 입력되었습니다.")
            return False
        try:
            height = float(input("신장(m) : "))
        except:
            print("신장이 잘못 입력되었습니다.")
            return False
        try:
            weight = int(input("체중(kg) : "))
        except:
            print("체중이 잘못 입력되었습니다.")
            return False
        new_member = member.Member(id, gender, height, weight)
        print(f"입력한 정보를 바탕으로 계산한 BMI 수치 : {new_member.calc_BMI():.2f}")
        return new_member
    

def modify():
    if mlt:
        search_id = input("아이디 : ")
        for m in mlt:
            if search_id == m.id:
                print("아이디 :", m.id)
                print("현재 신장 :", m.height)
                try:
                    m.height = float(input("수정 신장 : "))
                except:
                    print("신장이 잘못 입력되었습니다.")
                    return False
                print("현재 체중 :", m.weight)
                try:
                    m.weight = int(input("수정 체중 : "))
                except:
                    print("체중이 잘못 입력되었습니다.")
                    return False
                print("입력한 정보를 바탕으로 계산한 BMI 수치", m.calc_BMI())
            else:
                print("회원 정보가 없습니다.")
    else:
        print("등록된 회원정보가 없습니다.")


def show_members():
    if mlt:
        i = 1
        m_data = []
        m_chart = []
        w_data = []
        w_chart = []
        for m in mlt:
            if m.gender == 'M':
                m_data.append(f"[{i}] 아이디 : {m.id} 신장 : {m.height} 체중 : {m.weight} BMI : {m.calc_BMI():.2f}")
                m_chart.append(int(m.calc_BMI()))
            else:
                w_data.append(f"[{i}] 아이디 : {m.id} 신장 : {m.height} 체중 : {m.weight} BMI : {m.calc_BMI():.2f}")
                w_chart.append(int(m.calc_BMI()))
        print("[전체 상태 조회]")
        print("=" * 40)

        print("[남성]")
        for i in range(len(m_data)):
            print(f"[{i+1}] {m_data[i]}")
            print("도표 :", "*" * m_chart[i])
            print()

        print("[여성]")
        for i in range(len(w_data)):
            print(f"[{i+1}] {w_data[i]}")
            print("도표 :", "*" * w_chart[i])
            print()
        
        print("=" * 40)
        print(f"총 {len(mlt)}명의 정보입니다.")

    else:
        print("상태를 보여줄 회원이 없습니다.")


def check_dir():
    mypath = "c:\\202444091"
    myfile = "bmilist.txt"
    fullfile = os.path.join(mypath, myfile)

    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    
    return fullfile


def store_data(fullfile):
    if mlt:
        with open(fullfile, 'w') as f:
            for m in mlt:
                f.write(m.gen_file_record())
            print(f"{len(mlt)}건의 데이터를 저장했습니다.")
    else:
        print("저장할 자료가 없습니다.")


def load_data(fullfile):
    if not os.path.isfile(fullfile):
        print("복원할 데이터가 없습니다.")
        return False
    if mlt:
        print("기존 자료와의 충돌이 발생할 수 있으므로 복원할 수 없습니다.")
        return False
    else:
        with open(fullfile, 'r') as f:
            for datas in f:
                split_datas = datas.strip().split("|")
                mlt.append(member.Member(split_datas[0].split(), split_datas[1].split(), split_datas[2].split(), split_datas[3].split()))


if __name__ == "__main__":
    while True:
        sel = show_menu()

        if sel == 'A':
            fullfile = check_dir()
            load_data(fullfile)
            continue
        elif sel == 'B':
            result = add_member()
            if result == False:
                continue
            else:
                mlt.append(result)
        elif sel == 'C':
            modify()
            continue
        elif sel == 'D':
            show_members()
            continue
        elif sel == 'Q':
            fullfile = check_dir()
            store_data(fullfile)
            break
print("프로그램을 종료합니다.")
