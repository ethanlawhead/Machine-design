import math
# 1030 HR Steel info
sultmet = 470_000_000
sulteng = 68

seprime_met = sultmet/2
seprime_eng = sulteng/2

root_a_bending = 0.246-(3.08*10**(-3)*sulteng)+(1.51*10**(-5)*sulteng**2)-(2.67*10**(-8)*sulteng**3)
root_a_torsion = 0.190-(2.51*10**(-3)*sulteng)+(1.35*10**(-5)*sulteng**2)-(2.67*10**(-8)*sulteng**3)



bend_mom = int(input('what is the bending moment'))
torque = int(input('what is the torque'))
diameter = int(input('what is the diameter'))
stress_con = int()
criteria = input('what criteria? (g, vm, c, cig)')
kt_criteria = input('what is stress concentration?')

if kt_criteria == 'sharp':
    kt = 2.7
    kts = 2.2
    r = .02 *diameter
elif kt_criteria =='round':
    kt = 1.7
    kts = 1.5
    r = .1 *diameter
elif kt_criteria =='end':
    kt = 2.14
    kts = 3
    r =.02*diameter
elif kt_criteria =='sled':
    kt = 1.7
    kts = 1
    r =.01
elif kt_criteria == 'ring':
    kt = 5
    kts = 3
    r = .01

#kf
kf = 1 + ((kt - 1)/(1 + (root_a_bending/math.sqrt(r))))
kfs = 1 + ((kts - 1)/(1 + (root_a_torsion/math.sqrt(r))))

#se
ka = 2*(sulteng**(-.217))

if diameter <= 2:
    kb = 0.879 * (diameter**(-0.107))
if diameter > 2:
    kb = 0.91*(diameter**(-.157))



# def se(se_prime, ka = 1,kb = 1,kc = 1,kd = 1,ke = 1)
#     kb =
#     kc =
#     kd =
#     ke =
#     se = ka*kb*kc*kd*ke*se_prime
#     return se

se = seprime_eng * ka * kb
print(ka,kb,se)
print(kf,kfs)


#goodman criteria 
def goodman(d,kf,kfs,ma,tm,se, sult):

    # finding A
    a = math.sqrt((4*((kf*ma)**2)))
    print(a)
    #finding B
    b = math.sqrt((3*((kfs*tm)**2)))
    print(b)
    safety = ((math.pi*(d**3))/16) * (((a/(se*1000))+(b/(sult*1000)))**(-1))
    print(safety)
    return safety
goodman(diameter,kf,kfs,bend_mom,torque,se,sulteng)
