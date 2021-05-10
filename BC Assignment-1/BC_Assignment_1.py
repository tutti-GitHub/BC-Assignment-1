print();

radius = input("地球の半径を入力してください(km):");
air_thickness = input("空気の厚さを入力してください(km):");
vital_capacity = input("肺の体積を入力してください(L):");
molecules = 2*(10**22); #1Lの空気の分子数

volume = 3.14 * 4 / 3 * ( ( int(air_thickness) + int(radius) )**3 - int(radius)**3 ) ; #km**3

answer = int(molecules) * 22.4 / int(volume) * (int(vital_capacity) * 1000 / (10**15)); # 22.4Lの時の分子数/体積(km**3)×肺の体積(L→km**3)


print();
print("答えは" , end="");
print(round(answer, 1) , end="");
print("個です。(小数点第二位で四捨五入済み)")
print();

print("小数点第二位以降も含めた答えは" + str(answer) + "個です。");
print();

print("計算式:")
print("(空気が拡散する体積) = 3.14 * 4 / 3 * < {(空気の厚さ) + (地球の半径 )}^3 - (地球の半径)^3 >");
print("(答え) = (1Lの空気の分子数) * 22.4 / (空気が拡散する体積) * {(肺の体積) * 1000 / 10^15}");
print();
input("何かキーを押すと終了します。")

#forとifを使って、10以下になるまで10で割りnに1加算
