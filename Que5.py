def f(list1, list2):
    common = list(set(list1) & set(list2))
    not_common = list(set(list1) ^ set(list2))
    print(common)
    print(not_common)
    

mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]
f(mainstream, must_watch)

