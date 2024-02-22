import math
# 1030 HR Steel info
sultmet = 470_000_000
sulteng = 68_000

seprime_met = sultmet/2
seprime_eng = sulteng/2



bend_mom = int(input('what is the bending moment'))
torque = int(input('what is the torque'))
diameter = int(input('what is the diameter'))
stress_con = int()
criteria = input('what criteria? (g, vm, c, cig)')

#se
ka = 2*(sulteng**(-.217))
print(ka)

if diameter <= 2:
    kb = 0.879 * (diameter**(-0.107))
if diameter > 2:
    kb = 0.91*(diameter**(-.157))


print(kb)

# def se(se_prime, ka = 1,kb = 1,kc = 1,kd = 1,ke = 1)
#     kb =
#     kc =
#     kd =
#     ke =
#     se = ka*kb*kc*kd*ke*se_prime
#     return se



#goodman criteria 
def goodman(d,kf,kfs,ma,tm,se, sult):

    # finding A
    a = math.sqrt((4*(kf*ma)**2))

    #finding B
    b = math.sqrt((3*(kfs*tm)**2))

    safety = ((math.pi*(d**3))/16) * ((a/se)+(b/sult))**(-1)
    return safety
goodman(diameter,kf,kfs,bend_mom,torque,se,sulteng)