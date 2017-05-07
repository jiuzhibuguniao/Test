from Projectile import *

def getInputs():
    a=eval(input("Enter the launch angle (in degree)"))
    v=eval(input("Enter the initial velocity (in meters/sec)"))
    h=eval(input("Enter the initial height (in meters)"))
    t=eval(input("Enter the time interval"))

    return a,v,h,t

def main():
    angle,vel,h0,time=getInputs()
    shot=Projectile(angle,vel,h0)
    while shot.gety()>=0:
        shot.update(time)

    print("\nDistance traveled:{0:0.1f}meters".format(shot.getx()))


if __name__=="__main__":
    main()
