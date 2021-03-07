function [y] = stack_push (x,value)

x(end+1) = value ;
y = x;

end