import java.io.*;
class Basic {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		//col =  1, 2 , 3 .... N
		for(int i=1;i<=N;i++)
		{
			//row = 1,2,3...N
			for(int j=1;j<=N;j++)
			{
				//data = col*row
				System.out.print(i*j+" ");
			}
			//줄바꿈
			System.out.println();
		}
	}
}