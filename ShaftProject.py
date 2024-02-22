import math
# 1030 HR Steel info
sultmet = 470_000_000
sulteng = 68
sy = 37_500

seprime_met = sultmet/2
seprime_eng = sulteng/2

root_a_bending = 0.246-(3.08*10**(-3)*sulteng)+(1.51*10**(-5)*sulteng**2)-(2.67*10**(-8)*sulteng**3)
root_a_torsion = 0.190-(2.51*10**(-3)*sulteng)+(1.35*10**(-5)*sulteng**2)-(2.67*10**(-8)*sulteng**3)



bend_mom = int(input('what is the bending moment'))
torque = int(input('what is the torque'))
diameter = float(input('what is the diameter'))
criteria = input('what criteria? (g, vm, c, cig)')
kt_criteria= input('what is stress concentration?')

def stress_concentration(diameter,kt_criteria):

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
    
    kf = 1 + ((kt - 1)/(1 + (root_a_bending/math.sqrt(r))))
    kfs = 1 + ((kts - 1)/(1 + (root_a_torsion/math.sqrt(r))))
    
    return kf,kfs
print(stress_concentration(1,kt_criteria))
#kf
print(stress_concentration(1,kt_criteria)[0])
print(stress_concentration(diameter,kt_criteria))


#se
ka = 2*(sulteng**(-.217))

if diameter <= 2 and diameter != 0:
    kb = 0.879 * (diameter**(-0.107))
elif diameter > 2:
    kb = 0.91*(diameter**(-.157))
else:
    kb = 1


se = seprime_eng * ka * kb
def sigma_prime(diameter,ma,tm)
    sigmaa_prime = math.sqrt((((32*(stress_concentration(diameter)[0])*ma)/(math.pi*(diameter**3)))**2))
    sigmam_prime = math.sqrt(3*(((16*(stress_concentration(diameter)[1])*tm)/(math.pi*(diameter**3)))**2))
    return (sigmaa_prime,sigmam_prime)
#goodman criteria 
def goodman(d,kf,kfs,ma,tm,se, sult):

    # finding A
    a = math.sqrt((4*((kf*ma)**2)))
    #finding B
    b = math.sqrt((3*((kfs*tm)**2)))
    safety = ((math.pi*(d**3))/16) * (((a/(se*1000))+(b/(sult*1000)))**(-1))
    print(safety)
    return safety
#goodman(diameter,kf,kfs,bend_mom,torque,se,sulteng)

def von_mises(kf,kfs,sy,ma,tm,d):
    sigma_max = math.sqrt((((32*kf*ma)/(math.pi*(d**3)))**2)+(3*(((16*kfs*tm)/(math.pi*(d**3)))**2)))
    safety = (sy/sigma_max)
    print(safety)
    return safety

#von_mises(kf,kfs,sy,bend_mom,torque,diameter)
    
def conservative(sigmaM,sigmaA,sy):

    safety = sy/(sigmaM + sigmaA)
    print(safety)
    return safety

#conservative(sigmam_prime,sigmaa_prime,sy)
    
def cig(sigmaM,SigmaA,sy,kf,kfs,ma,tm,se,sult):
    good_diameter = 0.000
    conserve_diameter = 0
    safety_factor = 1.5
    good_safe = 0
    conserve_safe = 0
    while good_safe != safety_factor:
        good_diameter += 0.001
        good_safe = goodman(diameter,kf,kfs,ma,tm,se,sult)

    while conserve_safe != safety_factor:
        conserve_diameter += 0.001
        conservative(,,sy)

    print(diameter)

cig(sigma_prime[0],sigma_prime[1],sy,kf,kfs,bend_mom,torque,se,sulteng)