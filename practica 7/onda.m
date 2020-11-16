function U=onda(f,g,a,b,v,h,k)
% f es la condici´on inicial de la posici´on
% g es la condici´on inicial de la velocidad
% v es la velocidad de propagaci´on de la onda
% a es la longitud de la cuerda
% b es la tiempo que se necesita para evaluar la onda
% h es la tama~no de paso para el espacio
% k es la tama~no de paso para el tiempo
% U es la matriz donde se almacena la solucion numerica
n=ceil(a/h)+1;
m=ceil(b/k)+1;
n
m
% r es calculo para la condicion de estabilidad
r=v*k/h;
r1=r^2;
r2=r^2/2;
s1=1-r^2;
s2=2*(1-r^2);
U=zeros(n,m);
% calculo de las primeras dos filas
for i=2:n-1
U(i,1)=feval(f,h*(i-1));
a=h*(i-1)
U(i,2)=s1*feval(f,h*(i-1))+k*feval(g,h*(i-1))+r2*(feval(f,h*i)+
+feval(f,h*(i-2)));
end
U
% calculo a partir de la tercera fila
for j=2:m-1
for i=2:n-1
U(i,j+1)= s2*U(i,j)+r1*(U(i-1,j)+U(i+1,j))-U(i,j-1);
end
surf(U)
end
