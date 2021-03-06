import math, decimal, datetime

dec = decimal.Decimal


def position(now=None):
    if now is None:
        now = datetime.datetime.now()

    diff = now - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)


def phase(pos):
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}[int(index) & 7]


def main():
    pos = position()
    phasename = phase(pos)
    return phasename


if __name__ == "__main__":
    main()
