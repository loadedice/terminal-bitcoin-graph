import termsiz, subprocess, json, time
from urllib import request
x,y = [],[]
api = "https://btc-e.com/api/2/btc_usd/ticker"
queue = 10

while not False:
    req = request.urlopen(api)
    encoding = req.headers.get_content_charset()
    data = json.loads(req.read().decode(encoding))
    x.append(data['ticker']['updated'])
    y.append(data['ticker']['last'])
    """"""
    gnuplot = subprocess.Popen(["/usr/bin/gnuplot"],stdin=subprocess.PIPE)
    settings="set term dumb {} {}\n".format(termsiz.get_terminal_width(),termsiz.get_terminal_height())
    gnuplot.stdin.write(bytes(settings,"utf-8"))
    gnuplot.stdin.write(bytes("plot '-' using 1:2 title 'Bitcoin' with linespoints \n","utf-8"))
    for i,j in zip(x,y):
        gnuplot.stdin.write(bytes("%f %f\n" % (i,j),"utf-8"))
    gnuplot.stdin.write(bytes("e\n","utf-8"))
    gnuplot.stdin.flush()
    time.sleep(12)
