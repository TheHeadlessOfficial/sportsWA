# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wasports.lock"
try:
    # Check for file lock
    open(lock_file, 'w').close()
    import os
    import requests
    import urllib.request
    # import module GEOPY
    from geopy.geocoders import Photon
    # initialize Photon API
    geolocator = Photon(user_agent="measurements")
    ################################ get your HOME automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude, city and APPID
    mylat = 45.40713
    mylon = 11.87680
    mycity = 'Padova'
    myAPPID = ''
    ################################ pattern url SPORTS
    url3 = 'https://api.weatherapi.com/v1/sports.json?key=' + myAPPID + '&q=' + mycity
    res3 = requests.get(url3).json()
    data3 = res3
    ################################ insert angle of my North in 'myd' (if no wind then winddeg doesn't load)
    vtext = 'n/a'
    ################################ set default conky folder (change it if needed)
    home = '/home/'
    conky = '/.conky/'
    defconkyfol = conky + 'weather/Weatherapi/'
    ################################ set the paths for the API files
    ptemp = defconkyfol + 'sports/'
    #                   set the path for the ERROR
    perr = home + homename + ptemp + '-error.txt'
    ################################ get data for ERROR section
    responseHTTP = requests.get(url3)
    # get status code
    status_code = responseHTTP.status_code
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(status_code))
    fo.close()
    if status_code != 200:
        #                   set the path for the ALERTS conky section
        psportsc = home + homename + ptemp + 'sportsconky.txt'
        fo = open(psportsc, 'w')
        fo.write("ERROR: ", status_code)
        fo.close()
    else:
        ############################################### GEOPY NEW SYNTAX
        urlGeopy = 'https://photon.komoot.io/reverse?lon=' + str(mylon) + '&lat='  + str(mylat)
        resGeopy = requests.get(urlGeopy).json()
        dataGeopy = resGeopy
        Glocation = urllib.request.urlopen(urlGeopy)
        #address = location
        Ghousenumber = "housenumber is old syntax"
        Groad = "street is old syntax"#dataGeopy['features'][0]['properties']['street']
        Gsuburb = dataGeopy['features'][0]['properties']['district']
        Gmunicipality = "municipality is old syntax"
        Gcity = dataGeopy['features'][0]['properties']['city']
        Gcounty = dataGeopy['features'][0]['properties']['county']
        Gstate = dataGeopy['features'][0]['properties']['state']
        Gcountry = dataGeopy['features'][0]['properties']['country']
        Gcodetemp = dataGeopy['features'][0]['properties']['countrycode']
        Gcode = Gcodetemp.lower()
        Gzipcode = dataGeopy['features'][0]['properties']['postcode']
        ################################ write raw data for GEOPY
        pgeopy = '/home/' + homename + ptemp + '-geopy.txt'
        fo = open(pgeopy, 'w')
        fo.write('lat: {}\n'.format(mylat))
        fo.write('lon: {}\n'.format(mylon))
        #fo.write('TimeZone: {}\n'.format(tz))
        #fo.write('TimeZoneoffset: {}\n'.format(tz_off))
        fo.write('house number: {}\n'.format(Ghousenumber))
        fo.write('road: {}\n'.format(Groad))
        fo.write('suburb: {}\n'.format(Gsuburb))
        fo.write('municipality: {}\n'.format(Gmunicipality))
        fo.write('city: {}\n'.format(Gcity))
        fo.write('state: {}\n'.format(Gstate))
        fo.write('county: {}\n'.format(Gcounty))
        fo.write('country: {}\n'.format(Gcountry))
        fo.write('country_code: {}\n'.format(Gcode))
        fo.write('zip: {}\n'.format(Gzipcode))
        #                   next row writes geopy data as dict
        fo.write('addressraw: {}\n'.format(Glocation.read()))
        fo.close()
        ################################ get data for SPORTS
        #                   football data
        try:
            footsta = data3['football']['stadium']
        except:
            footsta = vtext
        try:
            footcou = data3['football']['country']
        except:
            footcou = vtext
        try:
            footreg = data3['football']['region']
        except:
            footreg = vtext
        try:
            foottou = data3['football']['tournament']
        except:
            foottou = vtext
        try:
            footstart = data3['football']['start']
        except:
            footstart = vtext
        try:
            footmat = data3['football']['match']
        except:
            footmat = vtext
        #                   cricket data
        try:
            crista = data3['cricket']['stadium']
        except:
            crista = vtext
        try:
            cricou = data3['cricket']['country']
        except:
            cricou = vtext
        try:
            crireg = data3['cricket']['region']
        except:
            crireg = vtext
        try:
            critou = data3['cricket']['tournament']
        except:
            critou = vtext
        try:
            cristart = data3['cricket']['start']
        except:
            cristart = vtext
        try:
            crimat = data3['cricket']['match']
        except:
            crimat = vtext
        #                   golf data
        try:
            golfsta = data3['golf']['stadium']
        except:
            golfsta = vtext
        try:
            golfcou = data3['golf']['country']
        except:
            golfcou = vtext
        try:
            golfreg = data3['golf']['region']
        except:
            golfreg = vtext
        try:
            golftou = data3['golf']['tournament']
        except:
            golftou = vtext
        try:
            golfstart = data3['golf']['start']
        except:
            golfstart = vtext
        try:
            golfmat = data3['golf']['match']
        except:
            golfmat = vtext
        ################################ write SPORTS raw data on a file
        # set the path for SPORT raw data
        psportsraw = home + homename + ptemp + 'wasportsraw.txt'
        fo = open(psportsraw, 'w')
        #                   football data
        fo.write('footstadium: {}\n'.format(footsta))
        fo.write('footcountry: {}\n'.format(footcou))
        fo.write('footregion: {}\n'.format(footreg))
        fo.write('foottournament: {}\n'.format(foottou))
        fo.write('footstart: {}\n'.format(footstart))
        fo.write('footsmatch: {}\n'.format(footmat))
        #                   cricket data
        fo.write('cristadium: {}\n'.format(crista))
        fo.write('cricountry: {}\n'.format(cricou))
        fo.write('criregion: {}\n'.format(crireg))
        fo.write('critournament: {}\n'.format(critou))
        fo.write('cristart: {}\n'.format(cristart))
        fo.write('crismatch: {}\n'.format(crimat))
        #                   golf data
        fo.write('golfstadium: {}\n'.format(golfsta))
        fo.write('golfcountry: {}\n'.format(golfcou))
        fo.write('golfregion: {}\n'.format(golfreg))
        fo.write('golftournament: {}\n'.format(golftou))
        fo.write('golfstart: {}\n'.format(golfstart))
        fo.write('golfsmatch: {}\n'.format(golfmat))
        fo.close()
        ################################ write SPORTS clean data on a file
        #                   set the path for SPORT clean data
        psportsclean = home + homename + ptemp + 'wasportsclean.txt'
        fo = open(psportsclean, 'w')
        #                   football data
        fo.write('{}\n'.format(footsta))
        fo.write('{}\n'.format(footcou))
        fo.write('{}\n'.format(footreg))
        fo.write('{}\n'.format(foottou))
        fo.write('{}\n'.format(footstart))
        fo.write('{}\n'.format(footmat))
        #                   cricket data
        fo.write('{}\n'.format(crista))
        fo.write('{}\n'.format(cricou))
        fo.write('{}\n'.format(crireg))
        fo.write('{}\n'.format(critou))
        fo.write('{}\n'.format(cristart))
        fo.write('{}\n'.format(crimat))
        #                   golf data
        fo.write('{}\n'.format(golfsta))
        fo.write('{}\n'.format(golfcou))
        fo.write('{}\n'.format(golfreg))
        fo.write('{}\n'.format(golftou))
        fo.write('{}\n'.format(golfstart))
        fo.write('{}\n'.format(golfmat))
        fo.close()
        ################################ create the path for weatherapi logo
        #                   set the path for the Weatherapi logo
        pwblogo = home + homename + ptemp + 'walogo.txt'
        pi = '${image ' + home
        pi2 = homename
        pi3 = defconkyfol + 'walogo2'
        est = '.png -p '
        x = 10
        virg = ','
        y =10
        pf = ' -s 15x15}'
        fo = open(pwblogo, 'w')
        tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
        fo.write('{}\n'.format(tot))
        fo.close()
        ################################ create SPORTS section
        anum = 1
        sportsblock = 18
        rowfstadium = []
        rowfcountry = []
        rowfreg = []
        rowftou = []
        rowfstart = []
        rowfmatch = []
        rowcstadium = []
        rowccountry = []
        rowcreg = []
        rowctou = []
        rowcstart = []
        rowcmatch = []
        rowgstadium = []
        rowgcountry = []
        rowgreg = []
        rowgtou = []
        rowgstart = []
        rowgmatch = []
        rowcolor = '${color}'
        rowcolor1 = '${color1}'
        rowcolor2 = '${color2}'
        rowcolor3 = '${color3}'
        rowcolor4 = '${color4}'
        rowcolor5 = '${color5}'
        rowcolor6 = '${color6}'
        rowcolor9 = '${color9}'
        rowfont6 = "${font URW Gothic L:size=6}"
        rowfont7 = "${font URW Gothic L:size=7}"
        rowfont8 = "${font URW Gothic L:size=8}"
        rowheadinga = rowcolor3 + '${alignc}----------------- SPORTS ALERTS -----------------' + tot
        rowheadingf = rowcolor1 + '             ------- Football'
        rowheadingc = rowcolor1 + '             ------- Cricket'
        rowheadingg = rowcolor1 + '             ------- Golf'
        for i in range(0, anum):
                # block control
            rowcount = 1 + sportsblock * i
            #                 write conky syntax for sports
            rowfstadium.append(rowcolor2 + rowfont7 + "Stadium: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowfcountry.append(rowcolor2 + "Country: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowfreg.append(rowcolor2 + "Region: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1    
            rowftou.append(rowcolor2 + "Tournament: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowfstart.append(rowcolor2 + "Start: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowfmatch.append(rowcolor2 + "Match: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowcstadium.append(rowcolor2 + rowfont7 + "Stadium: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowccountry.append(rowcolor2 + "Country: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowcreg.append(rowcolor2 + "Region: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1    
            rowctou.append(rowcolor2 + "Tournament: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowcstart.append(rowcolor2 + "Start: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowcmatch.append(rowcolor2 + "Match: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowgstadium.append(rowcolor2 + rowfont7 + "Stadium: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowgcountry.append(rowcolor2 + "Country: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowgreg.append(rowcolor2 + "Region: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1   
            rowgtou.append(rowcolor2 + "Tournament: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowgstart.append(rowcolor2 + "Start: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
            rowcount = rowcount + 1
            rowgmatch.append(rowcolor2 + "Match: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + psportsclean + "}")
        #set the path for SPORT conky syntax
        psportsc = home + homename + ptemp + 'sportsconky.txt'
        fo = open(psportsc, 'w')
        fo.write('{}\n'.format(rowheadinga))
        for i in range(0, anum):
            fo.write('{}\n'.format(rowheadingf))
            fo.write('{}\n'.format(rowfstadium[i]))
            fo.write('{}\n'.format(rowfcountry[i]))
            fo.write('{}\n'.format(rowfreg[i]))
            fo.write('{}\n'.format(rowftou[i]))
            fo.write('{}\n'.format(rowfstart[i]))
            fo.write('{}\n'.format(rowfmatch[i]))
            fo.write('{}\n'.format(rowheadingc))
            fo.write('{}\n'.format(rowcstadium[i]))
            fo.write('{}\n'.format(rowccountry[i]))
            fo.write('{}\n'.format(rowcreg[i]))
            fo.write('{}\n'.format(rowctou[i]))
            fo.write('{}\n'.format(rowcstart[i]))
            fo.write('{}\n'.format(rowcmatch[i]))
            fo.write('{}\n'.format(rowheadingg))
            fo.write('{}\n'.format(rowgstadium[i]))
            fo.write('{}\n'.format(rowgcountry[i]))
            fo.write('{}\n'.format(rowgreg[i]))
            fo.write('{}\n'.format(rowgtou[i]))
            fo.write('{}\n'.format(rowgstart[i]))
            fo.write('{}\n'.format(rowgmatch[i]))
        fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed