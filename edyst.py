from itertools import combinations,permutations
t=int(input())
while(t>0):
    t-=1
    ip_str=input()
    ip_lst=list(map(str,input().split()))[1:]
    def final(dict1,ip_str):
        a=ip_str
        key_list=list(dict1.keys())
        print("key list=",key_list,"ended")
        val_list=list(dict1.values())
        re_list=[]
        my_count=0
        for sub in key_list:
            ip_str=a
            real_count=0
            sub=list(sub)
            print("sub=",sub)
            per_list=[]
            for word in sub:
                
                print("word=",word)
                t=list(permutations(word,len(word)))
                per_list+=t
            p=''
            for i in range(len(per_list)):
                per_list[i]=p.join(per_list[i])
            for word1 in per_list:
                if(word1 in ip_str):
                    print("yes=",word1)
                    b=ip_str.index(word1)
                    c=len(word1)+b
                    ip_str=ip_str[ : b]+ip_str[c: ]
                    real_count+=1
            if(real_count==len(sub)):
                my_count+=1
        print("final=",my_count)
        return my_count
            
    def check(dict1,ip_str):
        key_list=list(dict1.keys())
        val_list=list(dict1.values())
        re_dict={}
        result=0
        count1=0
        for each in (dict1.values()):
            count=0
            for al in ip_str:
                if al in each:
                    count+=1
            if((count==len(each)) and (len(each)==len(ip_str))):
                #print("each=",each)
                a=key_list[val_list.index(each)]
                re_dict[a]=each
                count1+=1
        if(count1>0):
            result+=final(re_dict,ip_str)
        print("check=",result)
        return result
    def joining(lst,ip_str):
        result=0
        s=""
        re_dict={}
        for sub_list in lst:
            str1=s.join(sub_list)
            re_dict[sub_list]=str1
        #print(re_dict)
        result+=check(re_dict,ip_str)
        print("joining",result)
        return result

    count=0
    for i in range(4,len(ip_lst)):
        lst=combinations(ip_lst,i)
        count+=joining(lst,ip_str)
    print(count)
