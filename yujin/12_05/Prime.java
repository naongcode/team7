import java.io.*;
class Prime {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		for(int i=0;i<N;i++)
		{
			int num = Integer.parseInt(br.readLine());
			if (isPrime(num))
				System.out.println("Yes");
			else
				System.out.println("No");
		}
	}
	public static boolean isPrime(int num)
	{
		
		if (num ==2)
			return true;
		//1이나 2의 배수 다 거르기
		if (num <= 1 || num%2 == 0)
			return false;
		for(int i=3;i<=Math.sqrt(num);i=i+2)
		{
			if (num%i==0)
				return false;
		}
		return true;
	}
}