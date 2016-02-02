from app import app

#print(__name__) tulostaisi __main__, koska run.py on app:n main tiedosto

"""
#if -lauseella voitaisiin tarkistaa, onko run.py jo käynnissä, ettei yritä käynnistää uudelle, 
jos esim. importoitas run.py muualla
 -> __name__ = app ja __main__ = app
if __name__=='__main__':
"""

app.run(debug=True)