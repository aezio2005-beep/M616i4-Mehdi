print("Salam,radiotexnika!")
rsrp_dbm = -95
print(f"{rsrp_dbm} dBm = {p_mw:.2e} mW")
values = [-85,-97,-110,-118]
for v in values:
        if v <-105:
                print(v, "dBm -zəif siqnal")
        else:
                print(v, "dBm - normal")