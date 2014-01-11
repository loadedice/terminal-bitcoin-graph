import termsiz, subprocess, json, time
from urllib import request
x,y = [],[]
api = "https://btc-e.com/api/2/btc_usd/ticker"
queue = 50
gnuplot = subprocess.Popen(["/usr/bin/gnuplot"],stdin=subprocess.PIPE)

while not False:
    req = request.urlopen(api)
    encoding = req.headers.get_content_charset()
    data = json.loads(req.read().decode(encoding))
    #x.append(data['ticker']['updated'])
    x.append(time.strftime("%X"))
    y.append(data['ticker']['last'])
    settings="set term dumb {} {} ;set xdata time; set timefmt \"%H:%M:%S\"\n".format(termsiz.get_terminal_width(),termsiz.get_terminal_height())
    gnuplot.stdin.write(bytes(settings,"utf-8"))
    gnuplot.stdin.write(bytes("plot '-' using 1:2 title 'Bitcoin' with linespoints \n","utf-8"))
    for i,j in zip(x,y):
        gnuplot.stdin.write(bytes("%s %f\n" % (i,j),"utf-8"))
    gnuplot.stdin.write(bytes("e\n","utf-8"))
    gnuplot.stdin.flush()
    time.sleep(10)
