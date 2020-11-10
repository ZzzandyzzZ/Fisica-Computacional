function laplace(f1,f2,f3,f4,a,b,h,epsilon)

n=fix(a/h)+1;
m=fix(b/h)+1;
m
n
pp=(a*(feval(f1,0)+feval(f2,0))+b*(feval(f3,0)+feval(f4,0)))/(2*a+2*b);
U=pp*ones(n,m)*0.9;
%condiciones a la frontera
U(1,1:m)=feval(f3,0:h:(m-1)*h)';
size(0:h:(m-1)*h)
U(n,1:m)=feval(f4,0:h:(m-1)*h)';
U(1:n,1)=feval(f1,0:h:(n-1)*h);
U(1:n,m)=feval(f2,0:h:(n-1)*h);
U(1,1)=(U(1,2)+U(2,1))/2;
U(1,m)=(U(1,m-1)+U(2,m))/2;
U(n,1)=(U(n-1,1)+U(n,2))/2;
U(n,m)=(U(n-1,m)+U(n,m-1))/2;
% calculo de omega
w=4/(2+sqrt(4-(cos(pi/(n-1))+cos(pi/(m-1)))^2));
% inicio de los calculos
rmax=1;
while(rmax>epsilon)
  rmax=0;
  for i=2:n-1
    for j=2:m-1
      rij=(U(i,j+1)+U(i,j-1)+U(i+1,j)+U(i-1,j)-4*U(i,j))/4;
      U(i,j)=U(i,j)+w*rij;
      if rmax<=abs(rij)
        rmax=abs(rij);
      endif
    endfor
  endfor
endwhile
size(U)
surfc(U);
U
%U(1)