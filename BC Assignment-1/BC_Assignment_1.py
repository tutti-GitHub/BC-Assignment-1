print("(問題)");
print(" いま割った風船の中の 22.4 Lの空気が、地球の大気全体に拡散したと仮定する。");
print(" このとき、我々一人一人の肺の中に、風船の中にあった空気の分子は何個含まれているか？");

print("(条件)");
print(" ・空気は地球全体に均一に広がる");
print(" ・光合成などで変換されない");
print();

radius = input("地球の半径を入力してください(km){実際の地球は約6000km}:");
air_thickness = input("空気の厚さを入力してください(km){実際の地球は約15km}:");
vital_capacity = input("肺の体積を入力してください(L):");
significant_digits = input("有効数字を入力してください:");

#変数定義
n = 0;
x = int(significant_digits) -1; #有効数字をroundで使えるように

molecules = 2*(10**22); #1Lの空気の分子数

volume = 3.14 * 4 / 3 * ( ( float(air_thickness) + float(radius) )**3 - float(radius)**3 ) ; #km**3

answer = float(molecules) * 22.4 / float(volume) * (float(vital_capacity) * 1000 / (10**15)); # 22.4Lの時の分子数/体積(km**3)×肺の体積(L→km**3)

while answer > 10:

    answer = (answer / 10) ;
    n +=1;

while answer < 1:

    answer = (answer * 10);
    n -=1;

print();
print();
print("答えは" , end="");
print(round(answer, x ) , end=""); #x
print("×10^" + str(n), end="");
print("(個)です。")
print();
print();

print("計算式:")
print("(空気が拡散する体積) = 3.14 * 4 / 3 * < {(空気の厚さ) + (地球の半径 )}^3 - (地球の半径)^3 >");
print("(答え) = (1Lの空気の分子数) * 22.4 / (空気が拡散する体積) * {(肺の体積) * 1000 / 10^15}");
print();
input("何かキーを押すと終了します。")
