#=============================================================imports===============================================================================
import os
import pandas as pd
import datetime
#=============================================================initiation===============================================================================
def timee(hour):
    return (
        "morning" if 5 <= hour <= 17
        else
        "evening" if 18 <= hour <= 20
        else
        "night"
    )
now = datetime.datetime.now()
hour=int(now.hour)
if timee(hour)=='morning':
	bgimg="https://c0.wallpaperflare.com/preview/565/50/536/sky-cloud-blue-background.jpg"
elif timee(hour)=='evening':
	bgimg="https://images.hdqwalls.com/wallpapers/cloudy-sky-evening-sky-4k-zm.jpg"
elif timee(hour)=='night':
	bgimg="https://wallpaperaccess.com/full/149370.jpg"
cwd=os.getcwd()
thefiletobereadwhichisinputbytheuser='Simplifi.xlsx'
data=pd.read_excel(thefiletobereadwhichisinputbytheuser)
df=pd.DataFrame(data)
writegraphx=[]
writegraphy=[]
rowlst_master = df.to_numpy().tolist()
collst_master = df.transpose().values.tolist()

try:
		htmlout=open('index.html','x')
		htmlout.close()
		htmlout=open('index.html','w')
except FileExistsError:
		try:
				os.remove('index.html')
		except OSError:
				print('FILE ERROR')
				input()
				quit()
		htmlout=open('index.html','x')
		htmlout.close()
		htmlout=open('index.html','w')
htmllines=[]
htmllines.append('''<html>
<title>Simplifi Dashboard</title>
	<!-- Material Design Lite -->
	<script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
	<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
	<!-- Material Design icon font -->
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<script>
(function() {
  'use strict';
  window['counter'] = 0;
  var snackbarContainer = document.querySelector('#demo-toast-example');
  var showToastButton = document.querySelector('#demo-show-toast');
  showToastButton.addEventListener('click', function() {
	'use strict';
	var data = {message: 'Example Message # ' + ++counter};
	snackbarContainer.MaterialSnackbar.showSnackbar(data);
  });
}());
</script>
<style>
html { overflow-y: scroll; overflow-x:hidden; scroll-behavior: smooth;}
body {position: absolute; }
#view-source {
position: fixed;
display: block;
right: 0;
bottom: 0;
margin-right: 40px;
margin-bottom: 40px;
z-index: 900;
}
.demo-card-wide.mdl-card {
  width: 550px;
}
.demo-card-wide-1.mdl-card {
  width: 85%;
}
.demo-card-wide-1 > .mdl-card__title {
  color: #fff;
  height: 176px;
  background: url(' '''+bgimg+''' ') center / cover;
}
.demo-card-wide-1 > .mdl-card__menu {
  color: #fff;
}

.demo-card-wide > .mdl-card__title {
  color: #fff;
  height: 176px;
  background: url(' '''+bgimg+''' ') center / cover;
}

.mdl-layout {
  align-items: center;
  justify-content: center;
}
@media print
{
#view-source {display:none;}
#liawetmat {display:none;}
#liprnopo {display:none;}
#lliawetmat {display:none;}
#nlieawetmat {display:none;}
#m80 {display:none;}
#readys {display:none;}
#uniqwo {display:none;}
#unreadys {display:none;}
#noprrrrr {display:none;}
.demo-card-wide-1 {display:none;}
.noprint {display:none;}
.mdl-button-1 {display:none;}
}

@media screen
{
...
}
//.iframe-container {
//    overflow-x:scroll;
//    overflow-y: scroll;
//    padding-top: 56.25%;
//    position: relative;
//}
//.iframe-container iframe {
//   border: 0;
//   height: 100%;
//   left: 0;
//   position: absolute;
//   top: 0;
//   width: 100%;
//}
</style>
</head>
<body style="background-image:url(' '''+bgimg+''' '); background-size: cover; background-repeat: no-repeat; background-attachment: fixed;">
<br><br><br><br><br><br><br>
<div class="mdl-layout">
<div class="demo-card-wide mdl-card mdl-shadow--2dp through mdl-shadow--16dp" align="center">
<table class="mdl-data-table mdl-js-data-table" align="center">''')
htmllines.append('<tbody>')
#=============================================================standard definitions===============================================================================

def collst(x): #given column name, get the list of cells in the column
		coldf=pd.DataFrame(data,columns=[x])
		colst=coldf.transpose().values.tolist()
		return colst
def nec(i):
		i=str(i)
		if i!='nan' and i!='0' and i!=0 and i!=[] and i!='' and i!=' ' and i!=() and i!={} and i!='\t' and i!=None:
				return True
		else:
				return False

def listunest(l):
		for i in l:
				finl=i
				break
		return finl

#=============================================================MAIN PROCESSING===============================================================================

#1- Total # of Jobs
wocol=collst('JOB')
for i in wocol:
		finwocol=i
		break
uniqwo=[]
uniqro=[]
c=0
for i in finwocol:
		c+=1
		uniqwo.append(finwocol[c-1])
		uniqro.append(c)
print("TOTAL # OF JOBS : ",len(uniqwo))

#Initiation for Priority Tooltip
em=0
ur=0
no=0
sd=0

htmllines.append('<tr>')
htmllines.append('<td class="mdl-data-table__cell--non-numeric">Total # of Jobs</td>')
htmlstr='<td><a href="#calendar"><button class="mdl-button mdl-js-button mdl-js-ripple-effect">'+str(len(finwocol))+'</button></a>'
writegraphx.append('Total # of Jobs')
writegraphy.append(str(len(finwocol)))
htmllines.append(htmlstr)
htmllines.append('</td>')
htmllines.append('</tr>')



filename='jobs.html'
lst=uniqwo
title='List of jobs'
rono=uniqro


wod=listunest(collst('JOB DESCRIPTION'))
#print(rono)
wodi=[]
pod=listunest(collst('PRIORITY'))
#print(len(pod))
#print(rono)
podi=[]
eod=listunest(collst('DAYS NEEDED'))
#print(rono)
eodi=[]
for i in rono:
		try:
				wodi.append(wod[i-1])
		except IndexError:
				pass
		try:
				eodi.append(eod[i-1])
		except IndexError:
				pass
		try:
				podi.append(pod[i-1])
		except IndexError:
				pass
		#PRIORITY TOOLTIP COUNTS
		try:
			prior=pod[i-1]
		except IndexError:
			prior=9999
		if prior==1:
			em+=1
		elif prior==2:
			ur+=1
		elif prior==3:
			no+=1
		elif prior==4:
			sd+=1
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
				uniqwoo=open(filename,'x')
				uniqwoo.close()
				uniqwoo=open(filename,'w')
		except OSError:
				pass

uniqwoo.write(str('<h3 align="center">'+title+'</h3>\n<br><br>'))
towrite=[str('''<html>
<title>'''+title+'''</title>   <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.5.6/css/buttons.dataTables.min.css">

<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,900;1,100;1,300&display=swap" rel="stylesheet">
<style>
p {
	font-family: 'Roboto', sans-serif;
}
h1,h2,h3{
	font-family: 'Roboto', sans-serif;
	font-weight: 900; 
}
table,label {
	font-family: 'Roboto', sans-serif;
}
</style>

<script
src="https://code.jquery.com/jquery-3.4.1.min.js"
integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
crossorigin="anonymous"></script>

<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/buttons.html5.min.js"></script>


<script>
$(document).ready(function(){
$('#example').DataTable({
	dom: 'Bfrtip',
buttons: [
	'copyHtml5',
	'excelHtml5',
	'csvHtml5',
	'pdfHtml5'
]
});
});


</script>

</head>
<body>
''')]
count=0
towrite.append("""
<table id="example" class="display nowrap" style="width:100%"><thead>
<tr><th class="mdl-data-table__cell--non-numeric">S.No.</th>
<th class="mdl-data-table__cell--non-numeric">Job</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Priority</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Days Needed</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Job Description</th></tr></thead>
<tbody>""")

for i in lst:
		towrite.append('<tr><td class="mdl-data-table__cell">')
		towrite.append(str(((count+1))))
		#DEBUG-print(((rono[count])+1),end='  ')
		towrite.append('</td><td>')
		towrite.append(str(i))
		#DEBUG-print(i,end='  ')
		towrite.append('</td><td>')
		towrite.append(str(podi[count]))
##                try:
##                        print(podi[count],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(eodi[count]))
##                try:
##                        print(eodi[count-1],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(wodi[count]))
##                try:
##                        print(wodi[count-1])
##                except:
##                        pass
		towrite.append('</td></tr>')
		count+=1
towrite.append('''</tbody></table>''')
uniqwoo.writelines(towrite)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))







htmllines.append('<tr>')
htmllines.append('<td class="mdl-data-table__cell--non-numeric">Total # of Jobs</td>')
htmlstr='<td><a href="#uniqwo"><button class="mdl-button mdl-js-button mdl-button--primary" id="tt4"><b>'+str(len(uniqwo))+'</b></button></a>'
htmllines.append(htmlstr)
##showlistasdial(0,uniqwo)
htmllines.append('''
	<div class="mdl-tooltip" data-mdl-for="tt4">
'''+str(em)+''' EMERGENCY<br>'''+str(ur)+''' URGENT<br>'''+str(no)+''' NORMAL.
</div>''')
htmllines.append('</td>')
htmllines.append('</tr>')


print()


#2 - Total # complete jobs
totl=[collst("COMPLETION")]
readys=[]
idklol=list(df.columns.values).index('COMPLETION')
for i in range(len((rowlst_master))):
			   if i in uniqro:
					   if nec(str(rowlst_master[i-1][idklol]))==True:
							   readys.append(i)
readyswolst=[]
for i in readys:
		try:
				readyswolst.append(finwocol[i-1])
		except IndexError:
				pass




filename='readys.html'
lst=readyswolst
title='List of Complete Jobs'
rono=readys

wod=listunest(collst('JOB DESCRIPTION'))
#print(rono)
wodi=[]
pod=listunest(collst('PRIORITY'))
#print(len(pod))
#print(rono)
podi=[]
eod=listunest(collst('DAYS NEEDED'))
#print(rono)
eodi=[]
for i in rono:
		try:
				wodi.append(wod[i-1])
		except IndexError:
				pass
		try:
				eodi.append(eod[i-1])
		except IndexError:
				pass
		try:
				podi.append(pod[i-1])
		except IndexError:
				pass
		#PRIORITY TOOLTIP COUNTS
		try:
			prior=pod[i-1]
		except IndexError:
			prior=9999
		if prior==1:
			em+=1
		elif prior==2:
			ur+=1
		elif prior==3:
			no+=1
		elif prior==4:
			sd+=1
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
				uniqwoo=open(filename,'x')
				uniqwoo.close()
				uniqwoo=open(filename,'w')
		except OSError:
				pass

uniqwoo.write(str('<h3 align="center">'+title+'</h3>\n<br><br>'))
towrite=[str('''<html>
<title>'''+title+'''</title>   <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.5.6/css/buttons.dataTables.min.css">

<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,900;1,100;1,300&display=swap" rel="stylesheet">
<style>
p {
	font-family: 'Roboto', sans-serif;
}
h1,h2,h3{
	font-family: 'Roboto', sans-serif;
	font-weight: 900; 
}
table,label {
	font-family: 'Roboto', sans-serif;
}
</style>

<script
src="https://code.jquery.com/jquery-3.4.1.min.js"
integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
crossorigin="anonymous"></script>

<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/buttons.html5.min.js"></script>


<script>
$(document).ready(function(){
$('#example').DataTable({
	dom: 'Bfrtip',
buttons: [
	'copyHtml5',
	'excelHtml5',
	'csvHtml5',
	'pdfHtml5'
]
});
});


</script>

</head>
<body>
''')]
count=0
towrite.append("""
<table id="example" class="display nowrap" style="width:100%"><thead>
<tr><th class="mdl-data-table__cell--non-numeric">S.No.</th>
<th class="mdl-data-table__cell--non-numeric">Job</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Priority</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Days Needed</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Job Description</th></tr></thead>
<tbody>""")

for i in lst:
		towrite.append('<tr><td class="mdl-data-table__cell">')
		towrite.append(str(((count+1))))
		#DEBUG-print(((rono[count])+1),end='  ')
		towrite.append('</td><td>')
		towrite.append(str(i))
		#DEBUG-print(i,end='  ')
		towrite.append('</td><td>')
		towrite.append(str(podi[count]))
##                try:
##                        print(podi[count],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(eodi[count]))
##                try:
##                        print(eodi[count-1],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(wodi[count]))
##                try:
##                        print(wodi[count-1])
##                except:
##                        pass
		towrite.append('</td></tr>')
		count+=1
towrite.append('''</tbody></table>''')
uniqwoo.writelines(towrite)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))










htmllines.append('<tr>')
htmllines.append('<td class="mdl-data-table__cell--non-numeric">Total # of Complete Jobs</td>')
htmlstr='<td><a href="#readys"><button class="mdl-button mdl-js-button mdl-button--accent">'+str(len(readys))+'</button></a>'
htmllines.append(htmlstr)
writegraphx.append('Total # of Complete Jobs')
writegraphy.append(str(len(readys)))
htmllines.append('</td>')
htmllines.append('</tr>')



print()




#3 - Total # of incomplete jobs
unreadys=[]
for i in uniqro:
		if (i in readys)==False:
				unreadys.append(i+1)
		else:
				pass

unreadyswolst=[]

for i in unreadys:
		try:
				unreadyswolst.append(finwocol[i-1])
		except IndexError:
				pass

filename='unreadys.html'
lst=unreadyswolst
title='List of Incomplete Jobs'
rono=unreadys

wod=listunest(collst('JOB DESCRIPTION'))
#print(rono)
wodi=[]
pod=listunest(collst('PRIORITY'))
#print(len(pod))
#print(rono)
podi=[]
eod=listunest(collst('DAYS NEEDED'))
#print(rono)
eodi=[]
for i in rono:
		try:
				wodi.append(wod[i-1])
		except IndexError:
				pass
		try:
				eodi.append(eod[i-1])
		except IndexError:
				pass
		try:
				podi.append(pod[i-1])
		except IndexError:
				pass
		#PRIORITY TOOLTIP COUNTS
		try:
			prior=pod[i-1]
		except IndexError:
			prior=9999
		if prior==1:
			em+=1
		elif prior==2:
			ur+=1
		elif prior==3:
			no+=1
		elif prior==4:
			sd+=1
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
				uniqwoo=open(filename,'x')
				uniqwoo.close()
				uniqwoo=open(filename,'w')
		except OSError:
				pass

uniqwoo.write(str('<h3 align="center">'+title+'</h3>\n<br><br>'))
towrite=[str('''<html>
<title>'''+title+'''</title>   <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.5.6/css/buttons.dataTables.min.css">

<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,900;1,100;1,300&display=swap" rel="stylesheet">
<style>
p {
	font-family: 'Roboto', sans-serif;
}
h1,h2,h3{
	font-family: 'Roboto', sans-serif;
	font-weight: 900; 
}
table,label {
	font-family: 'Roboto', sans-serif;
}
</style>

<script
src="https://code.jquery.com/jquery-3.4.1.min.js"
integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
crossorigin="anonymous"></script>

<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/buttons.html5.min.js"></script>


<script>
$(document).ready(function(){
$('#example').DataTable({
	dom: 'Bfrtip',
buttons: [
	'copyHtml5',
	'excelHtml5',
	'csvHtml5',
	'pdfHtml5'
]
});
});


</script>

</head>
<body>
''')]
count=0
towrite.append("""
<table id="example" class="display nowrap" style="width:100%"><thead>
<tr><th class="mdl-data-table__cell--non-numeric">S.No.</th>
<th class="mdl-data-table__cell--non-numeric">Job</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Priority</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Days Needed</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Job Description</th></tr></thead>
<tbody>""")

for i in lst:
		towrite.append('<tr><td class="mdl-data-table__cell">')
		towrite.append(str(((count+1))))
		#DEBUG-print(((rono[count])+1),end='  ')
		towrite.append('</td><td>')
		towrite.append(str(i))
		#DEBUG-print(i,end='  ')
		towrite.append('</td><td>')
		towrite.append(str(podi[count]))
##                try:
##                        print(podi[count],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(eodi[count]))
##                try:
##                        print(eodi[count-1],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(wodi[count]))
##                try:
##                        print(wodi[count-1])
##                except:
##                        pass
		towrite.append('</td></tr>')
		count+=1
towrite.append('''</tbody></table>''')
uniqwoo.writelines(towrite)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))





htmllines.append('<tr>')
htmllines.append('<td class="mdl-data-table__cell--non-numeric">Total # of Incomplete Jobs</td>')
htmlstr='<td><a href="#unreadys"><button class="mdl-button mdl-js-button mdl-button--accent">'+str(len(unreadys))+'</button></a>'
htmllines.append(htmlstr)
writegraphx.append('Total # of Incomplete Jobs')
writegraphy.append(str(len(unreadys)))
htmllines.append('</td>')
htmllines.append('</tr>')

print()


# 4 - # of jobs to do today

tdys=[]
tdysno=[]
daysleft=listunest(collst('DAYS LEFT'))
daysneeded=listunest(collst('DAYS NEEDED'))
status=listunest(collst('COMPLETION'))
print(status)
for i in range(len(uniqwo)):
	if abs((daysleft[i])-(daysneeded[i]))<=5:
		if nec(status[i])==False:
			tdys.append(uniqwo[i])
			tdysno.append(i+1)
for i in range(len(uniqwo)):
	if (daysneeded[i])>15:
		if abs((daysleft[i])-(daysneeded[i]))<=10:
			if nec(status[i])==False:
				tdys.append(uniqwo[i])
				tdysno.append(i+1)

filename='tdys.html'
lst=tdys
title="List of Today's Jobs"
rono=tdysno

wod=listunest(collst('JOB DESCRIPTION'))
#print(rono)
wodi=[]
pod=listunest(collst('DAYS LEFT'))
#print(len(pod))
#print(rono)
podi=[]
eod=listunest(collst('DAYS NEEDED'))
#print(rono)
eodi=[]
for i in rono:
		try:
				wodi.append(wod[i-1])
		except IndexError:
				pass
		try:
				eodi.append(eod[i-1])
		except IndexError:
				pass
		try:
				podi.append(pod[i-1])
		except IndexError:
				pass
		#PRIORITY TOOLTIP COUNTS
		try:
			prior=pod[i-1]
		except IndexError:
			prior=9999
		if prior==1:
			em+=1
		elif prior==2:
			ur+=1
		elif prior==3:
			no+=1
		elif prior==4:
			sd+=1
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
				uniqwoo=open(filename,'x')
				uniqwoo.close()
				uniqwoo=open(filename,'w')
		except OSError:
				pass

uniqwoo.write(str('<h3 align="center">'+title+'</h3>\n<br><br>'))
towrite=[str('''<html>
<title>'''+title+'''</title>   <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.5.6/css/buttons.dataTables.min.css">

<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,900;1,100;1,300&display=swap" rel="stylesheet">
<style>
p {
	font-family: 'Roboto', sans-serif;
}
h1,h2,h3{
	font-family: 'Roboto', sans-serif;
	font-weight: 900; 
}
table,label {
	font-family: 'Roboto', sans-serif;
}
</style>

<script
src="https://code.jquery.com/jquery-3.4.1.min.js"
integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
crossorigin="anonymous"></script>

<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.2/js/buttons.html5.min.js"></script>


<script>
$(document).ready(function(){
$('#example').DataTable({
	dom: 'Bfrtip',
buttons: [
	'copyHtml5',
	'excelHtml5',
	'csvHtml5',
	'pdfHtml5'
]
});
});


</script>

</head>
<body>
''')]
count=0
towrite.append("""
<table id="example" class="display nowrap" style="width:100%"><thead>
<tr><th class="mdl-data-table__cell--non-numeric">S.No.</th>
<th class="mdl-data-table__cell--non-numeric">Job</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Days Left</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Days Needed</th>
<th class="mdl-data-table__cell--non-numeric" align="right">Job Description</th></tr></thead>
<tbody>""")

for i in lst:
		towrite.append('<tr><td class="mdl-data-table__cell">')
		towrite.append(str(((count+1))))
		#DEBUG-print(((rono[count])+1),end='  ')
		towrite.append('</td><td>')
		towrite.append(str(i))
		#DEBUG-print(i,end='  ')
		towrite.append('</td><td>')
		towrite.append(str(podi[count]))
##                try:
##                        print(podi[count],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(eodi[count]))
##                try:
##                        print(eodi[count-1],end='  ')
##                except:
##                        pass
		towrite.append('</td><td>')
		towrite.append(str(wodi[count]))
##                try:
##                        print(wodi[count-1])
##                except:
##                        pass
		towrite.append('</td></tr>')
		count+=1
towrite.append('''</tbody></table>''')
uniqwoo.writelines(towrite)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))





htmllines.append('<tr>')
htmllines.append('<td class="mdl-data-table__cell--non-numeric">Total # of Todays Jobs</td>')
htmlstr='<td><a href="#m80"><button class="mdl-button mdl-js-button mdl-button--accent">'+str(len(tdys))+'</button></a>'
htmllines.append(htmlstr)
writegraphx.append('Total # of Todays Jobs')
writegraphy.append(str(len(tdys)))
htmllines.append('</td>')
htmllines.append('</tr>')

print()









#=============================================================Graph Creation===============================================================================
graphhtml=('''<!DOCTYPE HTML>
<html lang="" >
    <head>
        <meta charset="UTF-8">
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
        <title>GRAPH OF STOCK MATERIAL TRACKER : LESS THAN 100</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <style>
        @media print
		{
			.noprint {display:none;}
		}
		</style>
        <meta name="description" content="">
        <meta name="generator" content="GitBook 3.2.2">
        <meta name="author" content="chartjs">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
<script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    	<meta name="HandheldFriendly" content="true"/>
    	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    	<meta name="apple-mobile-web-app-capable" content="yes">
    	<meta name="apple-mobile-web-app-status-bar-style" content="black">
    	<link rel="apple-touch-icon-precomposed" sizes="152x152" href="../gitbook/images/apple-touch-icon-precomposed-152.png">
    	<link rel="shortcut icon" href="../gitbook/images/favicon.ico" type="image/x-icon">  
    	<link rel="next" href="radar.html" />
    	<link rel="prev" href="line.html" />
    	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
    </head>
    <body>
    <div class="chartjs-wrapper"><canvas id="chartjs-2" class="chartjs" width="undefined" height="undefined"></canvas><script>
new Chart(document.getElementById("chartjs-2"),
{"type":"horizontalBar",
"data":{"labels":'''+str(writegraphx)+''',
"datasets":[{"label":"Analysed Number",
"data":'''+str(writegraphy)+''',
"fill":false,"backgroundColor":["rgba(255, 99, 132, 0.2)","rgba(255, 159, 64, 0.2)","rgba(255, 205, 86, 0.2)",
"rgba(75, 192, 192, 0.2)","rgba(54, 162, 235, 0.2)","rgba(153, 102, 255, 0.2)","rgba(201, 203, 207, 0.2)"],"borderColor":["rgb(255, 99, 132)","rgb(255, 159, 64)","rgb(255, 205, 86)",
"rgb(75, 192, 192)","rgb(54, 162, 235)","rgb(153, 102, 255)","rgb(201, 203, 207)"],"borderWidth":1}]},"options":{"scales":{"xAxes":[{"ticks":{"beginAtZero":true}}]}}});
</script></div></p>
    <script src="../gitbook/gitbook.js"></script>
    <script src="../gitbook/theme.js"></script>
	<script src="../gitbook/gitbook-plugin-search-plus/jquery.mark.min.js"></script>
    <script src="../gitbook/gitbook-plugin-search-plus/search.js"></script>
    <script src="../gitbook/gitbook-plugin-anchorjs/anchor.min.js"></script>
    <script src="../gitbook/gitbook-plugin-anchorjs/anchor-style.js"></script>
    <script src="../gitbook/gitbook-plugin-ga/plugin.js"></script>
    <script src="../gitbook/gitbook-plugin-sharing/buttons.js"></script>
    <script src="../gitbook/gitbook-plugin-fontsettings/fontsettings.js"></script>

    <div class='noprint'>
<a href="javascript:window.print()"><button id="demo-show-snackbar" class="mdl-button mdl-js-button mdl-button--raised" type="button">Print</button></a>
<div id="demo-snackbar-example" class="mdl-js-snackbar mdl-snackbar">
  <div class="mdl-snackbar__text"></div>
  <button class="mdl-snackbar__action" type="button"></button>
</div>
<script>
(function() {
  'use strict';
  var snackbarContainer = document.querySelector('#demo-snackbar-example');
  var showSnackbarButton = document.querySelector('#demo-show-snackbar');
  var handler = function(event) {
	showSnackbarButton.style.backgroundColor = '';
  };
  showSnackbarButton.addEventListener('click', function() {
	'use strict';
	var data = {
	  message: 'To export to PDF, choose Save As PDF',
	  timeout: 2000,
	};
	snackbarContainer.MaterialSnackbar.showSnackbar(data);
  });
}());
</script>
</div>
	</body>
</html>''')
filename='graphdash.html'
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
		except OSError:
				pass
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
uniqwoo.write(graphhtml)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))








#=============================================================Calendar Creation===============================================================================

calhtml=('''<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Simplifi - Calendar</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Calendar</title>
  <meta name="description" content="Calendar">
  <meta name="author" content="Charles Anderson">
  <link rel="stylesheet" href="style.css">

</head>

<body>
  <div class="content">
    <div class="calendar-container">
      <div class="calendar"> 
        <div class="year-header"> 
          <span class="left-button" id="prev"> &lang; </span> 
          <span class="year" id="label"></span> 
          <span class="right-button" id="next"> &rang; </span>
        </div> 
        <table class="months-table"> 
          <tbody>
            <tr class="months-row">
              <td class="month">Jan</td> 
              <td class="month">Feb</td> 
              <td class="month">Mar</td> 
              <td class="month">Apr</td> 
              <td class="month">May</td> 
              <td class="month">Jun</td> 
              <td class="month">Jul</td>
              <td class="month">Aug</td> 
              <td class="month">Sep</td> 
              <td class="month">Oct</td>          
              <td class="month">Nov</td>
              <td class="month">Dec</td>
            </tr>
          </tbody>
        </table> 
        
        <table class="days-table"> 
          <td class="day">Sun</td> 
          <td class="day">Mon</td> 
          <td class="day">Tue</td> 
          <td class="day">Wed</td> 
          <td class="day">Thu</td> 
          <td class="day">Fri</td> 
          <td class="day">Sat</td>
        </table> 
        <div class="frame"> 
          <table class="dates-table"> 
              <tbody class="tbody">             
              </tbody> 
          </table>
        </div> 
      </div>
    </div>
    <div class="events-container">
    </div>
  </div>
  <!-- Dialog Box-->
  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous">
  </script>
  <script src="app.js"></script>
</body>
</html>
<!-- partial -->
  <script  src="./script.js"></script>

</body>
</html>
''')
filename='calendar.html'
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
		except OSError:
				pass
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
uniqwoo.write(calhtml)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))


calcss=('''/* Overall body and content */
body { 
    height: 100%;
    width: 100%;
    margin: 0;
    background: #005C97;    
    background: -webkit-linear-gradient(left, #363795, #005C97);
    background: -moz-linear-gradient(left, #363795, #005C97);
    background: -o-linear-gradient(left, #363795, #005C97);
    background: linear-gradient(to right, #363795, #005C97); 
    font-family: Helvetica;
} 
.content {
    overflow: none;
    max-width: 790px;
    padding: 0px 0;
    height: 500px;
    position: relative;
    margin: 20px auto;
    background: #52A0FD;
    background: -moz-linear-gradient(right,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
    background: -webkit-linear-gradient(right,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
    background: linear-gradient(to left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);    
    border-radius: 3px;
    box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    -moz-box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    -webkit-box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}

/*  Events display */
.events-container {
    overflow-y: scroll;
    height: 100%;
    float: right;
    margin: 0px auto; 
    font: 13px Helvetica, Arial, sans-serif; 
    display: inline-block; 
    padding: 0 10px;
    border-bottom-right-radius: 3px;
    border-top-right-radius: 3px;
}
.events-container:after{
    clear:both;
}
.event-card {
    padding: 20px 0;
    width: 350px;
    margin: 20px auto;
    display: block;
    background: #fff;
    border-left: 10px solid #52A0FD;
    border-radius: 3px;
    box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    -moz-box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    -webkit-box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}
.event-count, .event-name, .event-cancelled {
    display: inline;
    padding: 0 10px;
    font-size: 1rem;
}
.event-count {
    color: #52A0FD;
    text-align: right;
}
.event-name {
    padding-right:0;
    text-align: left;
}
.event-cancelled {
    color: #FF1744;
    text-align: right;
}

/*  Calendar wrapper */
.calendar-container  { 
    float: left;
    position: relative;
    margin: 0px auto; 
    height: 100%;
    background: #fff;
    font: 13px Helvetica, Arial, san-serif; 
    display: inline-block; 
    border-bottom-left-radius: 3px;
    border-top-left-radius: 3px;
}
.calendar-container:after{
    clear:both;
}
.calendar {
    display: table;
}

/* Calendar Header */
.year-header { 
    background: #52A0FD;
    background: -moz-linear-gradient(left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
    background: -webkit-linear-gradient(left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
    background: linear-gradient(to right,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);    
    font-family: Helvetica;
    box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    -moz-box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    -webkit-box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    height: 40px; 
    text-align: center;
    position: relative; 
    color:#fff; 
    border-top-left-radius: 3px;
} 
.year-header span { 
    display:inline-block; 
    font-size: 20px;
    line-height:40px; 
}
.left-button, .right-button { 
    cursor: pointer;
    width:28px; 
    text-align:center; 
    position:absolute; 
} 
.left-button { 
    left:0; 
    -webkit-border-top-left-radius: 5px; 
    -moz-border-radius-topleft: 5px; 
    border-top-left-radius: 5px; 
} 
.right-button { 
    right:0; 
    top:0; 
    -webkit-border-top-right-radius: 5px; 
    -moz-border-radius-topright: 5px; 
    border-top-right-radius: 5px; 
} 
.left-button:hover {
    background: #3FADFF;
}
.right-button:hover { 
    background: #00C1FF;
}

/* Buttons */
.button{
    cursor: pointer;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    outline: none;
    font-size: 1rem;
    border-radius: 25px;
    padding: 0.65rem 1.9rem;
    transition: .2s ease all;
    color: white;
    border: none;
    box-shadow: -1px 10px 20px #9BC6FD;
    background: #52A0FD;
    background: -moz-linear-gradient(left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
    background: -webkit-linear-gradient(left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
    background: linear-gradient(to right,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
}
#cancel-button {
    box-shadow: -1px 10px 20px #FF7DAE;
    background: #FF1744;
    background: -moz-linear-gradient(left,  #FF1744 0%, #FF5D95 80%, #FF5D95 100%);
    background: -webkit-linear-gradient(left,  #FF1744 0%, #FF5D95 80%, #FF5D95 100%);
    background: linear-gradient(to right,  #FF1744 0%, #FF5D95 80%, #FF5D95 100%);
}
#add-button {
    display: block;
    position: absolute;
    right:20px;
    bottom: 20px;
}
#add-button:hover, #ok-button:hover, #cancel-button:hover {
    transform: scale(1.03);
}
#add-button:active, #ok-button:active, #cancel-button:active {
    transform: translateY(3px) scale(.97);
}

/* Days/months tables */
.days-table, .dates-table, .months-table { 
    border-collapse:separate; 
    text-align: center;
} 
.day { 
    height: 26px;
    width: 26px;
    padding: 0 10px;
    line-height: 26px; 
    border: 2px solid transparent;
    text-transform:uppercase; 
    font-size:90%; 
    color:#9e9e9e; 
} 
.month {
    cursor: default;
    height: 26px;
    width: 26px;
    padding: 0 2px;
    padding-top:10px;
    line-height: 26px; 
    text-transform:uppercase; 
    font-size: 11px; 
    color:#9e9e9e; 
    transition: all 250ms;
}
.active-month {
    font-weight: bold;
    font-size: 14px;
    color: #FF1744;
    text-shadow: 0 1px 4px RGBA(255, 50, 120, .8);
}
.month:hover {
    color: #FF1744;
    text-shadow: 0 1px 4px RGBA(255, 50, 120, .8);
}

/*  Dates table */
.table-date {
    cursor: default;
    color:#2b2b2b; 
    height:26px;
    width: 26px;
    font-size: 15px;
    padding: 10px;
    line-height:26px; 
    text-align:center; 
    border-radius: 50%;
    border: 2px solid transparent;
    transition: all 250ms;
}
.table-date:not(.nil):hover { 
    border-color: #FF1744;
    box-shadow: 0 2px 6px RGBA(255, 50, 120, .9);
}
.event-date {
    border-color:#52A0FD;
    box-shadow: 0 2px 8px RGBA(130, 180, 255, .9);
}
.active-date{ 
    background: #FF1744;
    box-shadow: 0 2px 8px RGBA(255, 50, 120, .9);
    color: #fff;
}
.event-date.active-date {
    background: #52A0FD;
    box-shadow: 0 2px 8px RGBA(130, 180, 255, .9);
}

/* input dialog */
.dialog{
    z-index: 5;
    background: #fff;
    position:absolute;
    width:415px;
    height: 500px;
    left:387px;
    border-top-right-radius:3px;
    border-bottom-right-radius: 3px;
    display:none;
    border-left: 1px #aaa solid;
}
.dialog-header {
    margin: 20px;
    color:#333;
    text-align: center;
}
.form-container {
    margin-top:25%;
}
.form-label {
    color:#333;
}
.input {
    border:none;
    background: none;
    border-bottom: 1px #aaa solid;
    display:block;
    margin-bottom:50px;
    width: 200px;
    height: 20px;
    text-align: center;
    transition: border-color 250ms;
}
.input:focus {
    outline:none;
    border-color: #00C9FB;
}
.error-input {
    border-color: #FF1744;
}

/* Tablets and smaller */
@media only screen and (max-width: 780px) {
    .content {
        overflow: visible;
        position:relative;
        max-width: 100%;
        width: 370px;
        height: 100%;
        background: #52A0FD;
        background: -moz-linear-gradient(left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
        background: -webkit-linear-gradient(left,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);
        background: linear-gradient(to right,  #52A0FD 0%, #00C9FB 80%, #00C9FB 100%);  
    }
    .dialog {
        width:370px;
        height: 450px;
        border-radius: 3px;
        top:0;
        left:0;
    }
    .events-container {
        float:none;
        overflow: visible;
        margin: 0 auto;
        padding: 0;
        display: block;
        left: 0;
        border-radius: 3px;
    }

    .calendar-container {
        float: none;
        padding: 0;
        margin: 0 auto;
        margin-right: 0;
        display: block;
        left: 0;
        border-radius: 3px;
        box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
        -moz-box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
        -webkit-box-shadow: 3px 8px 16px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    }
}

/* Small phone screens */
@media only screen and (max-width: 400px) {
    .content, .events-container, .year-header, .calendar-container {
        width: 320px;
    }
    .dialog {
        width: 320px;
    }
    .months-table {
        display: block;
        margin: 0 auto;
        width: 320px;
    }
    .event-card {
        width: 300px;
    }
    .day {
        padding: 0 7px;
    }
    .month {
        display: inline-block;
        padding: 10px 10px;
        font-size: .8rem;
    }
    .table-date {
        width: 20px;
        height: 20px;
        line-height: 20px;
    }
    .event-name, .event-count, .event-cancelled {
        font-size: .8rem;
    }
    .add-button{
        bottom: 10px;
        right: 10px;
        padding: 0.5rem 1.5rem;
    }
}
''')
filename='style.css'
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
		except OSError:
				pass
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
uniqwoo.write(calcss)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))



caljs=[('''// Setup the calendar with the current date
$(document).ready(function(){
    var date = new Date();
    var today = date.getDate();
    // Set click handlers for DOM elements
    $(".right-button").click({date: date}, next_year);
    $(".left-button").click({date: date}, prev_year);
    $(".month").click({date: date}, month_click);
    $("#add-button").click({date: date}, new_event);
    // Set current month as active
    $(".months-row").children().eq(date.getMonth()).addClass("active-month");
    init_calendar(date);
    var events = check_events(today, date.getMonth()+1, date.getFullYear());
    show_events(events, months[date.getMonth()], today);
});

// Initialize the calendar by appending the HTML dates
function init_calendar(date) {
    $(".tbody").empty();
    $(".events-container").empty();
    var calendar_days = $(".tbody");
    var month = date.getMonth();
    var year = date.getFullYear();
    var day_count = days_in_month(month, year);
    var row = $("<tr class='table-row'></tr>");
    var today = date.getDate();
    // Set date to 1 to find the first day of the month
    date.setDate(1);
    var first_day = date.getDay();
    // 35+firstDay is the number of date elements to be added to the dates table
    // 35 is from (7 days in a week) * (up to 5 rows of dates in a month)
    for(var i=0; i<35+first_day; i++) {
        // Since some of the elements will be blank, 
        // need to calculate actual date from index
        var day = i-first_day+1;
        // If it is a sunday, make a new row
        if(i%7===0) {
            calendar_days.append(row);
            row = $("<tr class='table-row'></tr>");
        }
        // if current index isn't a day in this month, make it blank
        if(i < first_day || day > day_count) {
            var curr_date = $("<td class='table-date nil'>"+"</td>");
            row.append(curr_date);
        }   
        else {
            var curr_date = $("<td class='table-date'>"+day+"</td>");
            var events = check_events(day, month+1, year);
            if(today===day && $(".active-date").length===0) {
                curr_date.addClass("active-date");
                show_events(events, months[month], day);
            }
            // If this date has any events, style it with .event-date
            if(events.length!==0) {
                curr_date.addClass("event-date");
            }
            // Set onClick handler for clicking a date
            curr_date.click({events: events, month: months[month], day:day}, date_click);
            row.append(curr_date);
        }
    }
    // Append the last row and set the current year
    calendar_days.append(row);
    $(".year").text(year);
}

// Get the number of days in a given month/year
function days_in_month(month, year) {
    var monthStart = new Date(year, month, 1);
    var monthEnd = new Date(year, month + 1, 1);
    return (monthEnd - monthStart) / (1000 * 60 * 60 * 24);    
}

// Event handler for when a date is clicked
function date_click(event) {
    $(".events-container").show(250);
    $("#dialog").hide(250);
    $(".active-date").removeClass("active-date");
    $(this).addClass("active-date");
    show_events(event.data.events, event.data.month, event.data.day);
};

// Event handler for when a month is clicked
function month_click(event) {
    $(".events-container").show(250);
    $("#dialog").hide(250);
    var date = event.data.date;
    $(".active-month").removeClass("active-month");
    $(this).addClass("active-month");
    var new_month = $(".month").index(this);
    date.setMonth(new_month);
    init_calendar(date);
}

// Event handler for when the year right-button is clicked
function next_year(event) {
    $("#dialog").hide(250);
    var date = event.data.date;
    var new_year = date.getFullYear()+1;
    $("year").html(new_year);
    date.setFullYear(new_year);
    init_calendar(date);
}

// Event handler for when the year left-button is clicked
function prev_year(event) {
    $("#dialog").hide(250);
    var date = event.data.date;
    var new_year = date.getFullYear()-1;
    $("year").html(new_year);
    date.setFullYear(new_year);
    init_calendar(date);
}

// Event handler for clicking the new event button
function new_event(event) {
    // if a date isn't selected then do nothing
    if($(".active-date").length===0)
        return;
    // remove red error input on click
    $("input").click(function(){
        $(this).removeClass("error-input");
    })
    // empty inputs and hide events
    $("#dialog input[type=text]").val('');
    $("#dialog input[type=number]").val('');
    $(".events-container").hide(250);
    $("#dialog").show(250);
    // Event handler for cancel button
    $("#cancel-button").click(function() {
        $("#name").removeClass("error-input");
        $("#count").removeClass("error-input");
        $("#dialog").hide(250);
        $(".events-container").show(250);
    });
    // Event handler for ok button
    $("#ok-button").unbind().click({date: event.data.date}, function() {
        var date = event.data.date;
        var name = $("#name").val().trim();
        var count = parseInt($("#count").val().trim());
        var day = parseInt($(".active-date").html());
        // Basic form validation
        if(name.length === 0) {
            $("#name").addClass("error-input");
        }
        else if(isNaN(count)) {
            $("#count").addClass("error-input");
        }
        else {
            $("#dialog").hide(250);
            console.log("new event");
            new_event_json(name, count, date, day);
            date.setDate(day);
            init_calendar(date);
        }
    });
}

// Adds a json event to event_data
function new_event_json(name, count, date, day) {
    var event = {
        "occasion": name,
        "invited_count": count,
        "year": date.getFullYear(),
        "month": date.getMonth()+1,
        "day": day
    };
    event_data["events"].push(event);
}

// Display all events of the selected date in card views
function show_events(events, month, day) {
    // Clear the dates container
    $(".events-container").empty();
    $(".events-container").show(250);
    console.log(event_data["events"]);
    // If there are no events for this date, notify the user
    if(events.length===0) {
        var event_card = $("<div class='event-card'></div>");
        var event_name = $("<div class='event-name'>There are no events planned for "+month+" "+day+".</div>");
        $(event_card).css({ "border-left": "10px solid #FF1744" });
        $(event_card).append(event_name);
        $(".events-container").append(event_card);
    }
    else {
        // Go through and add each event as a card to the events container
        for(var i=0; i<events.length; i++) {
            var event_card = $("<div class='event-card'></div>");
            var event_name = $("<div class='event-name'>"+events[i]["occasion"]+"</div>");
            var event_count = $("<div class='event-count'></div>");
            if(events[i]["cancelled"]===true) {
                $(event_card).css({
                    "border-left": "10px solid #FF1744"
                });
                event_count = $("<div class='event-cancelled'>Cancelled</div>");
            }
            $(event_card).append(event_name).append(event_count);
            $(".events-container").append(event_card);
        }
    }
}

// Checks if a specific date has any events
function check_events(day, month, year) {
    var events = [];
    for(var i=0; i<event_data["events"].length; i++) {
        var event = event_data["events"][i];
        if(event["day"]===day &&
            event["month"]===month &&
            event["year"]===year) {
                events.push(event);
            }
    }
    return events;
}

var event_data = {
    "events": [
''')]

jobs=listunest(collst('JOB'))
jobdesc=listunest(collst('JOB DESCRIPTION'))
daysleft=listunest(collst('DAYS LEFT'))
events=[]
for i in range(len(jobs)):
	events.append(str(str(jobs[i])+' : '+str(jobdesc[i])))
deadline=[]
for i in daysleft:
	deadline.append((datetime.datetime.today()+datetime.timedelta(i)))
deadlines=[]
for i in deadline:
	month=str(i.month)
	date=str(i.day)
	year=str(i.year)
	deadlines.append([month,date,year])


for i in range(len(jobs)):
	if i!=(len(jobs)-1):
		caljs.append('''{
	        "occasion": " '''+events[i]+'''",
	        "year": '''+deadlines[i][2]+''',
	        "month": '''+deadlines[i][0]+''',
	        "day": '''+deadlines[i][1]+''',
	    },''')
	else:
		caljs.append('''{
	        "occasion": " '''+events[i]+'''",
	        "year": '''+deadlines[i][2]+''',
	        "month": '''+deadlines[i][0]+''',
	        "day": '''+deadlines[i][1]+''',
	    }''')
caljs.append('''    ]
};

const months = [ 
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December" 
];''')
filename='script.js'
try:
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
except FileExistsError:
		try:
				os.remove(filename)
		except OSError:
				pass
		uniqwoo=open(filename,'x')
		uniqwoo.close()
		uniqwoo=open(filename,'w')
uniqwoo.writelines(caljs)
uniqwoo.close()
os.system(str(str("attrib +h ")+str(uniqwoo.name)))












#=============================================================User Input / Wait before exit===============================================================================
htmllines.append('</table>')
htmllines.append('''<div class='noprint'>
<a href="javascript:window.print()"><button id="demo-show-snackbar" class="mdl-button mdl-js-button mdl-button--raised" type="button">Print</button></a>
<div id="demo-snackbar-example" class="mdl-js-snackbar mdl-snackbar">
  <div class="mdl-snackbar__text"></div>
  <button class="mdl-snackbar__action" type="button"></button>
</div>
<script>
(function() {
  'use strict';
  var snackbarContainer = document.querySelector('#demo-snackbar-example');
  var showSnackbarButton = document.querySelector('#demo-show-snackbar');
  var handler = function(event) {
	showSnackbarButton.style.backgroundColor = '';
  };
  showSnackbarButton.addEventListener('click', function() {
	'use strict';
	var data = {
	  message: 'To export to PDF, choose Save As PDF',
	  timeout: 2000,
	};
	snackbarContainer.MaterialSnackbar.showSnackbar(data);
  });
}());
</script>
</div>
''')
htmllines.append('''</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<div class="demo-card-wide-1 mdl-card mdl-shadow--2dp" id="uniqwo" style="width: 85%;">
  <div class="mdl-card__supporting-text">
	<iframe src="'''+str(str("jobs.html"))+'''" style="height: 512px" /></iframe>
  </div>
  <div class="mdl-card__actions mdl-card--border">
	<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" href="'''+str(str("jobs.html"))+'''" target="_blank">
	  Open in New Tab
	</a>
  </div>
</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<div class="demo-card-wide-1 mdl-card mdl-shadow--2dp" id="readys" style="width: 85%;">
  <div class="mdl-card__supporting-text">
	<iframe src="'''+str(str("readys.html"))+'''" style="height: 512px" /></iframe>
  </div>
  <div class="mdl-card__actions mdl-card--border">
	<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" href="'''+str(str("readys.html"))+'''" target="_blank">
	  Open in New Tab
	</a>
  </div>
</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<div class="demo-card-wide-1 mdl-card mdl-shadow--2dp" id="unreadys" style="width: 85%;">
  <div class="mdl-card__supporting-text">
	<iframe src="'''+str(str("unreadys.html"))+'''" style="height: 512px" /></iframe>
  </div>
  <div class="mdl-card__actions mdl-card--border">
	<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" href="'''+str(str("unreadys.html"))+'''" target="_blank">
	  Open in New Tab
	</a>
  </div>
</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<div class="demo-card-wide-1 mdl-card mdl-shadow--2dp" id="m80" style="width: 85%;">
  <div class="mdl-card__supporting-text">
	<iframe src="'''+str(str("tdys.html"))+'''" style="height: 512px" /></iframe>
  </div>
  <div class="mdl-card__actions mdl-card--border">
	<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" href="'''+str(str("tdys.html"))+'''" target="_blank">
	  Open in New Tab
	</a>
  </div>
</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<div class="demo-card-wide-1 mdl-card mdl-shadow--2dp" id="graphdash" style="width: 85%;">
  <div class="mdl-card__supporting-text">
	<iframe src="'''+str(str("graphdash.html"))+'''" style="height: 512px" /></iframe>
  </div>
  <div class="mdl-card__actions mdl-card--border">
	<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" href="'''+str(str("graphdash.html"))+'''" target="_blank">
	  Open in New Tab
	</a>
  </div>
</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<div class="demo-card-wide-1 mdl-card mdl-shadow--2dp" id="calendar" style="width: 85%;">
  <div class="mdl-card__supporting-text">
	<iframe src="'''+str(str("calendar.html"))+'''" style="height: 512px" /></iframe>
  </div>
  <div class="mdl-card__actions mdl-card--border">
	<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" href="'''+str(str("calendar.html"))+'''" target="_blank">
	  Open in New Tab
	</a>
  </div>
</div>
<xo id='noprrrrr'>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</xo>
<xo id='noprrrrr'>
<a href="#" id="view-source" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-color--primary mdl-color-text--accent-contrast noprint">View Dashboard</a>
<script src="$$hosted_libs_prefix$$/$$version$$/material.min.js"></script></xo>''')
htmllines.append('</body>')
htmllines.append('</html>')
htmlout.writelines(htmllines)
htmlout.close()
os.system(str(str("attrib +h ")+str(htmlout.name)))
pathofindexhtml="start brave.exe "+str(os.getcwd())+"\\index.html"
os.system(pathofindexhtml)