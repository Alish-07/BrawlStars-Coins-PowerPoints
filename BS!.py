import requests
player_tag = 'gvoppuu'
totalno_of_brawlers = 65
no_of_brawlers = 0
totalpower = 0
totalcoin = 0
totalspcost = 0
spcost = 0
totalgadgetcost = 0
gdcost = 0
totalgearcost = 0
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk2NDMzODZiLTI1YjgtNDQ2Zi04NDQxLTg0ZGFkYjJjNmEyNiIsImlhdCI6MTY3ODE3ODQ1MCwic3ViIjoiZGV2ZWxvcGVyL2M4Y2M4YzQ5LWZhOGUtYThmNC0zZTZmLTNlNDg4MjEwYmIyZCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjcuMzQuMjIuMTk1Il0sInR5cGUiOiJjbGllbnQifV19.ajx05oXDTcFHtACiw9RsoX8f-CzRZ4s82T8Qbl5beeNM74kTMOK6l6P2DkN_5ocT8fGaOOfn_Gcrt_TT2DeBQA'

url = f'https://api.brawlstars.com/v1/players/%23{player_tag}'

headers = {
    'Accept': 'application/json',
    'authorization': f'Bearer {api_key}'
}

response = requests.get(url,headers=headers)

if response.status_code == 200:
    json_data = response.json()
    brawlers = json_data['brawlers']
    for brawler in brawlers:
        # For number of brawlers owned
        no_of_brawlers = no_of_brawlers + 1
       
        # For Power level
        power = brawler['power']
        totalpower = power + totalpower
        pp =3740 - ( 10 * (4^(power-2) - 1))
        cc =7765 - (5 * (4^(power-2) - 1))
        totalpower = totalpower + pp
        totalcoin = totalcoin + cc
        
        # For SP cost
        sp = brawler['starPowers']
        if sp == 0:
            spcost = 2000 + 2000
        elif sp == 1:
            spcost = 2000
        elif sp == 2:
            spcost == 0
        totalspcost = spcost + totalspcost

        # For gadget cost
        gd = brawler['gadgets']
        if gd == 0:
            gdcost = 2000 + 2000
        elif gd == 1:
            gdcost = 2000
        elif gdcost == 2:
            gdcost == 0
        totalgadgetcost = gdcost + totalgadgetcost

        # For gear cost

elif response.status_code == 404:
    json_data = response.json()
    print('Error retrieving brawlers:', response.text)
else:
    print("Error")

# For locked brawlers Cost
locked_brawlers = totalno_of_brawlers - no_of_brawlers
addcoins = (locked_brawlers * 7765) + 2000 + 2000 + 1000 + 1000
addpp = (locked_brawlers * 3740)

# Final Cost
final_coin_cost = totalcoin + totalgadgetcost + totalspcost + totalgearcost + addcoins
final_pp_cost = totalpower + addpp

# Display
print(f"No of total brawlers unlocked = {no_of_brawlers}")
print(f"Total Power points required for all power 11 = {totalpower}")
print(f"Total Coins required for all power 11 = {totalcoin}")
print(f"Total Coins required for all star power = {totalspcost}")
print(f"Total Coins required for all Gadgets = {totalgadgetcost}")

print(f"Final Coin cost to fully max account = {final_coin_cost}")
print(f"Final Power Point cost to fully max account = {final_pp_cost}")

    


