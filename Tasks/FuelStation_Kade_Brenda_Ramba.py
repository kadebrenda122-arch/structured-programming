# BRENDA KADE RAMBA
# REG_NO:  S26B38/050

def load_litres(filename):
    litres = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                   litres.append(int(line))
    except FileNotFoundError:
        print("sorry, dataset not found:", {filename}) 
    return litres                              

def total_sales(litres):
    """Returns the total litres sold, and returns 0 if the list is empty."""
    if len(litres) == 0:
       return 0
    total = 0
    for value in litres:
       total = total + value

    return total

def quiet_days(litres, limit = 400):
    count = 0 
    for amount in litres:
       if amount < limit:
          count += 1
    return count
 

def main():
    filename = "litres.txt"
    litres = load_litres(filename)

    if len(litres) == 0:
     return None
    
    days= len(litres)
    total= total_sales(litres)
    average = total / days
    busiest_day= max(litres)
    quiet = quiet_days(litres, 400)
   
    report = (
        "===== FUEL STATION SUMMMARY =====\n"
        f"Days recorded: {days}\n"
        f"Total litres: {total}\n"
        f"Average per day: {average:1f}\n"
        f"Busiest day: {busiest_day}litres\n"
        f"Quiet days(<400): {quiet}\n"
     )
    print(report)

    with open("Station_report.txt",  "w") as file:
      file.write(report)
    print("Report saved to station_report.txt")  

main()
 

     

       
        


     

       
        

