from scapy.all import *
from flask import Flask, render_template, request

def packetBuilder(args):
	packet = IP(dst=args[0], src=args[1])/TCP(sport=args[2], dport=args[3], seq=args[4],ack=args[5],dataofs=args[6],reserved=args[7],flags=args[8],window=args[9],chksum=args[10],urgptr=args[11],options={})/Raw(load=args[14])
	send(packet)

def checker(var):
	if var == '':
		return 0
	return var

'''
###[ TCP ]###
        sport     = ftp_data
        dport     = http
        seq       = 0
        ack       = 0
        dataofs   = None
        reserved  = 0
        flags     = S
        window    = 8192
        chksum    = None
        urgptr    = 0
        options   = {}
'''

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":

		feilds = []

		shostP = request.form["SHost"]
		feilds.append(str(shostP))

		dhostP = request.form["DHost"]
		feilds.append(str(dhostP))

		sportP = request.form["SPort"]
		feilds.append(int(checker(sportP)))

		dportP = request.form["DPort"]
		feilds.append(int(checker(dportP)))

		scP = request.form["Sequence Number"]
		feilds.append(int(checker(scP)))

		anP = request.form["Acknowledgment Number"]
		feilds.append(int(checker(anP)))

		doP = request.form["Data Offset"]
		feilds.append(int(checker(doP)))

		rP = request.form["Reversed"]
		feilds.append(int(checker(rP)))

		fP = request.form["Flags"]
		feilds.append(int(checker(fP)))

		wP = request.form["Window"]
		feilds.append(int(checker(wP)))

		csP = request.form["Checksum"]
		feilds.append(int(checker(csP)))

		upP = request.form["Urgent Pointer"]
		feilds.append(int(checker(upP)))

		oP = request.form["Option"]
		feilds.append(int(checker(oP)))

		pP = request.form["Padding"]
		feilds.append(int(checker(pP)))

		dP = request.form["Data"]
		feilds.append(str(dP))
		
		packetBuilder(feilds)

		#then execute packetBuilder and send the resaults to resualts.html
		return render_template('home.html')
	return render_template('home.html')



if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5000)