# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:36:56 2019

@author: PC
"""
jsonname="activator_rail_raised.json"
linegap1="\n\t "
linegap2="\n\t\t"
linegap3=linegap2+"\t"
linegap4=linegap3+"\t"
content="{"+linegap1+'"textures": {'+linegap2+'"particle": "block/wood",'+linegap2+'"wood": "block/wood",'+linegap2+'"metal": "block/metal",'+linegap2+'"rd_off": "block/redstone_off",'+linegap2+'"gold": "block/gold"'+linegap1+"},"+linegap1+'"elements": ['


endoftext=linegap2+"}"+linegap1+"]"+"\n}"
def createjson(jsname):
    
    file_write= open(jsname,"w")
    file_write.write(content)
    file_write.close()

def endjson(jsname):
    file_add=open(jsname,"a")
    file_add.write(endoftext)
    file_add.close()

def notcoordinate(arg,tp):
    if len(arg)!=3:
        tp=0
        return True
    for i in range(2):
        if type(arg[i]) is not int:
            tp+=1
            return True
        if (arg[i]>16 or arg[i]<0):
            tp+=1
            return True
    return False


def newstr(tup):
    st=str(tup)
    st=st.replace("(","[")
    return st.replace(")","]")

def addlist(lis1,lis2):
    n=len(lis1)
    lis3=[]
    for i in range(n):
        lis3.append(lis1[i]+lis2[i])
    return lis3


def addelements(material,start,ecart,jsname,empty_face):
    print(empty_face)
    typeproblem=0
    problemsent=""
    
    if material not in ["wood","metal","rd_off","gold"]:
        raise TypeError("need material in texture block")
    if (type(start) is not list or type(ecart) is not list):
        raise TypeError("no list to describe 3 dimension coordinate")
    if (notcoordinate(start,typeproblem) or notcoordinate(ecart,typeproblem)):
        if typeproblem ==0 :
            problemsent="no 3d tuple"
        if typeproblem ==1 :
            problemsent="no int value for coordinate"
        if typeproblem ==2 :
            problemsent="exists coordinate that are not in the cube"
        raise ValueError("probleme in tuple specification:"+problemsent)
    stop=addlist(start,ecart)
    if not(empty_face):
        adding = linegap2+"},"
    else :
        adding = ""
    adding+= linegap2+"{"
    adding+= linegap3+'"from":'+newstr(start)+","
    adding+= linegap3+'"to":'+newstr(stop)+","
    adding+= linegap3+'"faces":'
    adding+= linegap3+"{"
    face=['"north"','"south"','"east"','"west"','"up"','"down"']
    for i in range(6):
        substarttuple = ()
        if i<2 :
            substarttuple = start[:2]+stop[:2]
        elif i<4 :
            substarttuple = start[1:]+stop[1:]
        elif i<6 :
            substarttuple = (start[:1]+start[2:]+stop[:1]+stop[2:])
            
        lines=linegap4+face[i]+ ':{"uv": '+str(substarttuple)+","
        lines+= linegap4+'"texture": "#'+material+'"'
        if i!=5:
            lines+=linegap4+"},"
        else:
            lines+=linegap4+"}"
            lines+=linegap3+"}"
        adding += lines
    file_add=open(jsname,"a")
    file_add.write(adding)
        

#rail courbe
'''
#creation du debut du fichier
createjson(jsonname)

#ajout des partie

#voie peu courbé
addelements("metal",[0,1,3],[4,2,1],jsonname,True)
empty_face = False
addelements("metal",[4,1,4],[2,2,1],jsonname,empty_face)
addelements("metal",[6,1,5],[2,2,1],jsonname,empty_face)
addelements("metal",[8,1,6],[1,2,1],jsonname,empty_face)
addelements("metal",[9,1,7],[1,2,1],jsonname,empty_face)
addelements("metal",[10,1,8],[1,2,2],jsonname,empty_face)
addelements("metal",[11,1,10],[1,2,2],jsonname,empty_face)
addelements("metal",[12,1,12],[1,2,4],jsonname,empty_face)

#voie très courbe
addelements("metal",[0,1,12],[2,2,2],jsonname,empty_face)
addelements("metal",[2,1,14],[2,2,2],jsonname,empty_face)
addelements("metal",[2,1,13],[1,2,1],jsonname,empty_face)

#traverse du bas 
addelements("wood",[3,0,1],[2,2,3],jsonname,empty_face)
addelements("wood",[2,0,4],[2,2,3],jsonname,empty_face)
addelements("wood",[1,0,7],[2,2,3],jsonname,empty_face)
addelements("wood",[0,0,10],[2,2,5],jsonname,empty_face)

#traverse du haut 
addelements("wood",[12,0,11],[3,2,2],jsonname,empty_face)
addelements("wood",[9,0,12],[3,2,2],jsonname,empty_face)
addelements("wood",[6,0,13],[3,2,2],jsonname,empty_face)
addelements("wood",[1,0,14],[5,2,2],jsonname,empty_face)


#traverse en diagonale
for i in range(5,13):
    addelements("wood",[14-i,0,i],[2,2,2],jsonname,empty_face)
    


#ajoute les parties finale du json
endjson(jsonname)
'''

#rail elevee

#creation du debut du fichier
createjson(jsonname)


addelements("metal",[0,1,3],[1,2,1],jsonname,True)
empty_face = False
for i in range(16):
    addelements("metal",[i,i+1,3],[1,2,1],jsonname,empty_face)
    addelements("metal",[i,i+1,12],[1,2,1],jsonname,empty_face)



for i in range(4):
    #premier niveau
    addelements("wood",[4*i+1,4*i+1,1],[1,2,3],jsonname,empty_face)
    addelements("rd_off",[4*i+1,4*i+1,4],[1,2,2],jsonname,empty_face)
    
    addelements("wood",[4*i+1,4*i+1,6],[1,2,4],jsonname,empty_face)
    addelements("rd_off",[4*i+1,4*i+1,10],[1,2,2],jsonname,empty_face)
    
    addelements("wood",[4*i+1,4*i+1,12],[1,2,3],jsonname,empty_face)
    
    #deuxieme niveau
    addelements("wood",[4*i+2,4*i+2,1],[1,2,3],jsonname,empty_face)
    addelements("rd_off",[4*i+2,4*i+2,4],[1,2,2],jsonname,empty_face)
    
    addelements("wood",[4*i+2,4*i+2,6],[1,2,4],jsonname,empty_face)
    addelements("rd_off",[4*i+2,4*i+2,10],[1,2,2],jsonname,empty_face)
    
    addelements("wood",[4*i+2,4*i+2,12],[1,2,3],jsonname,empty_face)
    
    #troisieme niveau et quatrieme niveau (pour les trois premier i)
    if i!=3:
        addelements("rd_off",[4*i+3,4*i+3,7],[2,2,2],jsonname,empty_face)
        addelements("rd_off",[4*i+4,4*i+4,7],[2,2,2],jsonname,empty_face)
    
    





#ajoute les parties finale du json
endjson(jsonname)

    