#©2020 Jerold B. Larson. All Rights Reserved.

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.style.use(['dark_background'])

import matplotlib.animation as animation
import time

ro = lambda x : round(x, ndigits=2)





def pos():
	fig = plt.figure(figsize=(12.66, 5))
	ax1, ax2 = fig.add_subplot(221), fig.add_subplot(222)
	ax3, ax4 = fig.add_subplot(223), fig.add_subplot(224)

	def AniOverview(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		b1r, s1r, b1w, s1w = ro(abs(min(b1))), ro(abs(min(s1))), ro(max(b1)), ro(max(s1))
		ww, wl, lw = ro(b1w+s1w), ro(b1w-s1r), ro(s1w-b1r)
		wwr, wlr, lwr = ro((ww/trisk)*100), ro((wl/trisk)*100), ro((lw/trisk)*100)
		Lnout = [ww, wl, lw]
		Lout = [wwr, wlr, lwr]

		ss = sum(Lout)

		wwz = [ww if n == ww else False for n in net]
		wlz = [wl if n == wl else False for n in net]
		lwz = [lw if n == lw else False for n in net]


		if min(b1) < min(s1): prmin = int(round(min(b1), ndigits=0))
		else: prmin = int(round(min(s1), ndigits=0))
		if max(b1) < max(s1): prmax = int(round(max(b1), ndigits=0))
		else: prmax = int(round(max(s1), ndigits=0))
		
		prng = range(prmin, prmax, 2)
		Lrisk = [b1r, s1r]
		Lret = [b1w, s1w]
		LL = [b1w, b1r, s1r, s1w]
		LLabel = 'over-return', 'over-risk','under-risk', 'under-return'
		labels='over-Risk', 'under-Risk'
		for ax in [ax1, ax2, ax3, ax4]: ax.clear()


		ax1.clear()
		ax1.step(viz_rng, b1, color='#009900')

		ax2.clear()
		ax2.step(viz_rng, s1, color='#FF0000')
		
		ax3.clear()
		ax3.step(viz_rng, net, color='yellow')


		ax4.clear()
		ax4.step(viz_rng, b1, color='#009900')
		ax4.step(viz_rng, s1, color='#FF0000')
		ax4.step(viz_rng, net, color='yellow')
		
		

		for ax in [ax1, ax2]: ax.set_xticks([])
		for ax in [ax3, ax4]: ax.set_xlabel("Total Points", fontsize=16)
		for ax in [ax1, ax3]: ax.set_ylabel("Outcome ($)", fontsize=16)

		ax1.set_title('Over ($)', fontsize=12)
		ax2.set_title('Under ($)', fontsize=12)
		ax3.set_title('Net ($)', fontsize=12)
		ax4.set_title('All ($)', fontsize=12)


	fig.suptitle("Position Analysis", fontsize=18)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()




def scene():
	fig = plt.figure(figsize=(6.45, 7.15))
	ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

	def AniOverview(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		b1r, s1r, b1w, s1w = ro(abs(min(b1))), ro(abs(min(s1))), ro(max(b1)), ro(max(s1))
		ww, wl, lw = ro(b1w+s1w), ro(b1w-s1r), ro(s1w-b1r)
		wwr, wlr, lwr = ro((ww/trisk)*100), ro((wl/trisk)*100), ro((lw/trisk)*100)

		for ax in [ax1, ax2]: ax.clear()
		ax1.clear()
		ax1.bar('WW\n $' + str(ww), ww, color='g')
		ax1.bar('WL\n $' + str(wl), wl, color='y')
		ax1.bar('LW\n $' + str(lw), lw, color='r')

		ax2.clear()
		ax2.bar('WW\n $' + str(wwr), wwr, color='g')
		ax2.bar('WL\n $' + str(wlr), wlr, color='y')
		ax2.bar('LW\n $' + str(lwr), lwr, color='r')


		ax1.set_xlabel('Outcome ($)', fontsize=14)
		ax2.set_xlabel('ROI (%)', fontsize=14)

	fig.suptitle("Scenario Analysis", fontsize=18)

	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()





#risk
def risk():
	fig = plt.figure(figsize=(12.66, 5))
	ax1, ax2 = fig.add_subplot(231), fig.add_subplot(232)
	ax3, ax4 = fig.add_subplot(233), fig.add_subplot(234)
	ax5, ax6 = fig.add_subplot(235), fig.add_subplot(236)

	def AniOverview(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		b1r, s1r, b1w, s1w = ro(abs(min(b1))), ro(abs(min(s1))), ro(max(b1)), ro(max(s1))
		ww, wl, lw = ro(b1w+s1w), ro(b1w-s1r), ro(s1w-b1r)
		wwr, wlr, lwr = ro((ww/trisk)*100), ro((wl/trisk)*100), ro((lw/trisk)*100)

		Lout = [wwr, wlr, lwr]

		ss = sum(Lout)

		
		if min(b1) < min(s1): prmin = int(round(min(b1), ndigits=0))
		else: prmin = int(round(min(s1), ndigits=0))
		if max(b1) < max(s1): prmax = int(round(max(b1), ndigits=0))
		else: prmax = int(round(max(s1), ndigits=0))
		

		Lrisk = [b1r, s1r]
		Lret = [b1w, s1w]
		LL = [b1w, b1r, s1r, s1w]
		LLabel = 'over-return', 'over-risk','under-risk', 'under-return'
		labels='over-Risk', 'under-Risk'
		for ax in [ax1, ax2, ax3, ax4, ax5, ax6]: ax.clear()


		ax1.clear()
		ax1.barh('under\n $' + str(s1r), s1r, color='#9999FF')
		ax1.barh('over\n $' + str(b1r), b1r, color='#FF8000')


		ax2.clear()
		ax2.barh('under\n $' + str(s1w), s1w, color='#9999FF')
		ax2.barh('over\n $' + str(b1w), b1w, color='#FF8000')

		
		ax3.clear()
		ax3.barh('under\nreturn', s1w, color='#9999FF')
		ax3.barh('over\nreturn', b1w, color='#FF8000')
		ax3.barh('under\nrisk', s1r, color='#9999FF')
		ax3.barh('over\nrisk', b1r, color='#FF8000')



		ax4.clear()
		ax4.pie(Lrisk, labels=['over-risk', 'under-risk'], colors=['#FF8000', '#9999FF'], autopct='%.0f%%')

		
		ax5.clear()
		ax5.pie(Lret, labels=['over-return', 'under-return'], colors=['#FF8000', '#9999FF'], autopct='%.0f%%')


		ax6.clear()
		if (b1r + b1w) > (s1r+s1w):
			ax6.pie(LL, labels=LLabel, colors=['#336600', '#FF0505', '#FF9900', '#9999FF'], autopct='%.0f%%')
		else:
			ax6.pie(LL, labels=LLabel, colors=[ '#FF9900', '#9999FF', '#FF0505', '#336600'], autopct='%.0f%%')


		ax1.set_title("Risk($)", fontsize=12)
		ax2.set_title("Return($)", fontsize=12)


		ax3.set_title("Risk/Return($)", fontsize=12)


	fig.suptitle("Risk Analysis", fontsize=18)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()


