def how_eligible(essay):
    ans = 0
    if len(essay) <= 140:
        if '!' in essay:
            ans = ans + 1
        if ',' in essay:
            ans = ans + 1
        if '?' in essay:
            ans = ans + 1
        if '"' in essay:
            ans = ans + 1
        print(ans)
how_eligible('This? "Yes." No, not really')
