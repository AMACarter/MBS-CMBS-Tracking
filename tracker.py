from fredapi import Fred

fredapi = Fred(api_key='43014c898148b01637a1c1150e17ff0c')

# Treasury and Agency Securities: Mortgage-Backed Securities (MBS), All Commercial Banks
mbsbankdata = fredapi.get_series_latest_release('TMBACBW027SBOG')
mbsbankdata.tail()
print(mbsbankdata)

# Latest Mortgage 
mort30yeardata = fredapi.get_series_latest_release('MORTGAGE30US')
mort30yeardata.tail()
print(mort30yeardata)