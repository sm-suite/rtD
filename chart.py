#©2020 Jerold B. Larson. All Rights Reserved.

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.style.use(['ggplot'])
plt.style.use(['seaborn-darkgrid'])

import matplotlib.animation as animation
import time

ro = lambda x : round(x, ndigits=2)





#position
def scene():
	fig = plt.figure(figsize=(9, 12))
	ax1, ax2 = fig.add_subplot(321), fig.add_subplot(322)
	ax3, ax4 = fig.add_subplot(323), fig.add_subplot(324)
	ax5, ax6 = fig.add_subplot(325), fig.add_subplot(326)

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
		labels='Over-Risk', 'Under-Risk'
		for ax in [ax1, ax2, ax3, ax4, ax5, ax6]: ax.clear()



		ax1.clear()
		ax1.stem(viz_rng,sroi, linefmt='None', markerfmt='r--', use_line_collection=True)		
		ax1.stem(viz_rng,broi, linefmt='None', markerfmt='g--', use_line_collection=True)
		ax1.stem(viz_rng,roi, linefmt='None', markerfmt='y-', use_line_collection=True)




		ax2.clear()
		ax2.step(viz_rng, b1, color='#009900')
		ax2.step(viz_rng, s1, color='#FF0000')



		ax3.clear()
		ax3.bar('total-risk', trisk, color='b')
		ax3.bar('win-win', ww, color='g')

		
		ax4.clear()
		if wl>lw:	
			ax4.bar('win-loss', wl, color='y')
			ax4.bar('loss-win', lw, color='r')
		else:
			ax4.bar('loss-win', lw, color='y')
			ax4.bar('win-loss', wl, color='r')



		
		ax5.clear()
		ax5.barh('LW\n $' + str(lw), lw, color='#FF8000')
		ax5.barh('WL\n $' + str(wl), wl, color='#FF8000')
		ax5.barh('WW\n $' + str(ww), ww, color='#9999FF')


		ax6.clear()
		ax6.barh('LW\n ' + str(lwr) + '%', lwr, color='#FF8000')
		ax6.barh('WL\n ' + str(wlr) + '%', wlr, color='#FF8000')
		ax6.barh('WW\n ' + str(wwr) + '%', wwr, color='#9999FF')




		#for ax in [ax1]: ax.set_title('Risk/Return Weight', fontsize=12)
		ax1.set_title('ROI(%)')
		ax2.set_title('Over/Under ($)')
		ax3.set_title('Total Risk / Win-Win ($)')
		ax4.set_title('Win-Loss / Loss-Win ($)')
		ax5.set_title('Scenarios($)')
		ax6.set_title('Scenarios ROI(%)')

	fig.suptitle("Scenario Analysis", fontsize=16)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()



#risk
def risk():
	fig = plt.figure(figsize=(10, 6))
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
		labels='Over-Risk', 'Under-Risk'
		for ax in [ax1, ax2, ax3, ax4, ax5, ax6]: ax.clear()


		ax1.clear()
		ax1.barh('Under\n $' + str(s1r), s1r, color='#9999FF')
		ax1.barh('Over\n $' + str(b1r), b1r, color='#FF8000')


		ax2.clear()
		ax2.barh('Under\n $' + str(s1w), s1w, color='#9999FF')
		ax2.barh('Over\n $' + str(b1w), b1w, color='#FF8000')

		
		ax3.clear()
		ax3.barh('Under\nreturn', s1w, color='#9999FF')
		ax3.barh('Over\nreturn', b1w, color='#FF8000')
		ax3.barh('Under\nrisk', s1r, color='#9999FF')
		ax3.barh('Over\nrisk', b1r, color='#FF8000')



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


	fig.suptitle("Risk Analysis", fontsize=16)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()




