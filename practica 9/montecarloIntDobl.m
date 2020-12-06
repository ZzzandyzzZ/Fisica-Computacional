clear, clf, hold off
m=100000; veces=50;
ax = 0; bx = pi;
ay = 0; by = pi/2;
az =-1; bz=1;
sa = 0; saa = 0;
for k=1:veces
  n=0;
  for i=1:m
    r=rand; x = ax + (bx-ax)*r;
    r=rand; y = ay + (by-ay)*r;
    r=rand; z = az + (bz-az)*r;
    %if (y<=exp(-x^2))
    %if(y<=sqrt(x) && y>=x^2)
    if(z<=sin(x)*cos(y-pi))
      n=n+1;
      px(n)=x; py(n)=y;pz(n)=z;
    end
  end
  area = n*(by-ay)*(bx-ax)*(bz-az)/m;
  sa = sa + area;
  saa = saa + area^2;
end
disp("TERMINO")
prom = sa/veces;
desv = sqrt(veces*saa-sa^2)/veces;
promedio = num2str(prom);
desviacion = num2str(desv);
plot3 (px,py,pz,'.'),
title('Areas por el metodo MonteCarlo');
xlabel('x');
ylabel('y');
axis([-3,3,-4,4])
text(0.5,3.5,promedio);
text(1.5,3.5,'+-');
text(2,3.5,desviacion);