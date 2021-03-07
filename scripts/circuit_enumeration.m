function [NegativeCycles,PositiveCycles,PCycles,NCycles] = circuit_enumeration(G)
% An algorithm to enumerate all the elementary circuits of a directed graph.
% The algorithm uses back-tracking with lookahead to avoid unnecessary work,
% and it has a time bound of O((V+E)(C+1)) when applied to a graph with V vertices,
% E edges, and C elementary circuits.

mark=[];
marked_stack=[];
point_stack=[];
NegativeCycles = 0;
PositiveCycles = 0;

sizeG = length(G);

NCycles(sizeG) = 0;
PCycles(sizeG) = 0;


%dlmwrite('cycles.csv',[]); %% Create an empty csv file %%

for i=1:length(G)
    mark(i)=false;
end

for s = 1:length(G)
    
    [f, NegativeCycles,PositiveCycles,PCycles,NCycles] = backtrack(s,s,G,PCycles,NCycles, marked_stack, point_stack ,mark,NegativeCycles,PositiveCycles);
    
    while length(marked_stack)>0
        [u , marked_stack] = stack_pop (marked_stack);
        mark(u)= false;
    end
end

%display('------ End of Procedure ----');
end


function [f, NegativeCycles,PositiveCycles,PCycles,NCycles] = backtrack(s,v,G,PCycles,NCycles, marked_stack, point_stack ,mark,NegativeCycles,PositiveCycles)

f = false;

[point_stack] = stack_push (point_stack,v);

mark(v) = true;

[marked_stack] = stack_push (marked_stack,v);

A = children(G, v);

for w = A(:)'
    
    if w<s
        %delete w from A
        pos = find(A == w);
        sz = length(A);
        A = [A(1:pos-1) A(pos+1:sz)];
        
    elseif s==w
        %cycle found from s to v to s given by point_stack
        f = true;
        
        Path = [point_stack s];
        
        %dlmwrite('cycles.csv', Path, '-append')
        negative = 0;
        
        PathSize = length(Path);
        for k = 1 : PathSize - 1
            if G(Path(k),Path(k+1))<0
                negative = negative+1;
            end
        end
        if mod(negative,2) == 1
            NegativeCycles = NegativeCycles+1;
           % disp('------ Negative ----');
           for q = 1:PathSize-1
               NCycles(Path(q)) = NCycles(Path(q)) + 1;
           end     
        else
            PositiveCycles = PositiveCycles + 1;
            % disp('------ Positive ----');
           for q = 1:PathSize-1
               PCycles(Path(q)) = PCycles(Path(q)) + 1;
           end           
        end
    elseif mark(w)==false
        [g, NegativeCycles,PositiveCycles,PCycles,NCycles] = backtrack(s,w,G,PCycles,NCycles, marked_stack, point_stack ,mark,NegativeCycles,PositiveCycles);
        f = (g | f);
    end
end

if f==true
    % if an elementary cycle continuing the partial path on the stack has been found
    while marked_stack(end)~=v
        [u , marked_stack] = stack_pop (marked_stack);
        mark(u)= false;
    end
    %dele v from marked_stack
    [u , marked_stack] = stack_pop (marked_stack);
    mark(v)=false;
end
[u , point_stack] = stack_pop (point_stack);

return
end
