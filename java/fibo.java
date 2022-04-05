
public class fibo {
	
	public static int[] memo = new int[100];
	public static void main(String[] args) {

		for(int i=1; i< 10; i++) {
			System.out.print(fibo(i) + ", ");
		}
	}
	
  // fibo memoization
	public static int fibo(int n) {
		
		if(n <=2) {
			return 1;
		}
		if(memo[n] != 0) {
			return memo[n];
		}
		memo[n] = fivo(n-1) + fivo(n-2);
		return memo[n];
		
	}
	

}
