import mip

# Parameters

# Capacity of each farm per quarter
c = [[700.0,1500.0,700.0,0.0,0.0,700.0,1500.0,0.0],
     [1350.0,0.0,450.0,0.0,1350.0,0.0,450.0,0.0],
     [0.0,1500.0,1500.0,0.0,0.0,1500.0,1500.0,0.0],
     [820.0,1560.0,820.0,0.0,820.0,1560.0,820.0,0.0],
     [0.0,680.0,1080.0,0.0,0.0,680.0,1080.0,0.0]] # t
# Unit purchase price
p = [0.20,0.18,0.19,0.21,0.23] # $/t
# Unit storage cost
s = [0.002,0.012,0.007,0.011,0.015] # $/t
# Unit percentage of dry matter
d = [15.0,28.0,35.0,37.0,42.0] # %/t

dry_matter_range = [20.0,40.0] # %
energy_yield = 421.6 # kWh
market_price = 0.28 # $/t
state_regulations = 1950000.0 # kWh
total_silo_capacity = 500.0 # t

def solve_productmix(c,p,s,d,dry_matter_range,energy_yield,market_price,state_regulations,total_silo_capacity):
  # Farms
  F = range(len(c))
  # Quarters
  Q = range(len(c[0]))

  m = mip.Model()

  # The default value of the variable lower bound (lb) is 0.0, so, 
  # it is not necessary to enter variable constraints greater than or equal to 0.0.

  # Number of tons purchased
  x = {(i,j) : m.add_var(name = "x{}{}".format(str(i),str(j)),ub = c[i][j]) for i in F for j in Q}
  # Number of tons stored at the end of the quarter (note that there is an extra quarter for silo initialization)
  y = {(i,j) : m.add_var(name = "y{}{}".format(str(i),str(j))) for i in F for j in range(len(c[0])+1)}
  # Number of tons burned = x[i,j]+y[i,j]-y[i,j+1]

  # Constraints 
  for i in F:
    # Silo initialization
    m += y[i,0] == 0.0
    for j in Q:
      # Burned material must be greater than or equal to 0
      m += x[i,j]+y[i,j]-y[i,j+1] >= 0.0

  for j in Q:
    # The dry matter percentage must be between 20 and 40
    m += mip.xsum(d[i]*(x[i,j]+y[i,j]-y[i,j+1]) for i in F) >= dry_matter_range[0]*mip.xsum(x[i,j]+y[i,j]-y[i,j+1] for i in F)
    m += mip.xsum(d[i]*(x[i,j]+y[i,j]-y[i,j+1]) for i in F) <= dry_matter_range[1]*mip.xsum(x[i,j]+y[i,j]-y[i,j+1] for i in F)
    # Stocks per quarter shall not exceed 500 tons
    m += mip.xsum(y[i,j+1] for i in F) <= total_silo_capacity
    # State regulations must be met in each quarter: no more energy than 1950 MWh must be produced
    m += energy_yield*mip.xsum(x[i,j]+y[i,j]-y[i,j+1] for i in F) <= state_regulations

  # Objective Function
  m.objective = mip.maximize(energy_yield*market_price*mip.xsum(x[i,j]+y[i,j]-y[i,j+1] for i in F for j in Q)-mip.xsum(p[i]*x[i,j]+s[i]*y[i,j+1] for i in F for j in Q))
  m.optimize()

  return (m,[["%.2f" % x[i,j].x for j in Q] for i in F],[["%.2f" % y[i,j+1].x for j in Q] for i in F],m.objective_value)

_, solution_x, solution_y, objective_value = solve_productmix(c,p,s,d,dry_matter_range,energy_yield,market_price,state_regulations,total_silo_capacity)

print("Tons of material to be purchased (t/quarter) (variable x):")
for line in solution_x:
  print("\t".join(map(str,line)))
print("\n")
print("Tons of material in the silo (t/quarter) (variable y):")
for line in solution_y:
  print("\t".join(map(str,line)))
print("\n")  
print("Total profit ($) (objective value): ",objective_value)