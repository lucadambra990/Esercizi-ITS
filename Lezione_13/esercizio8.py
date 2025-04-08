def vowelsCounter(s:str) ->int:
    #if s is a empty string
    if len(s)==0:
        return 0
    if s[0].lower() in ["a","e","i","o","u"]:
        return 1 + vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])

print(f"La stringa contiene {vowelsCounter("ciao")} vocali")