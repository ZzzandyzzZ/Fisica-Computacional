clear, clf, hold off
m=100; veces=10;
ax = -0.5; bx = 4;
ay = -1; by = 3;
sa = 0; saa = 0;
for k=1:veces
  n=0;
  for i=1:m
    r=rand; x = ax + (bx-ax)*r;
    r
    r=rand; y = ay + (by-ay)*r;
    r
    %if (y<=exp(-x^2))
    %if(y<=sqrt(x) && y>=x^2)
    if(y>=x-1&&y^2<=2*x+1)
      n=n+1;
      px(n)=x; py(n)=y;
    end
  end
  area = n*(by-ay)*(bx-ax)/m;
  sa = sa + area;
  saa = saa + area^2;
end
prom = sa/veces;
desv = sqrt(veces*saa-sa^2)/veces;
promedio = num2str(prom);
desviacion = num2str(desv);
plot (px,py,'.'),
title('Areas por el metodo MonteCarlo');
xlabel('x');
ylabel('y');
axis([-3,3,-4,4])
text(0.5,3.5,promedio);
text(1.5,3.5,'+-');
text(2,3.5,desviacion);