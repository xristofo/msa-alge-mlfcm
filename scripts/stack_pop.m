function [z , y] = stack_pop (x)

z = x(end);
x(end) = [];
y = x;

end
