T1 =0.5;
T2 =0.5; 
f = 20 ;
t=linspace(0,3*T1,1000);
Mz=(1-exp(-t/T1));
Mx=exp(-t/T2).*(sin(2*pi*f.*t));
My=exp(-t/T2).*(cos(2*pi*f.*t)); 
figure,
view([3,3,2]);
axis([-max(Mx) max(Mx) -max(My) max(My) 0 max(Mz)]);
curve = animatedline('LineWidth' , 0.002 , 'Color','c');
hold on
grid on
for i=1:length(t)
  addpoints(curve ,Mx(i),My(i),Mz(i)); 
h2=plot3([0,Mx(i)],[0,My(i)],[0,Mz(i)],'r','LineWidth',2);
h3=plot3([0,Mx(i)],[0,My(i)],[0,0],'b','LineWidth',2);
h4=plot3([0,0],[0,0],[0,Mz(i)],'k','LineWidth',2);
drawnow 
pause(0.01)
delete(h2)
delete(h3)
delete(h4)
end
