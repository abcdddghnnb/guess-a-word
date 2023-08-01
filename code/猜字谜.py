import random as ra
import os
import time as ti
a=['山上还有山','十张口，一颗心','说它小，下边大，说它大，上边小',
   '一只黑狗，不叫不吼','差一点六斤','家中添一口','自小在一起，目前少联系',
   '点点成金','一人一张口，下面长只手','四面都是山,山山都相连','种花要除草,一人来一刀',
   '存心不让出大门,你说烦人不烦人','一只狗，两个口，谁遇它谁发愁',
   '格外大方','七十二小时','需要一半,留下一半','综合门市','守门员',
   '半青半紫','一口吃掉牛尾巴','一大二小','一月七日','人不在其位',
   '刀出鞘','十二点','十个哥哥','上下难分','文武两全','水上工程',
   '半个月亮','打断念头','多一半','春风吹又生','王先生在石头上',
   '挥手告别','推开又来','半字写下','此字只一个，二字边下躲','曰字加竖不加点',
   '一口分两家','二口在下下','三口叠罗汉']
b=['出','思','尖','默','兵','豪','省','全','拿','田','化',
   '闷','哭','回','晶','雷','闹','闪','素','告','奈','脂',
   '立','力','斗','克','卡','斌','汞','胖','心','夕','薪',
   '碧','军','摊','干','些','神','日','吕','品']
print("初始化中......|-|-|-|-")
cml=os.listdir("c:/")
if not ("猜字谜" in cml):
	os.mkdir("c:/猜字谜")
fill=open('c:/猜字谜/scrores.txt','a+',encoding='utf-8')
clist=os.listdir("C:/猜字谜")
if ("答案.txt" in clist) and ("题目.txt" in clist):
	nd=open('c:/猜字谜/答案.txt','a+',encoding='utf-8')
	nt=open('c:/猜字谜/题目.txt','a+',encoding='utf-8')
	nd.seek(0)
	nt.seek(0)
	nt1=nt.read()
	nt=nt1.split("-")
	nd1=nd.read()
	nd=nd1.split("-")
	if nt[len(nt)-1]=="":
		nt.pop(len(nt)-1)
	if nd[len(nd)-1]=="":
		nd.pop(len(nd)-1)
	for i in range(len(nd)):
		a.append(nt[i])
		b.append(nd[i])
d=len(a)
print("初始化完成")
print("猜字谜Build:1.7,库存量:"+str(d))
s=input("你要直接玩还是先加入自己的字谜？1为直接玩，2为自己单次加字谜，3为自己历史性添加字谜:")
if s!="1" and s!="2" and s!="3":
	print("请输入1,2,3中的一个选项!!!")
	ti.sleep(2)
	fill.close()
	os._exit(1)
elif s=="2":
	z=0
	while z!="5":
		while True:
			z=input("输5退出，或输入字谜：")
			if z=="":
				print("字谜不能为空，请重新输入")
			else:				
				if z!="5":
					while True:
						x=input("答案:")
						if x=="":
							print("答案不能为空，请重新输入")
						else:
							a.append(z)
							b.append(x)
							d=d+1
							print("现有库存:"+str(d))
							break						
				else:
					print("现有库存:"+str(d))
					print("退出中......")
					os.system("cls")
					break
elif s=="3":
	print("手动录入方法：请打开系统盘下的猜字谜文件\n夹后将字谜保存在“题目.txt”，用\n“-”分隔，以相同顺序与方法在同一目录创建\n“答案.txt”写入答案，分隔符一样，请按你输\n字谜的顺序输答案。")
	print("自动输入中！")
	nd=open('c:/猜字谜/答案.txt','a+',encoding='utf-8')
	nt=open('c:/猜字谜/题目.txt','a+',encoding='utf-8')
	z=0
	while z!="5":
		while True:
			z=input("输5退出，或输入字谜：")
			if z=="":
				print("字谜不能为空，请重新输入")
			else:				
				if z!="5":
					while True:
						x=input("答案:")
						if x=="":
							print("答案不能为空，请重新输入")
						else:
							nt.write(z+"-")
							nd.write(x+"-")
							break						
				else:
					print("退出中......")
					break
	nt.close()
	nd.close()
	ti.sleep(5)
	fill.close()
	os._exit(1)
while True:
	c=int(input("你要猜几个?"))
	if c>d:
		print("请少猜一点")
	else:
		break
g=0
h=0
for i in range(c):
	e=ra.randint(0,d-1)
	while True:
		f=input("字谜："+a[e]+"你猜谜底是什么?")
		if f=="":
			print("答案不能为空，请重新输入")
		else:
			break
	if f==b[e]:
		print("你答对了！")
		a.pop(e)
		b.pop(e)
		g+=1
		d-=1
	else:
		print("你答错了！答案是："+b[e])
		a.pop(e)
		b.pop(e)
		h+=1
		d-=1
print("总共：{}个,对了{}个,错了{}个".format(c,g,h))
n=fill.tell()
fill.seek(0)
res = len(fill.readlines())+1
fill.seek(n)
fill.write("第{}次		".format(res)+"总共{}个		对了{}个	".format(c,g)+"	错了{}个".format(h)+"\n")
fill.seek(0)
print(fill.read())
input("按Enter退出")
fill.close()