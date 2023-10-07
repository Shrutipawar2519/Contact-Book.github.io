contact={}

while True:
    ch=int(input('\n please enter your choice:\n1.show all contact .\t\t2.add contact \n3.update contact \t\t4. search contact.\n5.exit'))
    if ch==1:
        def showdata():
             if len(contact)==0:
                 print('no contact exit!!')
                 print('contact list is empty')
             else:
                 for m,n in contact.items():
                   print(n,m)
             return 'thankyou!!'
        print(showdata())
    elif ch==2:
        def adddata():
            name=input('please enter contact name:')
            mono=input('please enter mobile no to save:')
            found=False
            for m in contact.keys():
                if mono==m:
                    found=True
            if found:
                print('mono',m,'already exists with name',contact[m])
                print('please retry')
            else:      
                contact[mono]=name
                print()
                return 'contact added!'
        print(adddata())
       
    elif ch==3:
        def update():
            mono=input('enter mono to update:')
            found=False
            for m in contact.keys():
                if mono==m:
                    found=True
            if found:
                name=input('enter update name:')
                contact.update({mono:name})
                print()
                print('contact updated!')
            else:
                print('contact not found')
        update()
    elif ch==4:
        def search():
            mono=input('enter mono to search:')
            found=False
            for m in contact.keys():
                if mono==m:
                    found=True
            if found:
                 print('mono:',m,'name:',contact[m])
                 print('thank you!!')
            else:
                print('contact not found')
                print( 'thank you!!' )
        search()
    elif ch==5:
        print('Exit!')
        print('thank you!!')      
        break
    else:
        print('invalid choice')
    
        
