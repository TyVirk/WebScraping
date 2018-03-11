import requests

month=1

while month<13:
	r = requests.get('http://www.intellicast.com/Local/History.aspx?month='+str(month)+'&location=USNY1172')
	data={}
	i=0
	lines = r.text.split("\n")
	for line in lines:
		if '<td style="padding-left:5px;">' in line:
			temp = line.split('>')[1].split('<')[0]
			data['day']=temp
		
		if '<td>' in line:	
			temp2=line.split('<td>')[1].split('</td')[0]
			data['temp']=temp2
		print data
	month+=1

	