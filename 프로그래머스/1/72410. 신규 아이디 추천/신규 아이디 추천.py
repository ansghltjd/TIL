def solution(new_id):
    new_id = new_id.lower()
    a=''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ('-','_','.'):
            a+=i
    while '..' in a:        
        a=a.replace('..','.')
        
    if a.startswith('.') : 
        a=a[1:]
    if a.endswith('.') : 
        a=a[:-1]
        
    if a == '':
        a += 'a'
    if len(a)>=16:
        a = a[:15]
        if a.endswith('.') : 
            a=a[:-1]
    
    while len(a)<3:
        a+=a[-1]
        
    return a