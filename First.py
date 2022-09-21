"""
while True:
    command = input()
    if command == 'exit':
        break
    if command == 'transcribe':
        print('I transcribed that')
    if command == 'reverse':
        pass
    if command == 'complement':
        pass
    if command == 'reverse complement':
        pass

# try to transcribe
strok = 'AtGc'
d_transcribe = {'A': 'U', 'a': 'u', 'T': 'A', 't': 'a',
                'G': "C", 'g': 'c', 'C': 'G', 'c': 'g'}
d_complement = {'A': 'T', 'a': 'u', 'T': 'A', 't': 'a',
                'G': "C", 'g': 'c', 'C': 'G', 'c': 'g'}
for i in strok:
    print(d_transcribe[i], end='')
# try to reverse
for a in range(1, len(strok)+1):
    print(strok[-a], end='')
"""
commands = ['exit', 'transcribe', 'reverse', 'complement', 'reverse complement']
print('Enter command:')
command = input()
if command not in commands:
    print('I do not know what you want')
elif command == 'exit':
    print('Mission completed')
else:
    while True:
        print('Enter sequence:')
        strok = input()

        def f_complement(sequence):
            for i in sequence:
                print(d_complement[i], end='')


        def f_reverse(sequence):
            for a in range(1, len(sequence) + 1):
                print(sequence[-a], end='')


        def f_rev_complement(sequence):
            spis = []
            for i in range(1, len(sequence) + 1):
                spis += [sequence[-i]]
            for a in spis:
                print(d_complement[a], end='')


        op = 0
        # check RNA or DNA
        # what we can do with RNA
        if 'U' in strok or 'u' in strok:
            # set a dictionary for a complementary sequence
            d_complement = {'A': 'U', 'a': 'u', 'U': 'A', 'u': 'a',
                            'G': "C", 'g': 'c', 'C': 'G', 'c': 'g'}
            # check if there is "T" or other characters
            for i in strok:
                if i not in d_complement:
                    op += 1
            if op > 0:
                print("Invalid characters, please try again")
                continue
            if command == 'transcribe':
                print('RNA sequence is not transcribed')
                continue
            elif command == 'complement':
                f_complement(strok)
            elif command == 'reverse':
                f_reverse(strok)
            elif command == 'reverse complement':
                f_rev_complement(strok)

        else:
            d_complement = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a',
                            'G': "C", 'g': 'c', 'C': 'G', 'c': 'g'}
            d_transcribe = {'A': 'U', 'a': 'u', 'T': 'A', 't': 'a',
                            'G': "C", 'g': 'c', 'C': 'G', 'c': 'g'}
            # check if there is other characters
            for i in strok:
                if i not in d_complement:
                    op += 1
            if op > 0:
                print("Invalid characters, please try again")
                continue
            if command == 'complement':
                f_complement(strok)
            elif command == 'transcribe':
                for i in strok:
                    print(d_transcribe[i], end='')
            elif command == 'reverse':
                f_reverse(strok)
            elif command == 'reverse complement':
                f_rev_complement(strok)

        print('\nEnter command:')
        command = input()
        if command == 'exit':
            print('Mission completed')
            break
