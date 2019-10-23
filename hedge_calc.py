# inputs
hedge_required = 500000
existing_hedge = 100000
VIF = 400000
tolerance = 250000

# outputs
hedge_to_place = None

# If the hedge required is greater than the VIF and the VIF the existing hedge is equal to or greater than 250000
if (hedge_required >= VIF) and (VIF - existing_hedge >= tolerance):
    # Then the hedge to place is equal to the VIF - existing hedge
    hedge_to_place = VIF - existing_hedge
    print(f"Hedge to place: {hedge_to_place}")
# Else if the hedge required is less than the VIF and the hedge required - the existing hedge is equal to or greater
# than 250000
elif (hedge_required < VIF) and (hedge_required - existing_hedge >= tolerance):
    # Then the hedge to place is equal to the hedge required - existing hedge
    hedge_to_place = (hedge_required - existing_hedge)
    print(f"Hedge_to_place: {hedge_to_place}")

# Otherwise don't place a hedge
else:
    print("No hedge required")