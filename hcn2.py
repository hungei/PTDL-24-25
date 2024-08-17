import Rectangle as HCN
menu_options={
    1:'thêm hcn',
    2:'HIển thị danh sách',
    3:'tính tổng diện tích',
    4:'tính tổng chu vi',
    5:'hiện thị chu vi nhỏ nhất',
    'others':'thoát ctrinh'
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])
#khai báo biến để lưu trữ HCN
dsHCN=[]
while(True):
    print_menu()
    userchoice=''
    try:
        userchoice=int(input('nhập tùy chọn: '))
    except:
        print('nhập sai mời nhập lại')
        continue

    if userchoice == 1:
        cr=float(input('nhập cr: '))
        cd=float(input('nhập cd: '))
        hcn=HCN.Rectangle(cr,cd)
        dsHCN.append(hcn)

    elif userchoice==2:
        for item in dsHCN:
            item.hienthi()
        
    elif userchoice==3:
        DT=0
        for item in dsHCN:
            DT+=item.dientich()
        print('tổng diện tích',{DT})
            
    elif userchoice==4:
        CV=0
        for item in dsHCN:
            CV+=item.chuvi()
        print('tổng chu vi: ',{CV})
    elif userchoice==5:
        if dsHCN.count==0:
            print('ds rỗng')
        else:
            chuvinn=dsHCN[0].chuvi()
            for item in dsHCN:
                if chuvinn > item.chuvi():
                    chuvinn=item.chuvi()
            for item in dsHCN:
                if item.chuvi()==chuvinn:
                    item.hienthi()
    else:
        print('BYE')
        break

        

