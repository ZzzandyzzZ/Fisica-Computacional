clear, clf, hold off
m=20000; veces=50;
ax = -sqrt(2); bx = sqrt(2);
ay = -sqrt(3); by = sqrt(3);
az =-sqrt(4); bz=sqrt(4);
sa = 0; saa = 0;
for k=1:veces
  n=0;
  for i=1:m
    r=rand; x = ax + (bx-ax)*r;
    r=rand; y = ay + (by-ay)*r;
    r=rand; z = az + (bz-az)*r;
    %if (y<=exp(-x^2))
    %if(y<=sqrt(x) && y>=x^2)
    if(x^2/2+y^2/3+z^2/4<=1)
      n=n+1;
      px(n)=x; py(n)=y;pz(n)=z;
    end
  end
  area = n*(by-ay)*(bx-ax)*(bz-az)/m;
  sa = sa + area;
  saa = saa + area^2;
end
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