from nltkutil import Chat, reflections

pairs = [
    [
        r"hello|hi|hey(.*)",
        ["Bot : Hello, I am the Virtual Assistant for Dr.Ambedkar Institute of Technology, how can I help you today ? \n", ]
    ],
    [
        r"(.*)affiliated(.*)VTU",
        ["Bot : Dr.Ambedkar Institute of Technology is an autonomous college affliaited to VTU \n", ]
    ],
    [
        r"(.*)college(.*)location",
        ["Bot : BDA, Outer Ring Road, Near, Gnana Bharathi, Bengaluru. Please use the link below https://goo.gl/maps/NhV7MKqan755W9jbA \n", ]
    ],
[
        r"(.*)location(.*)college",
        ["Bot : BDA, Outer Ring Road, Near, Gnana Bharathi, Bengaluru. Please use the link below https://goo.gl/maps/NhV7MKqan755W9jbA \n", ]
    ],
    [
        r"(.*)branches|courses(.*)",
        ["Bot :The branches offered in our college are ISE, CSE, MECH, CIV, ECE, EE, ME, IEM and TC \n", ]
    ],
    [
        r"(.*)principal(.*)",
        ["Bot : The name of the Principal is Dr.Nanjundaswamy \n", ]
    ],
]
