function static_analysis


for k = 1:6

  % Get Weights matrix WW[nxm] from a csv file
  % Weight values should be within range [-1 1]
  fcmnumber = k;
  
  ifilename = ['../Questionnaires/ww_fcm',num2str(fcmnumber),'.csv'];
  rfilename = ['../Questionnaires/static_analysis_results_fcm',num2str(fcmnumber),'.csv'];
  
  WW = csvread(ifilename);
  
  [n, m] = size(WW);
  
  Edges = 0;
  EdgesWeight = 0;
  
  InDegree(n) = 0;
  OutDegree(n) = 0;
  TotalDegree(n) = 0;
  InValDegree(n) = 0;
  OutValDegree(n) = 0;
  TotalValDegree(n) = 0;
  
  for i = 1:n
      for j = 1:m
              if (WW(i,j)==0)
                  Adj(i,j) = 0;
              else
                  Adj(i,j) = 1;
                  Edges = Edges+1;
                  InDegree(j) = InDegree(j) + 1;
                  OutDegree(i) = OutDegree(i) + 1; 
                  InValDegree(j) = InValDegree(j) + abs(WW(i,j));
                  OutValDegree(i) = OutValDegree(i) + abs(WW(i,j));
                  EdgesWeight = EdgesWeight + abs(WW(i,j));
              end
      end
  end
  
  WW;
  Adj;
  EdgesWeight;
  Edges;
  
  Density = Edges / (n*(n-1));
  TotalDegree = OutDegree + InDegree;
  TotalValDegree = OutValDegree + InValDegree;
  
  %[NegativeCycles,PositiveCycles,PCycles,NCycles] = circuit_enumeration(WW);
  
  k
  %NegativeCycles
  %PositiveCycles
  Edges
  Density
    
  result(n,14) = 0;
  
  result(:,1) = InDegree;
  result(:,2) = OutDegree;
  result(:,3) = TotalDegree;
  result(:,4) = InDegree/(n-1);
  result(:,5) = OutDegree/(n-1);
  result(:,6) = TotalDegree/(2*(n-1));
  
  result(:,7) = InValDegree;
  result(:,8) = OutValDegree;
  result(:,9) = TotalValDegree;
  result(:,10) = InValDegree/EdgesWeight;
  result(:,11) = OutValDegree/EdgesWeight;
  result(:,12) = TotalValDegree/(2*EdgesWeight);
  
  %result(:,13) = PCycles;
  %result(:,14) = NCycles;
  
  %csvwrite(rfilename,result)


end


