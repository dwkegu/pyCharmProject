import numpy as np
import math
from mmc.asserts.ADataProvider import DataProvider
from matplotlib import pyplot as mpl


mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

dp = DataProvider()
data = dp.getData2()
xNum = dp.x2
yNum = dp.y2
fg = mpl.figure()
ax = fg.add_subplot(111)
ax.set_aspect(1)
for i in range(0,xNum):
        mpl.scatter([data[i,1]],[data[i,2]],s=1,c='blue')
        # ax.add_artist(mpl.Circle((data[i,1],data[i,2]),radius=2,fill=False,color='red'))
mpl.xlim([0,100])
mpl.ylim([0,130])
mpl.title(u'移动终端位置')
mpl.show()
