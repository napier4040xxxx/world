from flask import Flask, render_template
import json

w=json.load(open('worldl.json'))
for c in w:
  c['tld']=c['tld'][1:]
  page_size=20
app=Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('index.html',
      w=w[0:page_size])
    #return '<br>'.join([c['name'] for c in w])

@app.route('/begin/<b>')
def beginPage(b):
    bn=int(b)
    
    return render_template('index.html',
                           w=w[bn:bn+page_size],
                           page_number=bn,
                           page_size=page_size
                           )

@app.route('/continent/<a>')
def continentPage(a):
    cl=[c['name'] for c in w if c['continent']==a]
    return render_template('continent.html',
                           length_of_cl=len(cl),
                           cl=cl,
                           a=a)

@app.route('/country/<i>')
def countryPage(i):
    
    return render_template('country.html', c=w[int(i)])
    #return w[int(i)]['name'] +':' +w[int(i)]['continent'] +':' +w[int(i)]['capital'] 

@app.route('/countryByName/<n>')
def countryByNamePage(n):
    c=None
    for x in w:
        if x['name'] == n:
            c = x
       
    return render_template('country.html', c=c)

if (__name__=='__main__'):
  app.run(host='0.0.0.0', port=8080, debug=True)

#localhost:8080
