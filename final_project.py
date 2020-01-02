#encoding:utf-8
def project():
	
	import os,sys
	import jieba,codecs,math
	import jieba.posseg as pseg
	ns={}  #姓名字典]
	rs={} #关系字典
	lineNs=[]  #每段人物关系
	#设置字典,加载
	jieba.load_userdict('D:\大计基\dict.txt')
	with codecs.open("D:\大计基\黎明破晓的街道.txt",'r','gbk') as f:
	    for line in f.readlines():
	        poss=pseg.cut(line)  #分
	        lineNs.append([])
	        for w in poss:   #nr词频，
	            if  w.flag!="nr" or len(w.word) <2:
	                continue
	            lineNs[-1].append(w.word)
	            if ns.get(w.word) is None:
	                ns[w.word]=0
	                rs[w.word]={}
	            ns[w.word]+=1
	    for n,times in ns.items():
	        print (n,times)
	#根据识别结果构架网络
	for line in lineNs:  #对于每一段
	   for n1 in line:
	      for n2 in line: #每一段中两个任意人
	          if n1==n2:
	              continue
	          if rs[n1].get(n2) is None:
	            rs[n1][n2]=1
	          else:
	            rs[n1][n2]+=1
	#过滤冗余的边并输出结果，将已经建立好的ns和rs输出到文本，，输出
	#节点集合保存在busan_node.txt
	#边集合保存在busan_edge.node
	with codecs.open("People_node.csv", "w", "utf8") as f:
	    f.write("ID Label Weight\r\n")
	    for n, times in ns.items():
	        if times > 10:
	            f.write(n + " " + n + " " + str(times) + "\r\n")



	with codecs.open("People_edge.csv", "w", "utf8") as f:
	    f.write("Source Target Weight\r\n")
	    for n, edges in rs.items():
	        for v, w in edges.items():
	            if w > 10:
	                f.write(n + " " + v + " " + str(w) + "\r\n")


project()
