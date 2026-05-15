# Exercise - 11: Hours, Minutes, Seconds
def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds < 0:
        return -1  # Invalid input

    days = totalSeconds // 86400
    remainder = totalSeconds % 86400

    hours = remainder // 3600
    remainder %= 3600

    minutes = remainder // 60
    seconds = remainder % 60

    result = ""
    if days > 0:
        result += f"{days}d"
    if hours > 0:
        result += f"{hours}h"
    if minutes > 0:
        result += f"{minutes}m"
    if seconds > 0 or result == "":
        result += f"{seconds}s"

    return result

# Example usage
totalSeconds = int(input("Enter total seconds: "))
print(getHoursMinutesSeconds(totalSeconds))
