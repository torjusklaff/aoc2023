
if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='AoC run stuff')
    parser.add_argument('-d', default=[], nargs='+', required=True, type=int)
    args = parser.parse_args()
    days = args.d
    for day in days:
        exec("from d{} import day{}".format(day, day))
        exec("day{}.main()".format(day))