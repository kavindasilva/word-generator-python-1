### Testing Pull
listt = ["zabaglione","zabrawood","zaccab","zaffer","zalambdodont","zany","zap","zealot","zealous","zebra","zebu","zed","zee","zeitgeist","zel","zemindar","zenithal","zeolite","zephyr","zeppelin","zeroised","zeroth","zest","zeta","zeugen","zeus","ziggurat","zig","zag","zig","zagger","zillion","zincate","zincite","zincography","zingiberis","zinnia","zion","zipper","zirconium","zither","zloty","zoantharian","zodiacal","zoeaform","zoic","zollverein","zombie","zonal","zonation","zonda","zoned","zoning","zoocecidium","zoochlorella","zoochory","zooecium","zoogamete","zoogonidangium","zoogonous","zoogony","zooid","zoolatry","zoological","zoologist","zoology","zoomastigophora","zooming","zoomorphosis","zooophobia","zoophilic","zoophilous","zoophily","zoophobia","zoophyte","zooplankton","zoosporangiophore","zoosporangium","zoospore","zucchini","zulu","zwitterion","zygantrum","zygapophysis","zygography","zygomatic","zygomorphic","zygonema","zygosphene","zygospore","zygotene","zymase","zymochemistry","zymogen","zymosis"]
z2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
prob=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

i=1
def fun():
	length = len(listt)
	a=0

	while a<length:
		if listt[a][1]=="a":
			z2[0]=z2[0]+1
		
		elif listt[a][1]=="b":
			z2[1]=z2[1]+1
			
		elif listt[a][1]=="c":
			z2[2]=z2[2]+1
			
		elif listt[a][1]=="d":
			z2[3]=z2[3]+1
			
		elif listt[a][1]=="e":
			z2[4]=z2[4]+1

		elif listt[a][1]=="f":
			z2[5]=z2[5]+1
			
		elif listt[a][1]=="g":
			z2[6]=z2[6]+1
			
		elif listt[a][1]=="h":
			z2[7]=z2[7]+1
			
		elif listt[a][1]=="i":
			z2[8]=z2[8]+1			
			
		elif listt[a][1]=="j":
			z2[9]=z2[9]+1
			
		elif listt[a][1]=="k":
			z2[10]=z2[10]+1
			
		elif listt[a][1]=="l":
			z2[11]=z2[11]+1
			
		elif listt[a][1]=="m":
			z2[12]=z2[12]+1
			
		elif listt[a][1]=="n":
			z2[13]=z2[13]+1
			
		elif listt[a][1]=="o":
			z2[14]=z2[14]+1
			
		elif listt[a][1]=="p":
			z2[15]=z2[15]+1
			
		elif listt[a][1]=="q":
			z2[16]=z2[16]+1
			
		elif listt[a][1]=="r":
			z2[17]=z2[17]+1
			
		elif listt[a][1]=="s":
			z2[18]=z2[18]+1
			
		elif listt[a][1]=="t":
			z2[19]=z2[19]+1
			
		elif listt[a][1]=="u":
			z2[20]=z2[20]+1
			
		elif listt[a][1]=="v":
			z2[21]=z2[21]+1
			
		elif listt[a][1]=="w":
			z2[22]=z2[22]+1
			
		elif listt[a][1]=="x":
			z2[23]=z2[23]+1
			
		elif listt[a][1]=="y":
			z2[24]=z2[24]+1
			
		elif listt[a][1]=="z":
			z2[2]=z2[2]+1
			
		a=a+1

		
def probab():
	i=0
	while (i<26):
		prob[i]=z2[i]*1.0/len(listt)
		print (prob[i])
		i+=1
		
fun()
#print (count)
probab()
