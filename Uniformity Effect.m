z = (3-2.5).*rand(100,1) + 2;
x = (100-1).*rand(100,1) + 1;
y = (100-1).*rand(100,1) + 1;
xlin = linspace(min(x),max(x),33);
ylin = linspace(min(y),max(y),33);
[X,Y] = meshgrid(xlin,ylin);
f = scatteredInterpolant(x,y,z);
Z = f(X,Y);
figure
mesh(X,Y,Z) %interpolated
axis tight; hold on
stem3(x,y,z,'.','MarkerSize',15) %nonuniform