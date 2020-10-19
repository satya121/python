import java.util.*;

public class Main{
    public static int min(int a, int b){
        if( (a == b) && (a == Integer.MAX_VALUE))
            return (Integer.MAX_VALUE-1);
        
        if(a<b)
            return a;
        return b;

    }



    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int T = scan.nextInt();
        while(T-- > 0){
            int n = scan.nextInt();
            n = scan.nextInt();
            

            
            int[][] A = new int[n][n];

            for(int i=0; i< A.length; i++){
                for(int j=0; j<A[0].length; j++)
                    A[i][j] = scan.nextInt();
            }

            int distances[][] = new int[n][n];
            

            for(int i=0; i<distances.length; i++){
                for(int j=0; j<distances.length; j++)
                distances[i][j] = 1000000; // marking distances as very far away
            }
            distances[0][0] = 0;

            for (int i=0; i<distances.length; i++){
                for(int j=0; j<distances.length; j++){
                    int right = distances[i][j] +1;
                    int down = distances[i][j]+1;
                    int downright = distances[i][j]+1;

                    if(A[i][j] == 1) // we ignore the obstacles
                        {
                            distances[i][j] = 1000000;
                            continue;
                        }
					
                    // update diagonal if possible

                    if(i==j && i!=distances.length-1) 
                        distances[i+1][j+1] = min(distances[i][j]+1, distances[i+1][j+1]);
                    
                    // update right if it's possible to go right
                    
                    if(j<distances.length-1)
                        distances[i][j+1] = min(distances[i][j] +1, distances[i][j+1]);
                        
                    // update down if it's possible to go down
                    if(i<distances.length-1)
                        distances[i+1][j] = min(distances[i][j] +1, distances[i+1][j]);
                }
            }

            System.out.println(distances[n-1][n-1]);





        }
    }
}
