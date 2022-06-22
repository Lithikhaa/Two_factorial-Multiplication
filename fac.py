import numpy as np

def main():
   R = int(input("Enter the number of rows:")) 
   C = int(input("Enter the number of columns:")) 

   print("Enter the entries in a single line (separated by space): ") 
   entries = list(map(float, input().split())) 

   matrix = np.array(entries).reshape(R, C)
   m = matrix-matrix[0][0]
   print("\t\t\t---------- Enterded data-----------\n",matrix)

   print(f"\t\t\t--We code the data by subtracting {matrix[0][0]} from each value--\n",m)
   #ROW TOTAL:
   RT1 = m[0][0]+m[0][1]+m[0][2]+m[0][3]
   RT_1= round(RT1,1)
   RTa = m[1][0]+m[1][1]+m[1][2]+m[1][3]
   RT_a= round(RTa,1)
   RTb = m[2][0]+m[2][1]+m[2][2]+m[2][3]
   RT_b = round(RTb,1)
   RTab = m[3][0]+m[3][1]+m[3][2]+m[3][3]
   RT_ab = round(RTab,1)

   #COLUMN TOTAL:
   C1 = m[0][0]+m[1][0]+m[2][0]+m[3][0]
   C_1= round(C1,1)
   C2 = m[0][1]+m[1][1]+m[2][1]+m[3][1]
   C_2= round(C2,1)
   C3 = m[0][2]+m[1][2]+m[2][2]+m[3][2]
   C_3 = round(C3,1)
   C4 = m[0][3]+m[1][3]+m[2][3]+m[3][3]
   C_4 = round(C4,1)

   #ROW SQUARE:
   RTS1 = RT_1**2
   RTS_1 = round(RTS1,3)
   RTSa = RT_a**2
   RTS_a = round(RTSa,3)
   RTSb = RT_b**2
   RTS_b = round(RTSb,3)
   RTSab = RT_ab**2
   RTS_ab = round(RTSab,3)

   #COLUMN SQUARE:
   CS1 = C_1**2
   CS_1 = round(CS1,3)
   CS2 = C_2**2
   CS_2 = round(CS2,3)
   CS3 = C_3**2
   CS_3 = round(CS3,3)
   CS4 = C_4**2
   CS_4 = round(CS4,3)

   #STEP 1 -> TOTAL:

   TR1 = (RT_1 + RT_a + RT_b + RT_ab)
   TR = round(TR1,2)
   TC1 = (C_1 + C_2 + C_3 + C_4)
   TC = round(TC1,2)
   

   if TR == TC:
       T = TR
   else:
       print("--Given Data ERROR--")

   # STEP 2 -> C.F

   N = R * C
   C_F = round((T**2)/N,1)
   ANS = 1/4*(CS_1+CS_2+CS_3+CS_4)
   
   #STEP 3 -> sum of squares of individual
   
   M = m**2
   SM = M[0][0]+M[1][0]+M[2][0]+M[3][0] + M[0][1]+M[1][1]+M[2][1]+M[3][1] + M[0][2]+M[1][2]+M[2][2]+M[3][2] +  M[0][3]+M[1][3]+M[2][3]+M[3][3]
   #Func call
   Tss = TSS(SM,C_F)
   Ssc = SSC(ANS,C_F)
   Ssr = SSR(RTS_1,RTS_a,RTS_b,RTS_ab,C_F)
   Sse = SSE(Tss,Ssc,Ssr)
   b = B(RT_1,RT_a,RT_b,RT_ab)
   a = A(RT_1,RT_a,RT_b,RT_ab)
   ab = AB(RT_1,RT_a,RT_b,RT_ab)
   sb = SB(b,R)
   sa = SA(a,R)
   sab = SAB(ab,R)
   print(f"Step->1 Grand total(T) : \t{T}\nStep->2 (C.F) : \t\t{C_F}\nStep->3 (Sum of SOI) : \t\t{SM}\nStep->4 (TSS) : \t\t{Tss}")
   print(f"Step->5 (SSC) : \t\t{Sse}\nStep->6 (SSR) : \t\t{Ssr}\nStep->7 (SSE) : \t\t{Sse}\nStep->8 [B] : \t\t\t{b}")
   print(f"Step->9 [A] : \t\t\t{a}\nStep->10 [AB] : \t\t{ab}\nStep->11 [SB] : \t\t{sb}\nStep->12 [SA] : \t\t{sa}\nStep->13 (SAB) : \t\t{sab}")
   print("\t\t","-"*25,"ANOVA TABLE","-"*25,"\n")
   ANOVA(sb,sa,sab,Sse,N,C,R)
   #print(sb,sa,sab)
   #print(a,b,ab)
   
def TSS(SM,C_F):
    #STEP 4 ->sum of squares of individual - C.F

    return round(SM - C_F,2)

def SSC(ANS,C_F):
    #STEP 5 -> sum of squares column - C.F

    return round(ANS - C_F,3)

def SSR(RTS_1,RTS_a,RTS_b,RTS_ab,C_F):
    #STEP 6 -> sum of squares rows

    ANS = 1/4*(RTS_1+RTS_a+RTS_b+RTS_ab)
    return round(ANS - C_F, 2)

def SSE(Tss,Ssc,Ssr):
    #STEP 7 -> Residual
    ANS = Tss -(Ssc+Ssr)
    return round(ANS,3)

def B(RT_1,RT_a,RT_b,RT_ab):
    #STEP 8
    ANS = RT_ab-RT_a+RT_b-RT_1
    return round(ANS,1)

def A(RT_1,RT_a,RT_b,RT_ab):
    #STEP 9
    ANS = RT_ab+RT_a-RT_b-RT_1
    return round(ANS,1)

def AB(RT_1,RT_a,RT_b,RT_ab):
    #STEP 10
    ANS = RT_ab-RT_a-RT_b+RT_1
    return round(ANS,1)

def SB(b,r):
    #STEP 11
    ANS =  (b**2)/(4*r)
    return round(ANS , 2)

def SA(a,r):
    #STEP 12
    ANS =  (a**2)/(4*r)
    return round(ANS , 2)

def SAB(ab,r):
    #STEP 13
    ANS =  (ab**2)/(4*r)
    return round(ANS , 2)

def ANOVA(sb,sa,sab,Sse,N,C,R):
    #Mean squares
    MSB =sb
    MSA = sa
    MSAB = sab
   
    #Error degree of freedom formula & Mean square MSE
    Error = N-C-R+1
    MSE = round(Sse/Error,2)

    #Variance ratio - F
    FB = round(MSB/MSE,2)
    FA = round(MSA/MSE,2)
    FAB = round(MSAB/MSE,2)

    print(f"{'Source of variation':<25}{'Degree of Freedom':<22}{'Sum of Squares':<18}{'Mean squares':<18}{'Ratio - F':<18}")
    print("-"*95)
    print(f"{'B':<25}{'1':<22}{sb:<18}{MSB:<18}{FB:<18}")
    print(f"{'A':<25}{'1':<22}{sa:<18}{MSA:<18}{FA:<18}")
    print(f"{'AB':<25}{'1':<22}{sab:<18}{MSAB:<18}{FAB:<18}")
    print(f"{'Error':<25}{'9':<22}{Sse:<18}{MSE:<18}{'-':<18}")

main()
   #---------------------------------------------------------------------------------------------------------------------
   
