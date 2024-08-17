import Rectangle as HCN
menu_options={
    1:'đọc file dữ liệu từ file input.db',
    2:'Thêm mới HCN',
    3:'HIển thị danh sách',
    4:'Lưu ds HCN xuống file demo4output.db',
    'others':'thoát ctrinh'
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])
while(True):
    print_menu()
    chon=''
    try:
        chon= int(input("mời chọn chức năng"))
    except:
        print('lỗi?, mời nhập lại')
        continue
    if chon==1:
        fr = open('input.txt',mode='r',encoding='utf-8')
        dsHCN=[]
        for line in fr:
            stripLine= line.strip('\n')
            ds = stripLine.split(',')
            cr =float(ds[0])
            cd=float(ds[1])
            hcn=HCN.Rectangle(cr,cd)
            dsHCN.append(hcn)
        fr.close()
    
    elif chon==2:
        cr=float(input('nhập cr: '))
        cd=float(input('nhập cd: '))
        hcn=HCN.Rectangle(cr,cd)
        dsHCN.append(hcn)
    
    elif chon ==3:
        if dsHCN.count==0:
            print('danh sách rỗng')
        else: 
            for item in dsHCN:
                item.hienthi()
    
    elif chon==4:
        fw=open('demo4output.db',mode='w',encoding='utf-8')
        for item in dsHCN:
            fw.write(f"rong:{self.width},dai:{self.lenght},chu vi:{self.chuvi()},dien tich:{self.dientich()}\n")
        fw.close()
    else:
        print('BYE')
        break

