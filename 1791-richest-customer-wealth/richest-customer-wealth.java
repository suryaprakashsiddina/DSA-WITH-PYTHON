class Solution {
    public int maximumWealth(int[][] accounts) {
       int row = accounts.length; //for no.of rows
       int col = accounts[0].length;  //for no.of cols
       int ans = Integer.MIN_VALUE; //least minimum value for all integers
       for(int i = 0; i < row; i++){
           int sum = 0;
           for(int j = 0 ; j < col; j++){
               sum = sum + accounts[i][j];
           }
           if(sum > ans){
               ans = sum;
           }
       }
       return ans;
    }
}