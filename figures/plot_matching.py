import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig, (ax,bx)=plt.subplots(1,2,figsize=(13,5.2),layout='constrained')
x=np.linspace(0,2,401)
ax.plot(x,1000*x,label='Seller minimum: q = 1,000x',color='#bd542e')
ax.plot(x,1100*x,label='Buyer maximum: q = 1,100x',color='#2866b0')
z=np.linspace(0,1.65,331)
ax.fill_between(z,1000*z,np.minimum(1100*z,1650),color='#46a77a',alpha=.25,label='Feasible transfers')
ax.axhline(1650,color='#666666',ls='--',lw=1)
ax.axvline(2,color='#888888',ls=':',lw=1)
ax.scatter([1.5,1.65],[1650,1650],color=['#2866b0','#bd542e'],zorder=5)
ax.annotate('Buyer rests\n(1.50, 1,650)',(1.5,1650),xytext=(.62,1910),arrowprops={'arrowstyle':'-','color':'#777'},fontsize=10)
ax.annotate('Seller rests\n(1.65, 1,650)',(1.65,1650),xytext=(1.63,1230),arrowprops={'arrowstyle':'-','color':'#777'},fontsize=10)
ax.set(xlabel='Asset transferred, x',ylabel='USDC transferred, q',title='1. Limits and maximum fill',xlim=(0,2.1),ylim=(0,2350))
ax.legend(loc='upper left',frameon=False,fontsize=9)
u=np.linspace(0,3,601)
bx.step(u,np.floor(u),where='post',color='#515ba4',lw=2)
bx.axvspan(0,1,color='#46a77a',alpha=.12)
for val,color,name,ytext in [(.20,'#26936a','Executable ask',.6),(.55,'#2866b0','Buyer limit',1.05),(.85,'#bd542e','Noncrossing ask',1.5)]:
    bx.scatter([val],[0],color=color,zorder=4,s=45)
    bx.annotate(name,(val,0),xytext=(val,ytext),ha='center',fontsize=9,arrowprops={'arrowstyle':'-','color':color})
bx.set(xlabel='Exact price minus 1,000 USDC (millionths of USDC)',ylabel='Stored key minus 1,000,000,000',title='2. Different exact prices, same bucket',xlim=(-.12,3.1),ylim=(-.35,3.5),yticks=[0,1,2,3])
bx.text(.05,.94,'18-decimal asset / 6-decimal USDC',transform=bx.transAxes,fontsize=10)
fig.savefig(out/'matching-limits.png',dpi=180)
fig.savefig(out/'matching-limits.svg')
print(out/'matching-limits.png')
