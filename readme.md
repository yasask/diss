1. get_http.py
	to start the project from scratch this file needs to be run through mitmproxy
	Open mitmproxy and call the function 'mitmweb -s get_http.py --mode socks5 --showhost'

2. web_automation.py
	having installed the selenium driver, run this python script

3. tracking.py
	this script is run to cross-reference the tracking list with the combined list of data to add 1 to the tracking url in the combined list
	and to add 0 to others
4. cookie_jar.py
	is used to collect the cookies from the training list generated by tracking.py
5. cookieJar_data_collected.py
	this script is run to collect the cookies from the data being collected from MITM
6. ml.pynb
	this is the python notebook that creates machine learning algorithm
*/ the machine learning notebook named 'ml.pynb' can be run if the whole project does not want to be started again, all the nessesary data is provided in the folder
already being generated*/# diss