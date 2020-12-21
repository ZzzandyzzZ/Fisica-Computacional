function f = auto2(  )
    hold off;
    c=100;
    axis([0 c 0 c])
    a=0;
    b=0;
    for i=1:c
        hold on;
        a(i)=round(rand);
    end
    j=c;
    while j>0
        for i=1:c
            l=i-1;
            r=i+1;
            if l<1
                l=c;
            end
            if r>c
                r=1;
            end
            al=a(l);
            ar=a(r);
            if al==1 && a(i)==1 && ar==1
                b(i)=0;
            end
            if al==1 && a(i)==1 && ar==0
                b(i)=1;
            end
            if al==1 && a(i)==0 && ar==1
                b(i)=1;
            end
            if al==1 && a(i)==0 && ar==0
                b(i)=0;
            end
            if al==0 && a(i)==1 && ar==1
                b(i)=0;
            end
            if al==0 && a(i)==1 && ar==0
                b(i)=1;
            end
            if al==0 && a(i)==0 && ar==1
                b(i)=1;
            end
            if al==0 && a(i)==0 && ar==0
                b(i)=1;
            end
        end
        for k=1:c
            if b(k)==1
                plot(k,j,'.k');
            end
        end
        a=b;
        j=j-1;
    end
end
 