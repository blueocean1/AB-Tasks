def enough(cap, on, wait):
    if cap >= on + wait:
        print("He can fit all {} passangers!".format(wait))
        return 0
    else:
        print("Ha can't fit {} out of {} waiting!".format((on+wait)-cap, wait))
        return (on + wait) - cap