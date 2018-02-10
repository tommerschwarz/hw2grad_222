import sys

def opt(s1, s2):
    a = len(s1) + 1 #rows
    b = len(s2) + 1 #cols
    max_val = 0
    x = [[None]*(b) for i in range(a)]
    bt = [[0]*(b) for i in range(a)]
    
    for i in range(0,a):
        x[i][0] = i*(0)
    for j in range(0,b):
        x[0][j] = j*(0)

    for i in range(1, a):
        for j in range(1, b):
            t = PAM250[s1[i-1]][s2[j-1]]
            arr = [0, x[i-1][j] - 5, x[i-1][j-1] + t, x[i][j-1] - 5]
            x[i][j] = max(arr)
            bt[i][j] = arr.index(x[i][j])
            if (x[i][j] > max_val):
                max_val = x[i][j]
                max_i = i
                max_j = j

    i = max_i
    j = max_j

    
    seq1 = s1[:i]
    seq2 = s2[:j]

    while ((bt[i][j] != 0) & (i*j > 0)):
        if (bt[i][j] == 2):
            bt[i][j] = 88
            i = i - 1
            j = j - 1
        elif (bt[i][j] == 1):
            bt[i][j] = 88
            i = i - 1
        elif (bt[i][j] == 3):
            bt[i][j] = 88
            j = j - 1

    seq1 = seq1[i:]
    seq2 = seq2[j:]

    '''while ((x[i][j] != 0) & (i*j > 0)):
        if (s1[i-1] == s2[j-1]):
            i = i - 1
            j = j - 1
        elif (x[i-1][j] > x[i][j-1]):
            seq1 = s1[i-1] + seq1
            i = i - 1
        else:
            seq2 = s2[j-1] + seq2
            j = j - 1 '''
    print(max_val)
    print(seq1)
    print(seq2)
    return max_val



PAM250 = {
'A': {'A': 2,  'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
'C': {'A': -2, 'C': 12, 'D': -5, 'E':-5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
'D': {'A': 0,  'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'E': {'A': 0,  'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'F': {'A': -3, 'C': -4, 'D': -6, 'E':-5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
'G': {'A': 1,  'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
'I': {'A': -1, 'C': -2, 'D': -2, 'E':-2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
'L': {'A': -2, 'C': -6, 'D': -4, 'E':-3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
'M': {'A': -1, 'C': -5, 'D': -3, 'E':-2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
'N': {'A': 0,  'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
'P': {'A': 1,  'C': -3, 'D': -1, 'E':-1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
'Q': {'A': 0,  'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
'R': {'A': -2, 'C': -4, 'D': -1, 'E':-1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
'S': {'A': 1,  'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
'T': {'A': 1,  'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
'V': {'A': 0,  'C': -2, 'D': -2, 'E':-2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
'W': {'A': -6, 'C': -8, 'D': -7, 'E':-7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L':  -2, 'M':  -4, 'N': -4, 'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T':  -5, 'V':  -6, 'W': 17, 'Y': 0},
'Y': {'A': -3, 'C': 0, 'D': -4, 'E':-4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L':  -1, 'M':  -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T':  -3, 'V':  -2, 'W': 0, 'Y': 10}}


s1 = 'IKVRDPASCCIPGSENMHDVGSWEFRHWLEDYYWMNQYMGHAEEFLINAYLYSIHRVCKESERIAQLRHMAYILQDQHADVPQIWGEIHGGEINCYFNRSQMTITRLDYNAGCANCIHTPDLGCHFMPPQPMWPGCRLIDTHVTRWHFNDTDTRNCATYPEIRILDPVRSNEFCAFIRQCVQKVSVNAPNCSKRHWSWGVNHCPFTKAYHMFFCVMPPSHPCCCVCKHHIKKAERCCHVNYKIPYEMHELYFCCIPNTEYDGLKVTKLEMHRQQKTRNYGFVCLFGTLENFCHMGLPYFWQDCFVRAIKLFQHHWASQVREQDHSPITVKNCFQWLNTKDDQSDETQPEWEPNKINKSDLQKVDMMIGWNGDIHVHGIQAQCHTSIDRHIYHIWYTKCVVITGYAPACVWWYYIMRQYQKVWCRSNSYNQGCLFAHPQEKHMLRRLCNHSLIEWAMQECIIAFFHEQKIRGIISDYSYFDGLAPYYMKKTWIQTITDPKEWTMGEDPWGLFLRSRNAYTHQKYLGKTSGFGIRRADHAWECAKRNYLVEKPFHNGTIRCPNARNHRLQGCGGWDTPFGDYNQEPSVTSYYLWTFDRRVDLCYRWPITKQLFDSATFWHILSQNQISVHHESEPYKYAAALPEPCFSELFCFQENQHYVKDKPFHLWPLSAGTLHHYNPGKYSDHMDWYMHRAHFEQSADMEFVLWAFVCTIRSGYQTPMGGQRCMWTRHSQLMTVPTMGYLPMSPAQYSCPDSIKPDWGRLCAIYCQQLVFATVNIRYHSFVGKQYCIIQQPDKRPNDYEHRMMQKPLSHDVQSADKGICHIDRQCKKHVWQQPFCKLNEHRIHTQLIARHVVFFMAWACSRWDSGWEALTVYCQGVSMKFDAVWKTHRHAVTDIGIERF'
s2 = 'VACTIQSHSNSLQSETIDRWYVCRHMLCRMTGISTASYWRVISKSRTAQEWFLECIHTQYWMYHEPPGHMLFRRNMKYLKMLFACPWVESEHHRCRRDIEMDVHNGWMLCGVRLWMAESEKPNPVGQAFVNYCATAYCLCPWIYLYRMCFYREIRIPGAFYHYCPGFLEPEVIGLENKTPVTVPETTNTDFNFYMWRWDFTVEIISHLTCKWAIEKRGCGCWHKAEKWGGQSNRDPILGPSEMHELYFCCIPNTEYDGTKNEMHRQQKTRNKGFVCLFIATIIWTVFDAKLENFIHMGLPYFRPWKIEFCQHHCASQVREQDHSPITVWNCFQKCNTKDDQSDETQPEWEPNKINKSDLQKVDMMYGWNGDIHVHGIQAQCHTSIDRHIYHIWKEKCIRRQNSYNQGCNFAYQNQPQEKHMERVQAMWLRMCAMTLCNTSLIEWAMQECIIAFFQKISMISYFDGLAPYYMWGLFLSSSPLDADIHAWECMKRNMLVEVNCPCIWPFRNGTIRHRLQGIGGWDTPGDYNLELNAKNIAMDSVTSYYLPTFDRRWDLCIRWPITKQLMDSATFWHSVHGRPVDIERTLSEPNLPEPCFSELFCIQETHHNYGVTWLLFGMTKLYDDDMNLVFYQHPVRHNQEPRPNLSARYYNRPIRGKPKTFWQYDMHAVGRKDTMYNNGWFQGSSSFRILSCFHHQPSYFEWIVSSHHAWYYLCIKNDLGDHTDLGDECPIPHEQWCPFDFSWKAQFYHCTYSRLMSHYTWSSDFTTWVCPLAHFFKTHHTHESNKPGQSPECCLTFKCCCLQWSKETFQPMVRGMNHLSCLWMDIRVVRVTQMSYWDFGIAMFEHKP'
#s1 = 'MEANLYPRTEINSTRING'
#s2 = 'PLEASANTLYEINSTEIN'
print(opt(s1, s2))
