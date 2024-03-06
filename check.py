def check():
    # randomly select 0 or 1
    import random
    result = random.choice([0, 1])
    if result == 0:
        return True
    else:
        sys.exit(1)

if __name__ == "__main__":
    check()
