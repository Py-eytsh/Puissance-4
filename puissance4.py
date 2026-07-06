# Créé par pierre-henri, le 09/01/2026 en Python 3.7
## PUISSANCE4
import numpy as np
import copy
import random as rd
import time


inf=float("inf")
w=[0,1,10,30,inf]
grille=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,0,0],[1,2,0,2,2,0,0]]

def affiche(grille):
    d={0:". ",1:"x ",2:"o "}
    for ligne in grille:
        c=''
        for p in ligne:
            c=c+d[p]
        print(c)
    print("0 1 2 3 4 5 6")

def test_game():
    affiche(grille)

    return minimax(grille,1,2)
'''
def tourDuJoueur(grille,forme):
    valid=False
    while valid=False
        position=int(input())
        if position<len(grille) and position>=0:

'''


def coup_colonne(grille,j):
    for i in range (len(grille)-1,-1,-1):
        if grille[i][j]==0:
            return (i)
    return None

def coups(grille):
    positions=[]
    for j in range (len(grille[0])):
        i=coup_colonne(grille,j)
        if i!=None:
            positions.append([i,j])
    return positions

def alignement():
    L=[]
    for j in range (7):
        for i in range(3):
            L.append([(i,j),(i+1,j),(i+2,j),(i+3,j)])
    for j in range (4):
        for i in range(6):
            L.append([(i,j),(i,j+1),(i,j+2),(i,j+3)])
    for j in range (4):
        for i in range(3):
            L.append([(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)])
    for j in range (4):
        for i in range(3,6):
            L.append([(i,j),(i-1,j+1),(i-2,j+2),(i-3,j+3)])
    return L
tous=alignement()
def n(k,A,G):
    nk=0
    for coor in A:
        if G[coor[0]][coor[1]]==k:
            nk+=1
    return nk


def evaluation(grille,w):
  ## A retirer pour mettre dans le programme principal
    score1=0
    for ali in tous:
        if n(2,ali,grille)==0:
            score1+=w[n(1,ali,grille)]
        if n(1,ali,grille)==0:
            score1-=w[n(2,ali,grille)]
    return (score1)

def gagnant(G):
 ## A retirer pour mettre dans le programme principal
    for ali in tous:
        if n(2,ali,G)==4:
            return 2
        if n(1,ali,G)==4:
            return 1
    return 0

def minimax(G,k,p):
    if gagnant(G)==1:
        return inf,None
    elif gagnant(G)==2:
        return -inf, None
    elif p==0:
        return evaluation(G,w),None
    else:
        if k==1:
            maximum,coup=-inf,None
            if not (coups(G)==[]):
                for c in coups(G):
                    H=copy.deepcopy(G)
                    H[c[0]][c[1]]=1
                    valeur, _ = evaluation(H,w),minimax(H,2,p-1)
                    if valeur>maximum:
                        maximum,coup=valeur,c
                return maximum,coup
        if k==2:
            minimum,coup=inf,None
            if not (coups(G)==[]):
                for c in coups(G):
                    H=copy.deepcopy(G)
                    H[c[0]][c[1]]=2
                    valeur, _ = evaluation(H,w),minimax(H,1,p-1)
                    if valeur<minimum:
                        minimum,coup=valeur,c
                return minimum,coup


def new_game(p):
    G = [[0]*7 for i in range(6)]
    for t in range(21): #a verif
        affiche(G)
        time.sleep(0.5)
        if gagnant(G)==0:
            coup=None
            while coup ==None:
                j=int(input('ChoisiC une Colonne'))
                coup=coup_colonne(G,j)
            G[coup][j]=1
        if gagnant(G)==0:
            valeur,coup=minimax(G,2,p)
            if valeur==inf:
                coup=rd.choice(coups(G))
            G[coup[0]][coup[1]]=2
        if gagnant(G)>0:
            break
    affiche(G)
    if gagnant(G)==1:
        print('VOUS AVEZ GAGNé!!!')
    elif gagnant(G) == 2:
        print('L\'IA vas vous remplacer... ')
    else:
        print('¯\_(ツ)_/¯')
















