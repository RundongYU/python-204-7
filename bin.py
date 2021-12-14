if Pxy is True:
    Qxy = True
elif (Rxy | (Pxy & Pxy)) is True:
    Axy = True
elif ((Rxy & Txy) | (Pxy & Pxy & Txy) | (Pxy & Txy) & Txy) is True:
    BQxy = True
elif ((Rxy & Txy) | (Pxy & Pxy & Txy) | (Pxy & Txy) & Txy | Cxy) is True:
    FQxy = True
elif ((Rxy & Txy) | (Pxy & Pxy & Txy) | (Cxy & Txy)) is True:
    PQxy = True
elif (Pxy & Fxy) is True:
    Qxy = Qxy & Qxy
    Qxy = True
