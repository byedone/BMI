print ('輸入身高cm')
high = float(input())
print ('輸入體重kg')
weight = float(input())
BMI = weight/((high/100)**2)
if BMI < 18.5:
	print("BMI為",round(BMI,2),"體重過輕")
elif 18.5 <= BMI<24:
	print("BMI為",round(BMI,2),"正常範圍")
elif 24 <= BMI<27:
	print("BMI為",round(BMI,2),"過重")
elif 27 <= BMI<30:
	print("BMI為",round(BMI,2),"輕度肥胖")
elif 30 <= BMI<35:
	print("BMI為",round(BMI,2),"中度肥胖")
elif BMI >= 35:
	print("BMI為",round(BMI,2),"重度肥胖")