#密碼重試程式

pwd = "a12345678"
i = 3
while i > 0:
	user_pw = input('請輸入密碼: ')
	if pwd == user_pw:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤，還有',i,'次')
print('程式關閉')