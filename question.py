import random
import os
import time

def question():
    H = "수소"
    He = "헬륨"
    Li = "리튬"
    Be = "베릴륨"
    B = "붕소"
    C = "탄소"
    N = "질소"
    O = "산소"
    F = "플루오린"
    Ne = "네온"
    Na = "나트륨"
    Mg = "마그네슘"
    Al = "알루미늄"
    Si = "규소"
    P = "인"
    S = "황"
    Cl = "염소"
    Ar = "아르곤"
    K = "칼륨"
    Ca = "칼슘"
    print("문제 모드입니다.")
    print("아직 베타 버전으로 문제를 많이 만들진 않았습니다.")
    print("원자 기호들이 나올텐데 한글로 이름을 써서 문제를 맞추시면 됩니다.")
    h = input("H\n")
    if(h == H):
        print("정답입니다.\n")
    if(h != H):
        print("오답입니다.\n")
    he = input("He\n")
    if (he == He):
        print("정답입니다.\n")
    if (he != He):
        print("오답입니다.\n")
    li = input("Li\n")
    if (li == Li):
        print("정답입니다.\n")
    if (li != Li):
        print("오답입니다.\n")
    be = input("Be\n")
    if (be == Be):
        print("정답입니다.\n")
    if (be != Be):
        print("오답입니다.\n")
    b = input("B\n")
    if (B == b):
        print("정답입니다.\n")
    if (B != b):
        print("오답입니다.\n")
    c = input("C\n")
    if (c == C):
        print("정답입니다.\n")
    if (c != C):
        print("오답입니다.\n")
    n = input("N\n")
    if (n == N):
        print("정답입니다.\n")
    if (n != N):
        print("오답입니다.\n")
    o = input("O\n")
    if (o == O):
        print("정답입니다.\n")
    if (o != O):
        print("오답입니다.\n")
    f = input("F\n")
    if (f == F):
        print("정답입니다.\n")
    if (o != O):
        print("오답입니다.\n")
    ne = input("Ne\n")
    if (ne == Ne):
        print("정답입니다.\n")
    if (ne != Ne):
        print("오답입니다.\n")
    na = input("Na\n")
    if (na == Na):
        print("정답입니다.\n")
    if (na != Na):
        print("오답입니다.\n")
    mg = input("Mg\n")
    if (mg == Mg):
        print("정답입니다.\n")
    if (mg != Mg):
        print("오답입니다.\n")
    al = input("Al\n")
    if (al == Al):
        print("정답입니다.\n")
    if (al != Al):
        print("오답입니다.\n")
    si = input("Si\n")
    if (si == Si):
        print("정답입니다.\n")
    if (si != Si):
        print("오답입니다.\n")
    p = input("P\n")
    if (p == P):
        print("정답입니다.\n")
    if (p != P):
        print("오답입니다.\n")
    s = input("S\n")
    if (s == S):
        print("정답입니다.\n")
    if (s != S):
        print("오답입니다.\n")
    cl = input("Cl\n")
    if (cl == Cl):
        print("정답입니다.\n")
    if (cl != Cl):
        print("오답입니다.\n")
    ar = input("Ar\n")
    if (ar == Ar):
        print("정답입니다.\n")
    if (ar != Ar):
        print("오답입니다.\n")
    k = input("K\n")
    if (k == K):
        print("정답입니다.\n")
    if (cl != Cl):
        print("오답입니다.\n")
    ca = input("Ca\n")
    if (ca == Ca):
        print("정답입니다.\n")
    if (ca != Ca):
        print("오답입니다.\n")
    print("문제 출제를 완료하였습니다.\n")
    print("답안:")
    print("H - 수소")
    time.sleep(0.1)
    print("He - 헬륨")
    time.sleep(0.1)
    print("Li - 리튬")
    time.sleep(0.1)
    print("Be - 베릴륨")
    time.sleep(0.1)
    print("B - 붕소")
    time.sleep(0.1)
    print("C - 탄소")
    time.sleep(0.1)
    print("N - 질소")
    time.sleep(0.1)
    print("O - 산소")
    time.sleep(0.1)
    print("F - 플루오린")
    time.sleep(0.1)
    print("Ne - 네온")
    time.sleep(0.1)
    print("Na - 나트륨")
    time.sleep(0.1)
    print("Mg - 마그네슘")
    time.sleep(0.1)
    print("Al - 알루미늄")
    time.sleep(0.1)
    print("Si - 규소")
    time.sleep(0.1)
    print("P - 인")
    time.sleep(0.1)
    print("S - 황")
    time.sleep(0.1)
    print("Cl - 염소")
    time.sleep(0.1)
    print("Ar - 아르곤")
    time.sleep(0.1)
    print("K - 칼륨")
    time.sleep(0.1)
    print("Ca - 칼슘")
    time.sleep(0.1)
    if(h == H and he == He and li == Li and be == Be and b == B and c == C and n == N
            and o == O and f == F and ne == Ne and na == Na and mg == Mg and al == Al
            and si == Si and P == p and s == S and cl == Cl and Ar == ar and K == k and ca == Ca):
        print("모든 문제를 맞추셨습니다!!\n")