function U=laplace(f1,f2,f3,f4,a,b,h,epsilon)
%f1,f2,f3,f4 son funciones en el frontera
% f1=u(x,0)=u(i,1) -> Abajo
% f2=u(x,b)=u(i,m) -> Arriba
% f3=u(0,y)=u(1,j) -> Izquierda
% f4=u(a,y)=u(n,j) -> Derecha
% a,b son los extremos de los intervalos [0,a] y [0,b]
% h es el tama~no de paso
% epsilon es la tolerancia
% U es la matriz donde se almacena la solucion numerica
n=fix(a/h)+1;
m=fix(b/h)+1;
pp=(a*(feval(f1,0)+feval(f2,0))+b*(feval(f3,0)+feval(f4,0)))/(2*a+2*b);
U=pp*ones(n,m)*0.9;
%condiciones a la frontera
U(1,1:m)=feval(f3,0:h:(m-1)*h)';
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
      rij=(U(i,j+1)+U(i,j-1)+U(i+1,j)+U(i-1,j)-4*U(i,j))/4
      U(i,j)=U(i,j)+w*rij;
      if rmax<=abs(rij)
        rmax=abs(rij);
      end
    end
  end
surfc(U);
end