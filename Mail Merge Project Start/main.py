with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file1:
    names = file1.readlines()
    for name in names:
        name = name.strip("\n")
        print(name)
        with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file2:
            invitation = file2.read()
            invitation = invitation.replace("[name]", name)
            # print(invitation)
            with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as invite:
                invite.write(invitation)




