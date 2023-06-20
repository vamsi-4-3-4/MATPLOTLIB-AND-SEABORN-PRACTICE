import matplotlib.pyplot as plt
a=["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
sunday=13*60+42
saturday=10*60+45
friday=13*60+31
thursday=11*60+52
wednesday=12*60+25
tuesday=12*60+44
monday=15*60+28
s_st=sunday-2*60+55
sat_st=saturday-3*60+16
f_st=friday-2*60+26
th_st=thursday-4*60+33
w_st=wednesday-4*60+20
tue_st=tuesday-3*60+31
m_st=monday-2*60+13
b=[sunday,monday,tuesday,wednesday,thursday,friday,saturday]
c=[s_st,m_st,tue_st,w_st,th_st,f_st,sat_st]
plt.style.use("dark_background")
plt.plot(a,b,label="phone usage",color="red",marker=".",linestyle="dashed",linewidth=2,markersize=12,alpha=1)
plt.plot(a,c,label="Study Time on phone",color="green",marker="s",linestyle="dotted",linewidth=2,markersize=12,alpha=0.5)
#limits on the axis
total_mins_in_a_day=24*60
plt.axis([0,7,0,total_mins_in_a_day])
plt.xlabel("DAYS OF THE WEEK")
plt.ylabel("STUDY TIME IN THE MINUTES")
plt.title("MY STUDY ANALYSIS")
plt.legend()
plt.show()
